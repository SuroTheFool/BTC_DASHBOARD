import tkinter as tk
from tkinter import ttk
from .crypto_ticker import CryptoTicker


class SecretTickerApp:
    def __init__(self, root):
        # Base of my app
        self.root = root
        self.root.title("Secret Crypto Dashboard")
        self.root.geometry("1500x800")
        root.configure(bg="black")
        control_frame = tk.Frame(root, bg='black', padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        # Can't tell you ;(
        self.secret = ["up", "down", "left", "right"]
        self.pause_code = ["s", "t", "o", "p"]
        self.pause_index = 0
        self.current_sequence_index = 0
        root.bind('<Key>', self.discover_secret)
        self.hidden_visible = False
        self.initial_text = tk.Label(
            root,
            text=self.change_hint(),
            fg="white",
            bg="black",
            font=("Calibri", 14, 'bold'),
            wraplength=1000,
            justify="left",
        )
        self.initial_text.pack(pady=10)
        self.ticker_frame = tk.Frame(root, bg="black", padx=20, pady=20)
        self.ticker_frame.pack(fill=tk.BOTH, expand=True)

        self.btc_ticker = CryptoTicker(
            self.ticker_frame, "btcusdt", "BTC/USDT", "img/BTC.png")

        self.eth_ticker = CryptoTicker(
            self.ticker_frame, "ethusdt", "ETH/USDT", "img/ETH.png")

        self.sol_ticker = CryptoTicker(
            self.ticker_frame, "solusdt", "SOL/USDT", "img/SOL.png")

    def on_closing(self):
        """Clean up when closing."""
        self.btc_ticker.stop()
        self.eth_ticker.stop()
        self.sol_ticker.stop()
        self.root.destroy()

    def on_pause(self, event):
        key = event.keysym.lower()
        if key == self.pause_code[self.pause_index]:
            self.pause_index += 1
            if self.pause_index == len(self.pause_code):
                self.pause_index = 0
                new_state = not self.btc_ticker.is_paused

                self.btc_ticker.is_paused = new_state
                self.eth_ticker.is_paused = new_state
                self.sol_ticker.is_paused = new_state
                print(f'Game is {'paused' if new_state else 'resumed'}')
        else:
            self.pause_index = 0

    def discover_secret(self, event):
        """Show my tickers with Konami Code."""
        self.on_pause(event)
        key = event.keysym.lower()
        if key == self.secret[self.current_sequence_index]:
            self.current_sequence_index += 1
            if self.current_sequence_index == len(self.secret):
                self.hidden_visible = True
                self.current_sequence_index = 0
                self.initial_text.configure(text=self.change_hint())
                self.btc_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.btc_ticker.start()
                self.eth_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.eth_ticker.start()
                self.sol_ticker.pack(side=tk.LEFT, padx=10,
                                     fill=tk.BOTH, expand=True)
                self.sol_ticker.start()
        else:
            self.current_sequence_index = 0

    def change_hint(self):
        if self.hidden_visible == True:
            return "HOW DID YOU DISCOVERED MY SECRET ?"
        else:
            return """\n
            (Konami code answer at the top of my README.MD)\n
            To start, look towards the sky, where birds fly and clouds pass.\n
            Next, set your eyes on the ground, where roots grow and buried treasures hide\n
            Turn your head towards the place where the sun sets in the evening, where your less used hand is often found.\n
            Finally, look to the other side, where the sun rises in the morning, where your strongest hand is."""
