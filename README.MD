# 🕵️‍♂️ Secret CRYPTO App

A discrete crypto dashboard built with **Python** and **Tkinter**. the interface is locked behind the **Konami Code**. Once unlocked, it provides real-time price tracking and dynamic market visualization.

## ✨ Key Features

* **🔐 Secret Access:** The main dashboard is hidden by default. You must enter the **Konami Code** on your keyboard to reveal the app.
* **₿ Multi-Asset Tracking:** Displays live prices for **Bitcoin (BTC)**,  **Solarium (SOL)** and **Ethereum (ETC)**.
* **📈 Dynamic Graphing:**
    * The graph turns **Green** 🟢 when the price increases.
    * The graph turns **Red** 🔴 when the price decreases.
* **⏸️ Pause Control:** Stop the live feed and freeze the price data instantly pressing SPACE .

## 🛠️ Tech Stack

* **Language:** Python
* **GUI:** Tkinter 
* **Data:** Cryptocurrency API 

## 🚀 Installation

1.  **Clone the repository**:
    ```bash
    https://github.com/SuroTheFool/BTC_DASHBOARD
    cd BTC_DASHBOARD
    ```

2.  **Install dependencies**:
    *Needed Packages*
    ```bash
    pip install websocket-client
    pip install requests
    pip install numpy
    pip install matplotlib
    ```

3.  **Run the App**:
    ```bash
    python main.py
    ```

## 🎮 Controls & Usage

### 1. How to Unlock (The Konami Code)
When the application launches, the screen is locked. If you can't solve the enigma, Type the following sequence on your keyboard to enter:

### **↑ ↓ ← →**


### 2. Dashboard Controls
* **Pause/Resume:** Press `Space` to freeze the price updates.
* **Visuals:** Watch the graph line color to instantly gauge market sentiment (Green/Red).

## 🌳 File tree
```│   
initial.py
│   main.py
│   README.MD
│
├───crypto
│   │   crypto_ticker.py
│   │   error_handling.py
│   │   price_graph.py
│   │   secret_app.py
│   │
│   └───__pycache__
│           crypto_ticker.cpython-313.pyc
│           error_handling.cpython-313.pyc
│           price_graph.cpython-313.pyc
│           secret_app.cpython-313.pyc
│
└───img
        BTC.png
        ETH.png
        final_design.png
        SOL.png
```
## 📸 Final DESIGN

![alt text](image.png)