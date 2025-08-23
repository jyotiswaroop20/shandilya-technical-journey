<h1 align="center">
  🚀 Compile The Linux Kernel in RHEL/CentOS/AlmaLinux
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Linux-Kernel-green?style=for-the-badge&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/Build-Custom-blue?style=for-the-badge&logo=gnu&logoColor=white" />
  <img src="https://img.shields.io/badge/RHEL%2FCentOS-AlmaLinux-red?style=for-the-badge&logo=redhat&logoColor=white" />
</p>

---

## ✨ Introduction
The **Linux Kernel** is like the **heart/engine** of the operating system.  
Compiling the kernel means taking the raw **source code** and building it into a working kernel that your system can boot with.

This guide explains, in **very simple steps**, how to **download, configure, compile, and install** the latest Linux Kernel in **RHEL, CentOS, and AlmaLinux**.

---

## ❓ Why Do We Compile the Kernel?

- 🔧 **Enable new hardware support** (latest WiFi, RAID, GPU drivers, etc.)  
- ⚡ **Improve performance** by removing unnecessary features  
- 🔒 **Security fixes & latest features** from upstream kernel.org  
- 🧑‍🎓 **Learning & Research** about how Linux works internally  

> 💡 Even a beginner can follow this guide step by step!

---

## ⚙️ Prerequisites

```bash
# Enable required repos (CRB/PowerTools depending on your distro)
sudo dnf config-manager --set-enabled crb

# Install required packages
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y ncurses-devel elfutils-libelf-devel openssl-devel   bc bison flex perl dwarves pahole wget xz tar gzip dracut   gcc gcc-c++ make zstd rsync rpm-build
```

- ✅ At least **20 GB free space**
- ✅ 2–4 CPU cores (for faster build)
- ✅ Root/sudo access
- ✅ Backup before experimenting  

---

## 📥 Step 1: Download the Kernel Source

```bash
mkdir -p ~/src && cd ~/src
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.10.5.tar.xz
tar -xf linux-6.10.5.tar.xz
cd linux-6.10.5
```

---

## 🛠️ Step 2: Configure the Kernel

```bash
# Start with your existing config
cp -v /boot/config-$(uname -r) .config

# Adjust automatically for new options
yes "" | make oldconfig

# OR use a menu-based UI (recommended for learning)
make menuconfig
```

---

## 🏗️ Step 3: Compile & Install

```bash
make -j"$(nproc)"         # Compile
sudo make modules_install # Install modules
sudo make install         # Install kernel
```

- If initramfs missing:
```bash
KV=6.10.5
sudo dracut --kver $KV --force
```

---

## 📌 Step 4: Update GRUB & Reboot

```bash
# For BIOS systems:
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

# For UEFI systems:
sudo grub2-mkconfig -o /boot/efi/EFI/$(. /etc/os-release; echo $ID)/grub.cfg

# Set default kernel (optional)
sudo grubby --set-default /boot/vmlinuz-6.10.5
```

Reboot your system:
```bash
sudo reboot
uname -r
```

---

## 📦 Alternative: Build Kernel as RPM (Recommended for RHEL family)

```bash
make -j$(nproc) rpm-pkg
# Install generated RPMs
sudo dnf localinstall -y ~/rpmbuild/RPMS/x86_64/kernel-*.rpm
```

- Easy to uninstall later:
```bash
sudo dnf remove kernel-<version>
```

---

## 🛡️ Rollback if Something Goes Wrong

- Select **older kernel** from GRUB menu at boot.  
- Or permanently set old kernel:
```bash
sudo grubby --set-default /boot/vmlinuz-<old-version>
```

---

## 📊 Quick Checklist

- [x] Installed build tools  
- [x] Downloaded kernel source  
- [x] Copied `.config` from current kernel  
- [x] Compiled with `make -j$(nproc)`  
- [x] Installed modules & kernel  
- [x] Updated GRUB + rebooted  
- [x] Verified with `uname -r`  

## 🧑‍💻 Author

**Jyotiswarup Tripathi**  
Self-taught **Linux System Administrator & DevOps Engineer**  
🌐 [GitHub](https://github.com/jyotiswaroop20) | 🔗 [Portfolio Website](#)  

---

## ⚠️ Disclaimer
This guide is for **educational purposes**.  
Do NOT directly compile kernels on **production servers** without testing.  

> 🛑 Always keep at least one older working kernel installed to avoid boot failures!

---

<p align="center">
  Made with ❤️ for Linux Enthusiasts
</p>

