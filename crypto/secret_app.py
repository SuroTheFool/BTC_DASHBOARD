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
