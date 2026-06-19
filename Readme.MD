# Stock_Tracking_IND

A lightweight Python application designed to track and monitor Indian stock market data, with seamless integration to sync and log metrics directly into a public Google Sheet. Powered by `uv` for blazing-fast dependency management.

---

## 🚀 Features

* **Indian Stock Tracking:** Fetch and monitor real-time or historical data for Indian equities.
* **Google Sheets Integration:** Automatically log, update, and track your portfolio or watchlists directly into a public Google Sheet.
* **Modern Python Tooling:** Managed with `uv` for fast, reproducible builds and dependency resolution.

---

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed:

* Python (version specified in `.python-version`)
* [uv](https://github.com/astral-sh/uv) (recommended for managing dependencies)

---

## 📦 Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/Arun8811/Stock_Tracking_IND.git
cd Stock_Tracking_IND

```


2. **Install Dependencies:**
Using `uv`, you can set up your virtual environment and install all required packages defined in `pyproject.toml` instantly:
```bash
uv sync

```



---

## 🖥️ Usage

1. **Configure your Google Sheet:** Ensure your public Google Sheet URL or ID is correctly configured within the application environment or script.
2. **Run the Tracker:**
Execute the main script to start fetching stock data and updating your sheet:
```bash
uv run main.py

```



---

## 📂 Project Structure

```text
├── .gitignore          # Standard Git ignore configurations
├── .python-version     # Target Python version
├── Readme.MD           # Project documentation
├── main.py             # Main application logic & Google Sheets sync
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock             # Locked dependency versions for reproducible builds

```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you want to add new features, fix bugs, or improve the tracking logic.
