import pyautogui
import time
import re
import os
import subprocess
import sys
import csv

# === CONFIG ===
export_file = os.path.join(os.path.dirname(__file__), "ipscan_results.csv")
filename_to_type = "ipscan_results.csv"
total_ips = 2048
export_interval = 30  # seconds

seen_ips = set()


def trigger_export():
    try:
        print("\n💾 Exporting scan data...")
        pyautogui.hotkey('ctrl', 's')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite(filename_to_type)
        pyautogui.press('enter')
    except Exception as e:
        print(f"❌ Failed to export: {e}")


def get_scan_percentage():
    import win32gui
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "Angry IP Scanner" in title:
                match = re.search(r'(\d+)%', title)
                if match:
                    return int(match.group(1))
        return 0

    percent = [0]
    def grab(hwnd, lParam):
        p = enum_handler(hwnd, lParam)
        if p:
            percent[0] = p
    win32gui.EnumWindows(grab, None)
    return percent[0]


def read_ips(max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            with open(export_file, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.DictReader(f)
                ips = set()
                for row in reader:
                    ip = row.get("IP")
                    if ip:
                        ips.add(ip.strip())
                return ips
        except FileNotFoundError:
            print(f"\n⚠️ CSV file not found (attempt {attempt+1}/{max_retries}). Retrying in {delay}s...")
        except Exception as e:
            print(f"\n❌ Error reading CSV (attempt {attempt+1}/{max_retries}): {e}")
        time.sleep(delay)
    return set()


print("📡 Live scan tracker running...\n")

# === Wait before first export ===
print(f"⏳ Waiting {export_interval} seconds before first export...")
time.sleep(export_interval)

# Create export file if it doesn’t exist yet
if not os.path.exists(export_file):
    trigger_export()
    time.sleep(1)

# === Main Loop ===
scan_complete = False

while not scan_complete:
    trigger_export()

    new_ips = read_ips()
    new_found = new_ips - seen_ips

    for ip in new_found:
        print(f"\n🔹 IP found: {ip}")
    seen_ips.update(new_found)

    percent_now = get_scan_percentage()

    print(f"📊 Status: {len(seen_ips)} IPs found so far — {percent_now}% complete")

    if percent_now >= 100:
        print(f"\n✅ Scan complete — {len(seen_ips)} IPs found ({percent_now}%)")
        scan_complete = True
        break

    time.sleep(export_interval)

# === Final Export and Sort ===
trigger_export()
print("\n🔄 Final export complete. Sorting ports...")

try:
    subprocess.run(["python", "sort_ports.py"])
    print("✅ Ports sorted into sorted_by_ports.csv")
except Exception as e:
    print(f"❌ Failed to run sort_ports.py: {e}")
