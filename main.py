import tkinter as tk
from crypto.secret_app import SecretTickerApp

if __name__ == '__main__':
    root = tk.Tk()
    app = SecretTickerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
