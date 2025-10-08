#!/usr/bin/env python3
import os
import psutil
import platform
import subprocess

def system_health():
    os.system("clear")
    print("=== 🩺 System Health Report ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    uptime = subprocess.getoutput("awk '{print $1}' /proc/uptime")
    print(f"Uptime (sec): {uptime}")
    
if __name__ == "__main__":
    system_health()
