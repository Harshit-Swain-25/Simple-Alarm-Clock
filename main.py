import datetime
import time
import platform
import subprocess
import sys
import os

def parse_hms(s):
    parts = s.split(':')
    if len(parts) not in (2, 3):
        raise ValueError("Use HH:MM or HH:MM:SS")
    h = int(parts[0])
    m = int(parts[1])
    sec = int(parts[2]) if len(parts) == 3 else 0
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= sec < 60):
        raise ValueError("Invalid time values")
    return h, m, sec

def wait_until(target_dt):
    try:
        while True:
            now = datetime.datetime.now()
            if now >= target_dt:
                return
            remaining = target_dt - now
            rem_str = str(remaining).split('.')[0] 
            print(f"\rTime remaining: {rem_str}   ", end='', flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAlarm cancelled.")
        sys.exit(0)

def play_alarm_sound(path, repeat=3):
    system = platform.system()
    
    if system == "Darwin":  
        if not os.path.exists(path):
            print(f"Alarm sound file not found: {path}")
            return
        for _ in range(repeat):
            try:
                subprocess.call(["afplay", path])
            except Exception as e:
                print("Could not play sound with afplay:", e)
        return
    
    elif system == "Windows":
        try:
            import winsound
            for _ in range(repeat * 2):
                winsound.Beep(1000, 500)  
            return
        except Exception:
            pass
    
    elif system == "Linux":
        for cmd in (["paplay", path], ["aplay", path]):
            try:
                for _ in range(repeat):
                    subprocess.call(cmd)
                return
            except Exception:
                continue

    for i in range(5):
        print("\aALARM! TIME UP! \a")
        time.sleep(1)

def main():
    print("=== Simple Alarm Clock ===")
    print("Options:")
    print("1) Set alarm at time (HH:MM or HH:MM:SS, 24-hour)")
    print("2) Set alarm after X seconds")
    choice = input("Choose (1 or 2): ").strip()
    
    if choice == '1':
        tstr = input("Enter time (HH:MM or HH:MM:SS): ").strip()
        try:
            h, m, s = parse_hms(tstr)
        except Exception as e:
            print("Invalid time format:", e)
            return
        now = datetime.datetime.now()
        target = now.replace(hour=h, minute=m, second=s, microsecond=0)
        if target <= now:
            target += datetime.timedelta(days=1)
    elif choice == '2':
        try:
            secs = int(input("Enter seconds from now (e.g., 10): ").strip())
            if secs < 0:
                print("Please enter a positive number.")
                return
            target = datetime.datetime.now() + datetime.timedelta(seconds=secs)
        except ValueError:
            print("Invalid seconds.")
            return
    else:
        print("Invalid choice.")
        return

    print("Alarm set for:", target.strftime("%Y-%m-%d %H:%M:%S"))

    system = platform.system()
    if system == "Darwin":
        print("Alarm sound will play using 'afplay' (macOS).")
    elif system == "Windows":
        print("Alarm sound will use winsound.Beep (Windows).")
    elif system == "Linux":
        print("Alarm sound will try paplay/aplay (Linux).")
    else:
        print("Alarm sound will use fallback terminal beep.")

    wait_until(target)
    print("\nTime reached:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    alarm_file = "/Users/harshitswain/Desktop/Simple Alarm Clock/alarm.wav"
    play_alarm_sound(alarm_file)
    print("Alarm finished.")

if __name__ == "__main__":
    main()
