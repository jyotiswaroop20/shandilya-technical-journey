# Python program using variables to show Linux system info

import platform
import os

# variables
system_name = platform.system()
release = platform.release()
user = os.getlogin()
current_date = os.popen("date").read()
uptime = os.popen("uptime -p").read()
disk_usage = os.popen("df -h").read()
firewall = os.popen("firewall-cmd --list-all").read()


# print information
print("System Name:", system_name)
print("Release Version:", release)
print("Current User:", user)
print("Current Date & Time:", current_date)
print("System Uptime:", uptime)
print("Disk Usage Information:")
print(disk_usage)
print(firewall)
