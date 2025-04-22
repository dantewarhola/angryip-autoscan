# ⚡ Angry IP Live Tracker & Port Sorter

A Python‑powered automation tool that monitors live IP scan results from Angry IP Scanner, exports data automatically every 30 seconds, and generates a detailed, sorted report of open ports with common vulnerability annotations.

---

## 🚀 Project Highlights

- ✅ Automatically triggers Angry IP Scanner export on a 30‑second interval  
- 🌐 Live IP detection with real‑time console status updates  
- 📑 Automated port sorting into `sorted_by_ports.csv`  
- 🔍 Includes descriptions and known vulnerabilities for each open port  
- 🤖 Fully headless once configured—just launch and let it run  

---

## 🧠 Technologies Used

- **Python 3.9+**  
- **pyautogui**, **pywin32** for GUI automation  
- **Angry IP Scanner** for network scanning  
- **CSV** handling via Python’s built‑in `csv` module  
- **Windows OS** (automation tested on Windows 10)  

---

## 🗂️ Project Structure

```
ip_scanner/
├── live_scan_tracker.py        # Main automation & live‑update script
├── sort_ports.py               # Sorter that enriches ports with vulnerability data
├── ipscan_results.csv          # Auto‑exported raw scan results
├── sorted_by_ports.csv         # Final, vulnerability‑annotated output
└── README.md                   # You are here!
```

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dantewarhola/ip_scanner.git
cd ip_scanner
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

*(`requirements.txt` includes `pyautogui` and `pywin32`)*

### 3. Install & Configure Angry IP Scanner

1. Download from [angryip.org/download](https://angryip.org/download/)  
2. In **Tools → Preferences → Ports**, add your port list (e.g., `21,22,23,80,443,445,3389`)  
3. In **Tools → Preferences → Export**:  
   - **Format:** CSV  
   - **File path:** `ipscan_results.csv` (in this project folder)  
   - **Enable:** Overwrite existing file  

---

## ▶️ Running the Project

### Step 1: Start Angry IP Scanner  
- Set your target IP range  
- Click **Start**  
- Keep the Angry IP window open (or in split‑screen)

### Step 2: Launch the Tracker

```bash
python live_scan_tracker.py
```

- The script waits 30 seconds, triggers an export, and prints new IPs/ports as they appear  
- After the scan completes, it automatically runs `sort_ports.py`

### Step 3: View Your Report

Open:

```
sorted_by_ports.csv
```

– Contains: IP, hostname, open port, description, and common vulnerabilities

---

## 🔐 Sample Output (CSV)

| Port | IP           | Hostname    | Description      | Common Vulnerabilities          |
|------|--------------|-------------|------------------|---------------------------------|
| 22   | 192.168.1.5  | raspberrypi | SSH              | Brute‑force, outdated crypto    |
| 445  | 192.168.1.22 | workstation | SMB (File Share) | EternalBlue, WannaCry (SMBv1 RCE) |
| 3389 | 192.168.1.8  | unknown     | RDP              | BlueKeep, weak auth, RCE        |

---

## 🧠 Notes

- Designed and tested on **Windows 10**  
- Ensure Angry IP remains open for the duration of the scan  
- Best used in split‑screen alongside your terminal  
- IP ranges outside `192.168.x.x` may require adjusting scan settings  

---

## 🧑‍💻 Author

**Dante Warhola**  
University of Pittsburgh — Computer Science  
Pi Kappa Phi Risk Manager | Cybersecurity Enthusiast  
[LinkedIn](https://linkedin.com/in/dante-warhola/) | [GitHub](https://github.com/dantewarhola)

---

## 📜 License

This project is licensed under the MIT License.
