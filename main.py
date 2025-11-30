
import tkinter as tk
from tkinter import ttk
import websocket
import json
import threading
from PIL import Image, ImageTk
import os

# Price graph object widget 
class PriceGraph(ttk.Frame):
    def __init__(self,parent,width=300,height=120,max_points=100):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.max_points = max_points
        self.prices = []

        self.canvas = tk.Canvas(self,width=self.width,height = self.height, bg="black")
        self.canvas.pack(fill="both",expand=True)
    def add_price(self,price:float):
        self.prices.append(price)
        if len(self.prices) > self.max_points:
            self.prices = self.prices[-self.max_points:]
        self._redraw()
    def _redraw(self):
        self.canvas.delete("all")
        if len(self.prices) < 2:
            return
        min_p = min(self.prices)
        max_p = max(self.prices)

        if max_p == min_p:
            max_p = min_p + 1e-8

        n = len(self.prices)
        # Horizontal spacing between 2 points
        x_step = self.width / (n - 1)

        def price_to_y(p):
            ratio = (p - min_p) / (max_p - min_p)
            return self.height - ratio * self.height
        for i in range(1,n):
            p0 = self.prices[i-1]
            p1 = self.prices[i]
            x0 = (i - 1) * x_step
            x1 = i * x_step
            y0 = price_to_y(p0)
            y1 = price_to_y(p1)

            color = "green" if p1 >= p0 else "red"
            self.canvas.create_line(x0,y0,x1,y1, fill=color, width=2)
class CryptoTicker:
    """Reusable ticker component for any cryptocurrency."""

    def __init__(self, parent, symbol, display_name, image_path):
        self.parent = parent
        self.symbol = symbol.lower()
        self.display_name = display_name
        self.is_active = False
        self.ws = None
        self.image_path = image_path

        # Create UI
        self.frame = ttk.Frame(parent, relief="solid",
                               borderwidth=1, padding=20)
        # Show image of the currency
        try:
            self.currency_img_pil = Image.open(self.image_path)
            self.currency_img_pil.thumbnail((64, 64), Image.Resampling.LANCZOS)
            self.tk_image_reference = ImageTk.PhotoImage(self.currency_img_pil)

            self.image_label = tk.Label(
                self.frame, image=self.tk_image_reference)
            self.image_label.pack(pady=5)

        except FileNotFoundError:
            print(f"Image file not found at: {self.image_path}")
            ttk.Label(self.frame, text="[Image N/A]").pack(pady=5)

        # Title
        ttk.Label(self.frame, text=display_name,
                  font=("Arial", 16, "bold")).pack()

        # Price
        self.price_label = tk.Label(self.frame, text="--,---",
                                    font=("Arial", 40, "bold"))
        self.price_label.pack(pady=10)

        # Change
        self.change_label = ttk.Label(self.frame, text="--",
                                      font=("Arial", 12))
        self.change_label.pack()
        # Graph with green and red line depending of the price evolution
        self.price_graph = PriceGraph(self.frame,width=320,height=120,max_points=120)
        self.price_graph.pack(pady=10)
        

    def start(self):
        """Start WebSocket connection."""
        if self.is_active:
            return

        self.is_active = True
        ws_url = f"wss://stream.binance.com:9443/ws/{self.symbol}@ticker"

        self.ws = websocket.WebSocketApp(
            ws_url,
            on_message=self.on_message,
            on_error=lambda ws, err: print(f"{self.symbol} error: {err}"),
            on_close=lambda ws, s, m: print(f"{self.symbol} closed"),
            on_open=lambda ws: print(f"{self.symbol} connected")
        )

        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def stop(self):
        """Stop WebSocket connection."""
        self.is_active = False
        if self.ws:
            self.ws.close()
            self.ws = None

    def on_message(self, ws, message):
        """Handle price updates."""
        if not self.is_active:
            return

        data = json.loads(message)
        price = float(data['c'])
        change = float(data['p'])
        percent = float(data['P'])

        # Schedule GUI update on main thread
        self.parent.after(0, self.update_display, price, change, percent)

    def update_display(self, price, change, percent):
        """Update the ticker display."""
        if not self.is_active:
            return

        color = "green" if change >= 0 else "red"
        self.price_label.config(text=f"{price:,.2f}", fg=color)

        sign = "+" if change >= 0 else ""
        self.change_label.config(
            text=f"{sign}{change:,.2f} ({sign}{percent:.2f}%)",
            foreground=color
        )
        self.price_graph.add_price(price)

    def pack(self, **kwargs):
        """Allow easy placement of ticker."""
        self.frame.pack(**kwargs)

    def pack_forget(self):
        """Hide the ticker."""
        self.frame.pack_forget()

class SecretTickerApp:
    def __init__(self, root):
        # Base of my app
        self.root = root
        self.root.title("Secret Crypto Dashboard")
        self.root.geometry("1000x400")
        control_frame = ttk.Frame(root, padding=10)
        control_frame.pack(fill=tk.X)
        # Can't tell you ;(
        self.secret = ["up", "down", "left", "right"]
        self.current_sequence_index = 0
        root.bind('<Key>', self.discover_secret)

        self.ticker_frame = ttk.Frame(root, padding=20)
        self.ticker_frame.pack(fill=tk.BOTH, expand=True)

        self.btc_ticker = CryptoTicker(
            self.ticker_frame, "btcusdt", "BTC/USDT", "img/BTC.png")

        self.eth_ticker = CryptoTicker(
            self.ticker_frame, "ethusdt", "ETH/USDT", "img/ETH.png")

        self.sol_ticker = CryptoTicker(
            self.ticker_frame, "solusdt", "SOL/USDT", "img/SOL.png")

        self.hidden_visible = False

    def on_closing(self):
        """Clean up when closing."""
        self.btc_ticker.stop()
        self.eth_ticker.stop()
        self.sol_ticker.stop()
        self.root.destroy()

    def discover_secret(self, event):
        """Show my tickers with Konami Code."""
        key = event.keysym.lower()
        if key == self.secret[self.current_sequence_index]:
            self.current_sequence_index += 1
            if self.current_sequence_index == len(self.secret):
                self.current_sequence_index = 0
                self.btc_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.btc_ticker.start()
                self.eth_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.eth_ticker.start()
                self.sol_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.sol_ticker.start()
                self.hidden_visible = True
        else:
            self.current_sequence_index = 0


if __name__ == '__main__':
    root = tk.Tk()
    app = SecretTickerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
