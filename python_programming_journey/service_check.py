import os
import subprocess

os.system("clear")
print("=== 🔧 Service Status ===")

service = input("Enter service name to check enabled or not: ")

status = subprocess.getoutput(f"systemctl is-enabled {service}")
if "enabled" in status:
    print("✅ Service is enabled")
else:
    print("❌ Service is not enabled")
    os.system("sleep 3")
    values = input("Want to enable service (yes / no): ")
    if values == "yes":
        os.system(f"systemctl enable --now {service}")
        status = subprocess.getoutput(f"systemctl is-enabled {service}")
        if "enabled" in status:
            print("✅ Now Service is enabled")
    elif values == "no":   # ✅ अब indentation सही है
        print("ok")
