import pyautogui
import time
import subprocess
import pygetwindow as gw
import win32gui
import win32con

# Launch Angry IP Scanner
subprocess.Popen(r'"C:\Program Files\Angry IP Scanner\ipscan.exe"')
time.sleep(5)  # Wait for it to open

# Bring the window to the front
window = None
for win in gw.getWindowsWithTitle('Angry IP Scanner'):
    window = win
    break

if window:
    window.activate()
    window.maximize()
    time.sleep(1)
    
    # Click the center of the window to ensure it's focused
    win_center_x = window.left + window.width // 2
    win_center_y = window.top + window.height // 2
    pyautogui.moveTo(win_center_x, win_center_y)
    pyautogui.click()

    # Press Enter to start scan
    time.sleep(0.5)
    pyautogui.press('enter')


else:
    print("Could not find Angry IP Scanner window.")
