# 💀 Ransom Bae

A prank-style fullscreen GUI "ransomware" simulation made using Python and Tkinter. Ideal for trolling your friends or classmates by pretending their GPA is at stake — unless, of course, they bring you a cold coffee ☕.

> ⚠️ **Disclaimer:** This project is for educational and prank purposes only. It does **not** encrypt any files or cause real harm.

---

## 🚀 Features

- 🖥️ Fullscreen app with system key blocking.
- 😈 Fake ransom note demanding cold coffee.
- ⏱️ Countdown timer simulating urgency (default 5 mins).
- 🔐 Blocks Escape, Alt+F4, Ctrl+W, F11, and even Windows key.
- 🔓 Hidden exit combo: `CTRL + Q`.

---

## 🖼️ Preview

![Ransom Bae Screenshot](screenshot.png) *(Optional: Add your screenshot here)*

---

## 🛠️ Setup

### 🔹 Requirements (for script version)
- Python 3.x
- `keyboard` module:
```bash
  pip install keyboard
````

### 🔹 Running as `.py`

```bash
python ransom_bae.py
```

### 🔹 Creating the `.exe`

Run the following command to generate a standalone Windows executable:

```bash
python -m PyInstaller --noconsole --onefile --icon=path\to\icon.ico --name=final_project ransom_bae.py
```

> **Note**: If `CTRL+Q` exit doesn't work in the `.exe`, try adjusting permissions or run as administrator. Some keyboard hooks require elevated access OR you can press power button to shutdown.

---

## 🔑 Secret Exit

To escape the app, press:

```
CTRL + Q
```

---

## ⚙️ Buttons Explained

* 💸 **Pay Ransom** — Simulates paying for file decryption.
* 💻 **Try to Hack Back** — Shows failure message (you ain't Neo).
* 😵 **Give Up** — Accepts defeat, GPA = RIP 💀.

---

## 🧃 Motivational Message

> "Bring cold coffee, save your GPA."

---

## 📂 File Structure

```
ransom_bae/
├── ransom_bae.py         # Main prank ransomware script
├── final_project.exe     # Compiled executable (Windows)
├── README.md             # You're reading this
└── ransom_bae/Github-Octicons-Copilot-error-16.ico            # Optional custom icon
```

---

## 📜 License

MIT License. Prank responsibly.


