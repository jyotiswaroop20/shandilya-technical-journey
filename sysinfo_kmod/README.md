# 🚀 sysinfo\_kmod — Your Own Kernel-Powered System Info Tool

> ✨ A **Linux Kernel Module** that creates a `/proc/sysinfo_kmod` entry and lets you peek directly into **uptime, memory usage, load averages, and kernel version** — straight from kernel space.

---

## 🎯 Features

* 📊 **Uptime** in seconds since boot.
* 🧠 **Total & Free RAM** in MB.
* ⚖️ **Load Average** (1, 5, 15 minutes).
* 🛠️ **Kernel Version** currently running.
* 🔒 Safe, clean, removable anytime with `rmmod` or `modprobe -r`.

---

## ⚡ Quick Start

### 1️⃣ Build

```bash
make
```

### 2️⃣ Load the module

```bash
sudo insmod sysinfo_kmod.ko   # OR recommended: sudo modprobe sysinfo_kmod
```

✅ Check kernel logs:

```bash
dmesg | tail
```

### 3️⃣ View system info

```bash
cat /proc/sysinfo_kmod
```

🔍 Example output:

```
===== System Information =====
Uptime: 3500 seconds
Total RAM: 16384 MB
Free RAM : 12000 MB
Load Avg : 0.05 0.10 0.20
Kernel   : 5.14.0-422.el9.x86_64
==============================
```

### 4️⃣ Remove the module

```bash
sudo rmmod sysinfo_kmod or modprob -r sysinfo_kmod
```

---

## 🌀 Auto-load on Reboot

Keep it alive across reboots:

```bash
sudo cp sysinfo_kmod.ko /lib/modules/$(uname -r)/extra/
sudo depmod -a
echo sysinfo_kmod | sudo tee /etc/modules-load.d/sysinfo_kmod.conf
```

---

## 🎨 Developer Info

* 👨‍💻 **Author:** Jyoti S. Tripathi
* 📝 **Description:** System Info provider via /proc
* 🔖 **Version:** 1.0
* ⚖️ **License:** GPL

Check anytime with:

```bash
modinfo sysinfo_kmod.ko
```

---

## 🧩 Why Unique?

Unlike a typical *Hello World* module, **sysinfo\_kmod** gives you **real-time, practical kernel data** that userspace tools like `free`, `uptime`, and `top` normally fetch indirectly.

Here, you own the kernel logic 🚀 — tweak it to expose **custom monitoring metrics, security hooks, or even hidden Easter eggs** 😉.

---

## 🔥 Pro Tips

* Combine with `watch` for live updates:

```bash
watch -n 2 cat /proc/sysinfo_kmod
```

* Extend code to log data into `/var/log/` or export via `sysfs`.
* Package it into an RPM and share with your team!

---

## ✨ ASCII Art Vibes

```
   _____       _        _              _   _               _
  / ____|     | |      | |            | | (_)             | |
 | (___   __ _| |_ __ _| | ___   _ __ | |_ _  ___ ___  ___| |
  \___ \ / _` | __/ _` | |/ _ \ | '_ \| __| |/ __/ _ \/ __| |
  ____) | (_| | || (_| | |  __/ | | | | |_| | (_|  __/\__ \_|
 |_____/ \__,_|\__\__,_|_|\___| |_| |_|\__|_|\___\___||___(_)
```

---

## 🌌 The Big Picture

This is not just a module. It’s your **entry point into kernel-space programming**:

* Learn Linux internals 🐧
* Build real device drivers ⚡
* Craft monitoring/security modules 🔐

**Welcome to Kernel Hacking 🚀** — You’re not reading `/proc`, you’re *owning it*.

---
