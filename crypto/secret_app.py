import tkinter as tk
from tkinter import ttk
from .crypto_ticker import CryptoTicker


class SecretTickerApp:
    def __init__(self, root):
        # Base of my app
        self.root = root
        self.root.title("Secret Crypto Dashboard")
        self.root.geometry("1500x800")
        control_frame = ttk.Frame(root, padding=10)
        control_frame.pack(fill=tk.X)
        # Can't tell you ;(
        self.secret = ["up", "down", "left", "right"]
        self.current_sequence_index = 0
        root.bind('<Key>', self.discover_secret)
        self.hidden_visible = False
        self.initial_text = ttk.Label(
            root,
            text=self.change_hint(),
            foreground="blue",
            style="TLabel",
        )
        self.initial_text.pack(pady=10)
        self.ticker_frame = ttk.Frame(root, padding=20)
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

    def discover_secret(self, event):
        """Show my tickers with Konami Code."""
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
            return "To find The secret..."
