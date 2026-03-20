# Username OSINT Tool

A lightweight OSINT tool for checking username availability across multiple platforms.

> ⚠️ This tool is intended for educational and authorized OSINT purposes only.

---

## 🔍 Features

* Username input support
* Multi-site profile checking
* Fast HTTP-based scanning
* Clean and readable terminal output
* Basic detection logic (status + content check)
* Modular architecture (easy to expand)
* JSON output support (optional)

---

## 📦 Installation

```bash
git clone https://github.com/k4yraa/username-osint-tool.git
cd username-osint-tool
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python main.py username
```

### Example

```bash
python main.py srxaixl
```

---

## 🧠 How It Works

* Sends HTTP requests to predefined platforms
* Checks response status codes
* Analyzes page content for "not found" patterns
* Determines whether a username exists or not

---

## 📁 Project Structure

```
username-osint-tool/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
└── modules/
    ├── __init__.py
    ├── checker.py
    ├── formatter.py
    └── sites.py
```

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized testing only.
Do not use it against systems without permission.
The user is responsible for any misuse.

---

## 📝 Notes

* Results may vary depending on website behavior
* Some platforms may block requests or return false positives
* Detection logic is basic and can be improved

---

## 🧩 Future Improvements

* More platform integrations
* Proxy / TOR support
* Async requests (faster scanning)
* Web interface (GUI)
* Advanced detection (AI / pattern-based)

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a star ⭐
