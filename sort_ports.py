import csv
import os

# === Known ports info ===
PORT_INFO = {
    "22": ("SSH (Secure Shell)", "Brute-force attacks, outdated algorithms, remote code execution"),
    "80": ("HTTP (Web Server)", "Cross-site scripting (XSS), directory traversal, outdated web software"),
    "443": ("HTTPS (Secure Web)", "Misconfigured SSL/TLS, BEAST/Heartbleed"),
    "445": ("SMB (Windows File Sharing)", "EternalBlue, WannaCry, SMBv1 vulnerabilities"),
    "3389": ("RDP (Remote Desktop)", "BlueKeep, brute-force, unpatched services"),
    "5900": ("VNC (Remote Desktop)", "No encryption, weak auth, GUI hijacking"),
}

input_file = "ipscan_results.csv"
output_file = "sorted_by_ports.csv"

if not os.path.exists(input_file):
    print(f"❌ Could not find {input_file}")
    exit()

rows = []

with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ip = row.get("IP", "").strip()
        ports = row.get("Ports", "").strip()
        hostname = row.get("Hostname", "").strip()

        if not ip or not ports:
            continue

        for port in ports.split('.'):
            port = port.strip()
            if port.isdigit():
                desc, vulns = PORT_INFO.get(port, ("Unknown", ""))
                rows.append({
                    "Port": port,
                    "IP": ip,
                    "Hostname": hostname or "Unknown",
                    "Description": desc,
                    "Common Vulnerabilities": vulns
                })

# Write the enhanced output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Port", "IP", "Hostname", "Description", "Common Vulnerabilities"
    ])
    writer.writeheader()
    for row in sorted(rows, key=lambda r: int(r["Port"])):
        writer.writerow(row)

print(f"✅ Ports sorted with descriptions and vulnerabilities into {output_file}")
