; Launch Angry IP Scanner
Run, "C:\Program Files\Angry IP Scanner\ipscan.exe"
WinWait, Angry IP Scanner
WinActivate
WinWaitActive, Angry IP Scanner

; Wait for UI to be fully ready
Sleep, 5000  ; 5 seconds — adjust if needed

; Move mouse to center to help with window focus
WinGetPos, X, Y, W, H, Angry IP Scanner
MouseMove, % X + W//2, % Y + H//2
Click

; Wait just a little more
Sleep, 500

; Press Enter to start scan
Send, {Enter}
