<h1 align="center">
  🔐 Reset Forgotten Root Password in <span style="color:#EE0000;">RHEL 10</span>
</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=24&pause=1000&color=EE0000&center=true&vCenter=true&width=800&lines=🚀+Rescue+Mode+%7C+Forgotten+Root+Password+Solution;🔥+Step-by-Step+Guide+for+RHEL+10;💡+Works+when+rd.break+fails;💻+SysAdmin+Essential+Skill" alt="typing animation" />
</p>

---

## 🌟 Why This Guide?
> RHEL 9 method (`rd.break + chroot`) sometimes fails in **RHEL 10**,  
> because `chroot` / `switch_root` are missing in initramfs environment.  
> ✅ Solution: Use **Rescue Mode via Installation ISO**.

---

## 🛠️ Steps to Reset Root Password (RHEL 10)

### 1. Boot into Rescue Mode
- Insert **RHEL 10 Installation ISO/DVD**.
- In boot menu → select **Troubleshooting**.
- Choose **Rescue a Red Hat Enterprise Linux system** → Press **Enter** (⚠️ don’t press `e` here).

---

### 2. Mount System Automatically
- Rescue mode will auto-mount your installed OS under:
  ```
  /mnt/sysimage
  ```
- It is mounted in **read-write mode** (so no remount needed).

---

### 3. Enter into System
```bash
chroot /mnt/sysimage
```

---

### 4. Reset Root Password
```bash
passwd root
```
👉 Enter new password twice.

---

### 5. Relabel SELinux Context
```bash
touch /.autorelabel
```

---

### 6. Exit & Reboot
```bash
exit
reboot
```
System will reboot → SELinux will relabel automatically → 🎉 Login with your **new root password**.

---

## 📊 Quick Comparison: RHEL 9 vs RHEL 10

| Feature              | RHEL 9 (`rd.break`)                 | RHEL 10 (`Rescue Mode`)          |
|----------------------|--------------------------------------|----------------------------------|
| `chroot` available   | ✅ Yes                              | ❌ Not in initramfs, only in ISO |
| Need remount         | ✅ `mount -o remount,rw /sysroot`   | ❌ Not needed                    |
| Tool used            | `chroot /sysroot`                   | `chroot /mnt/sysimage`           |
| Media required       | ❌ No                               | ✅ Yes (Installation ISO/DVD)    |

---

## 🧭 Which Boot Option to Use (AlmaLinux 9 vs RHEL 9 vs RHEL 10)

> नीचे दिए गए तीन scenarios से **फर्क स्पष्ट** समझ आएगा और user सही path follow कर सकेगा:

### ✅ AlmaLinux 9 (जब main kernel से करना हो)
1. Boot पर GRUB menu में **main kernel** entry select करें।  
2. `e` दबाकर kernel line edit करें।  
3. `linux` (या `linux16`) वाली line के अंत में जोड़ें:  
   ```
   rd.break
   ```
4. `Ctrl + X` से boot करें → initramfs shell आएगा।  
5. Root FS को read-write करें और password reset करें:  
   ```bash
   mount -o remount,rw /sysroot
   chroot /sysroot
   passwd root
   touch /.autorelabel
   exit
   reboot
   ```

### ✅ RHEL 9 (जब **Rescue kernel** से करना हो)
1. GRUB menu में **Rescue kernel** (या “Red Hat Enterprise Linux (rescue)”) entry चुनें।  
2. `e` दबाकर kernel line edit करें और अंत में जोड़ें:  
   ```
   rd.break
   ```
3. `Ctrl + X` से boot करें।  
4. फिर वही steps:  
   ```bash
   mount -o remount,rw /sysroot
   chroot /sysroot
   passwd root
   touch /.autorelabel
   exit
   reboot
   ```

### ✅ RHEL 10 (Recommended — ISO से Rescue Mode)
1. **RHEL 10 Installation ISO/DVD** से boot करें → **Troubleshooting** → **Rescue a Red Hat Enterprise Linux system** (यहाँ `e` नहीं दबाना है)।  
2. System auto-mount होगा: `/mnt/sysimage` (read‑write)।  
3. फिर:  
   ```bash
   chroot /mnt/sysimage
   passwd root
   touch /.autorelabel
   exit
   reboot
   ```

> **Note:** RHEL 10 के initramfs environment में अकसर `chroot`/`switch_root`/`passwd` नहीं मिलते, इसलिए ISO-based Rescue Mode सबसे reliable है।

---

## 🎬 Demo Flow (Animated)

<p align="center">
  <img src="https://media.giphy.com/media/l0HlQ7LRalM1qF8Ji/giphy.gif" width="500" alt="rescue mode boot" />
</p>

---

## 💡 Pro Tips
- Always keep **installation ISO/DVD handy** for rescue.  
- If no ISO, you may try `init=/bin/bash` method in GRUB as fallback.  
- For exam/interview: Remember → **AlmaLinux 9 → main kernel + rd.break** | **RHEL 9 → rescue kernel + rd.break** | **RHEL 10 → ISO rescue mode**.

---

## 👨‍💻 Author
**Jyotiswaroop Tripathi**  
💼 Linux Administrator & DevOps Enthusiast  
🌐 https://www.linkedin.com/in/jyoti-swaroop-mani-tripathi-741980379/

