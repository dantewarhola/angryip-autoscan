# ⚡ Angry IP Live Tracker & Port Sorter

A Python-powered automation tool that monitors live IP scan results from Angry IP Scanner, exports data automatically, and generates a detailed, sorted report of open ports with common vulnerabilities.

---

## 🚀 Features

- Automatically triggers Angry IP export every 30 seconds
- Live IP detection and console status updates
- Port sorting into `sorted_by_ports.csv`
- Includes descriptions and known vulnerabilities for common ports
- 100% automated — just set up once and let it run

---

## 📁 Project Structure

```
ip_scanner/
├── live_scan_tracker.py        # Main tracker script
├── sort_ports.py               # Port sorter with descriptions
├── ipscan_results.csv          # Live scan export (auto-created)
├── sorted_by_ports.csv         # Final port summary (auto-created)
├── requirements.txt            # Python dependencies
└── README.md                   # You're reading this!
```

---

## 💾 Installation Guide

### 1. ✅ Install Python 3.9+
Download and install Python from [python.org](https://www.python.org/downloads/).  
Make sure to check ✅ **"Add Python to PATH"** during installation.

### 2. ✅ Install Angry IP Scanner
Download it from [https://angryip.org/download/](https://angryip.org/download/)

After installation, configure it:
- Go to **Tools > Preferences > Ports**, add ports like: `21,22,23,80,443,445,3389`
- Go to **Tools > Preferences > Export**
  - Format: **CSV**
  - File path: `ipscan_results.csv` in this project folder
  - Enable **overwrite existing files**

### 3. ✅ Install Required Python Libraries

Open a terminal or command prompt inside the project folder and run:

```bash
pip install -r requirements.txt
```

#### requirements.txt
```txt
pyautogui
pywin32
```

---

## ▶️ How to Run

### Step 1: Start Angry IP Scanner
- Set your IP range
- Click "Start"
- Leave the Angry IP window **open and in focus**

### Step 2: Run the Tracker

```bash
python live_scan_tracker.py
```

### The script will:
- Wait 30 seconds
- Automatically save/export scan results every 30 seconds
- Print found IPs live in the terminal
- After 100% scan, it will auto-run `sort_ports.py`

### Step 3: View Your Report
Open the generated file:

```
sorted_by_ports.csv
```

This contains:

- Open ports
- IP addresses
- Hostnames
- Port descriptions
- Common vulnerabilities

---

## 🔐 Sample Output (CSV)

| Port | IP           | Hostname      | Description       | Common Vulnerabilities                     |
|------|--------------|---------------|-------------------|---------------------------------------------|
| 22   | 192.168.1.5  | raspberrypi   | SSH               | Brute-force, outdated crypto               |
| 445  | 192.168.1.22 | Workstation   | SMB (File Share)  | EternalBlue, WannaCry, SMBv1 RCE           |
| 3389 | 192.168.1.8  | Unknown       | RDP               | BlueKeep, weak auth, RCE                   |

---

## 🧠 Notes

- Designed for **Windows OS**
- Keep Angry IP open during the scan
- Works best when run alongside Angry IP in split-screen mode
- Tested with networks using `192.168.x.x` IP ranges

---

## 📬 Questions / Contributions

Feel free to submit an issue or pull request if you’d like to:
- Expand port vulnerability mappings
- Add headless Nmap integration
- Add GUI or log file outputs

Built with ❤️ and caffeine by [Dante Warhola].
