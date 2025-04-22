# ⚡ Angry IP Live Tracker & Port Sorter

A Python‑powered automation tool that monitors live IP scan results from Angry IP Scanner, exports data automatically, and generates a detailed, sorted report of open ports with common vulnerability annotations.

---

## 🚀 Project Highlights

- ✅ Automatically triggers Angry IP Scanner export on a set interval  
- 🌐 Live IP detection with real‑time console status updates  
- 📑 Automated port sorting into a final Excel report  
- 🔍 Includes descriptions and known vulnerabilities for each open port  
- 🤖 Fully automated once initiated via batch script  

---

## 🧠 Technologies Used

- **Python 3.9+**  
- **pyautogui**, **pywin32** for GUI automation  
- **Angry IP Scanner** for network scanning  
- **CSV** and **Excel** handling via Python’s built‑in modules and `pandas`  
- **Windows OS** (tested on Windows 10)  

---

## 🗂️ Project Structure

```
ip_scanner/
├── live_scan_tracker.py        # Main automation & live‑update script
├── sort_ports.py               # Sorter that enriches ports with vulnerability data and outputs Excel
├── ipscan_results.csv          # Auto‑exported raw scan results
├── sorted_by_ports.xlsx        # Final, sorted port report (auto-generated)
├── ip.bat                      # Batch file to launch the process
└── README.md                   # You are here!
```

---

## 📦 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/dantewarhola/ip_scanner.git
   cd ip_scanner
   ```

2. **Install Python Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Angry IP Scanner**

   - Download from [angryip.org/download](https://angryip.org/download/)  
   - In **Tools → Preferences → Ports**, add your port list (e.g., `21,22,23,80,443,445,3389`)  
   - In **Tools → Preferences → Export**:  
     - **Format:** CSV  
     - **File path:** `ipscan_results.csv` (in this project folder)  
     - **Enable:** Overwrite existing file  

---

## ▶️ How to Run

1. **Launch the Batch Script**

   Double-click or run:

   ```bash
   ip.bat
   ```

2. **Start the Automated Scan**

   - When prompted, enter **`1`** and press **Enter**  
   - The script will automatically open Angry IP Scanner and begin scanning your configured IP range

3. **Monitor & Save Results**

   - Let the scan run—results (IP addresses and open ports) will auto-save to `ipscan_results.csv`  
   - Live status updates will display in the console

4. **View the Sorted Report**

   - Once the scan completes, the script will run `sort_ports.py`  
   - A sorted, vulnerability‑annotated Excel report will be generated as:
     ```
     sorted_by_ports.xlsx
     ```

---

## 🔐 Sample Output

| Port | IP           | Hostname    | Description      | Common Vulnerabilities          |
|------|--------------|-------------|------------------|---------------------------------|
| 22   | 192.168.1.5  | raspberrypi | SSH              | Brute‑force, outdated crypto    |
| 445  | 192.168.1.22 | workstation | SMB (File Share) | EternalBlue, WannaCry (SMBv1 RCE) |
| 3389 | 192.168.1.8  | unknown     | RDP              | BlueKeep, weak auth, RCE        |

---

## 🧑‍💻 Author

**Dante Warhola**  
University of Pittsburgh — Computer Science  
Pi Kappa Phi Risk Manager | Cybersecurity Enthusiast  
[LinkedIn](https://linkedin.com/in/dante-warhola/) | [GitHub](https://github.com/dantewarhola)

---

## 📜 License

This project is licensed under the MIT License.
