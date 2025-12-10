import tkinter as tk
from crypto.secret_app import SecretTickerApp
from crypto.error_handling import ConnectionsError,DataError,ImageLoadError,CryptoAppError
from tkinter import messagebox


if __name__ == '__main__':
    root = tk.Tk()
    try:
        app = SecretTickerApp(root)
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.mainloop()
    except ImageLoadError as e:
        messagebox.showerror(
            f"image error",f'{e.path}'
        )
    except DataError as e:
            messagebox.showerror(
                "Data error",
                f"{e}\nRaw data: {e.raw_data}"
            )

    except ConnectionsError as e:
        messagebox.showerror(
            "Connection error",
            f"{e}\nSymbol: {e.symbol}"
        )

    except CryptoAppError as e:
        messagebox.showerror("Crypto error", str(e))