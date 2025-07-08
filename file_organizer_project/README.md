# 📂 File Organizer Bash Script (System-Level Version)

## 📝 Description

This is a system-wide Bash-based file organizer script for Linux. It uses globbing patterns to automatically sort and move files from a specified directory into categorized folders like `Documents`, `Images`, `Scripts`, and `Others`. It supports detailed logging, handles unknown file types, and can be invoked globally using the `org` command.

---

## ✨ Features

- ✅ Sorts files based on their extensions into:
  - `.txt`, `.pdf` → `Documents/`
  - `.jpg`, `.png` → `Images/`
  - `.sh` → `Scripts/`
  - All other file types → `Others/`
- ✅ Logs every file move operation in `organizer.log`
- ✅ Automatically creates destination folders
- ✅ System-wide usage with alias `org`
- ✅ Works in both **login** and **non-login** shell environments

---

## ⚙️ System-Wide Installation Steps

1. **Copy the script** to a system executable directory:
   ```bash
   sudo cp organize.sh /usr/local/bin/organize.sh
   sudo chmod +x /usr/local/bin/organize.sh
2. **Create a system-wide alias (recommended method):**
   ```bash
   sudo nano /etc/profile.d/org.sh
   ```
   **Paste the following:**
   ```
   #!/bin/bash
   alias org='/usr/local/bin/organize.sh'
3. **Make it executable:**
   ```bash
   sudo chmod +x /etc/profile.d/org.sh
4. **Reload the profile (or logout-login):**
   ```bash
   source /etc/profile
Now, the org command is available to all users in all shell sessions.

## 📤 Usage
```bash
org /path/to/target/folder
```
**Example**
```
org ~/Downloads
```

## 📋 Prerequisites Before Running
1. Ensure the target directory contains some of the following file types:

   **A -** .txt, .pdf, .jpg, .png, .sh

   **B -**  Plus some unknown types like .zip, .log, .csv to test Others/ folder

2. Make sure script has executable permissions (chmod +x)

3. Run only in non-system directories (see security tips below)

## 📂 Sample Output Folder Structure
```
/home/user/Downloads/
├── Documents/
│   └── test.txt
├── Images/
│   └── photo.jpg
├── Scripts/
│   └── script.sh
├── Others/
│   └── data.csv
└── organizer.log
```

## 📄 Sample Log (organizer.log)
```
2025-07-07 22:30:12 Moved test.txt to Documents
2025-07-07 22:30:12 Moved photo.jpg to Images
2025-07-07 22:30:12 Moved script.sh to Scripts
2025-07-07 22:30:12 Moved data.csv to Others
```

## 👨‍💻 Developer

* Name: Jyotiswarup Tripathi
* Role: Linux System Administrator (Trainee)
* Email: jyotiswaroop.niit1@gmail.com
* Location: Gorakhpur, Uttar Pradesh, India

## 🛡️ Security Tips

**🚫 Do Not Run This Command In These Folders:** 
* `/etc/`
* `/usr/`
* `/bin/`
* `/boot/`
* `/lib/`
* Any system-critical directory

**✅ Recommended Safe Locations:**
* `/home/username/Downloads`
* `/mnt/yourdisk/data`
* `/tmp/test-organize`
  
**💡 Always test in a non-critical folder first, especially if using wildcards or automated scripts.**

## 🆓 License

This script is free for educational and personal use. Attribution is appreciated. Not recommended for commercial production without further testing.
