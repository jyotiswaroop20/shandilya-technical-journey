# 🔐 GRUB Password Protection & Recovery Guide (RHEL / AlmaLinux 9/10)

This guide explains how to **set, remove, and recover** GRUB password in RHEL/AlmaLinux systems.  
It also covers the recovery method if **both GRUB and root passwords are forgotten**.

---

## 🚀 1. Why Protect GRUB?

Without GRUB password protection, attackers can:
- Boot into **single-user mode** and gain root access.
- Modify kernel boot parameters from the GRUB console.
- Boot into insecure operating systems (like DOS/Windows).

---

## 🔑 2. Set GRUB Password

### Steps:
1. Edit `/etc/grub.d/10_linux` and remove `--unrestricted`:
   ```bash
   sed -i "/^CLASS=/s/ --unrestricted//" /etc/grub.d/10_linux
   ```

2. Set a new GRUB password:
   ```bash
   grub2-setpassword
   ```
   → This creates `/boot/grub2/user.cfg` containing a hashed password.

3. Regenerate GRUB configuration:
   ```bash
   grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

4. Reboot and verify. GRUB will now prompt for a password.

---

## ❌ 3. Remove GRUB Password

### Steps:
1. Edit `/etc/grub.d/10_linux` and add back `--unrestricted`:
   ```bash
   vim /etc/grub.d/10_linux
   CLASS="--class gnu-linux --class gnu --class os --unrestricted"
   ```

2. Remove the GRUB password file:
   ```bash
   rm -f /boot/grub2/user.cfg
   ```

3. Regenerate GRUB configuration:
   ```bash
   grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

4. Reboot → No password protection.

#### OR if you want the user.cfg file to remain exactly as it is with all its current settings, without removing any file, but only want to deactivate the grub password field that is currently active — so that later, whenever you want, you can simply activate the password again by changing it in one place — then the method is as follows: --------
####  EDIT GRUB CONFIGURATION AND REMOVE PASSWORD PROTECTION:
   ```bash
   vim /etc/grub2.cfg
   # Comment lines with "username" or "password_pbkdf2"
   #### and If you want to activate the password again, simply uncomment this line of code — that’s it.
   ```



---

## 🆘 4. If Both GRUB & Root Password Are Forgotten

If you forget **both GRUB password and root password**, recovery requires booting via ISO.

### Steps:
1. Boot from RHEL/AlmaLinux ISO.  
2. Select **Troubleshooting → Rescue a RHEL System**.  
3. Mount the system under `/mnt/sysimage`.  
4. Enter chroot environment:
   ```bash
   chroot /mnt/sysimage
   ```

5. Edit GRUB configuration and remove password protection:
   ```bash
   vim /etc/grub2.cfg # Comment or delete lines with "username" or "password_pbkdf2"
   touch /.autorelabel
   exit
   exit or reboot again by setting/selecting boot-up first priority hard-disk from BIOS boot menu Because your system was currently booted from the ISO image…
   ```

6. after Reboot from hard-disk → You will get kernel image and then press "e" and you will get GRUB menu without password.  
7. Reset your root password to follow further steps in system:
   ```bash
   passwd root
   ```

8. Reboot again → Both GRUB and root password are recovered.

---

## 📌 Summary

- **Set Password:**  
  `grub2-setpassword` → `/boot/grub2/user.cfg` → `grub2-mkconfig` → reboot  

- **Remove Password:**  
  `rm /boot/grub2/user.cfg` + `--unrestricted` → `grub2-mkconfig` → reboot  

- **Forgot Both (GRUB + Root):**  
  ISO boot → Rescue mode → edit `/etc/grub2.cfg` → reboot → `passwd root`  

---

## 👨‍💻 Author

- **Name:** Jyotiswaroop Tripathi  
- **Role:** Linux Administrator & DevOps Engineer  
- **Focus:** RHEL, AlmaLinux, Cloud, DevOps, and System Security
- **🌐LinkedIn:** https://www.linkedin.com/in/jyoti-swaroop-mani-tripathi-741980379/
  

---

✅ Secure your Linux boot process with GRUB password protection!  

