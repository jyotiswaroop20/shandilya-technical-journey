# 🔐 Welcome Message Logger using SUID (Linux)

This is a **C program** that logs a welcome message of the currently executing user into a protected system file:


Even though this file is owned by `root` and **not writable** by normal users, this program—when compiled and configured correctly—can still allow any user to append messages to it using the **SUID permission mechanism**.

---

## 🎯 Purpose / Concept

This program is created to **demonstrate how the `SUID` (Set User ID) permission works in Linux**.

### 💡 Real-Life Analogy: `passwd` command

- On Linux, the `passwd` command allows any normal user to change their password.
- Passwords are stored in `/etc/shadow`, which is only writable by `root` and has **no write permission** for anyone else.
- Yet users can update it via `passwd`. How?

### ✅ Reason:
> The `passwd` binary has the **SUID bit set** and is **owned by root**.  
> So when a user runs it, it **executes with root's privilege** — just like root is running it.

---

## 📂 What this program does

- Finds the currently logged-in user
- Writes a message like `Welcome jyoti!` to `/var/log/user_welcome.log`
- Demonstrates that **with SUID**, a binary can perform actions on behalf of its owner (`root`), even when the calling user doesn't have permission to do so.

---

## 🧾 Sample Output

- Welcome rahul!
- Welcome anjali!


(inside `/var/log/user_welcome.log`)

---

## 🧑‍💻 Source Code

> File: `user_welcome_logger.c`

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pwd.h>

int main() {
    FILE *fp;
    char *username;
    struct passwd *pw;

    uid_t uid = getuid();
    pw = getpwuid(uid);
    if (pw == NULL) {
        perror("getpwuid failed");
        return 1;
    }

    username = pw->pw_name;

    fp = fopen("/var/log/user_welcome.log", "a");
    if (fp == NULL) {
        perror("Unable to open log file");
        return 1;
    }

    fprintf(fp, "Welcome %s!\n", username);
    fclose(fp);
    return 0;
}
```
## ⚙️ Compilation
gcc user_welcome_logger.c -o user_welcome_logger

# 🔐 Setup for SUID Demo
### 🛑 Perform this setup as root:
### 1. Create log file with root ownership and no permission for any one.
- sudo touch /var/log/user_welcome.log
- sudo chmod 000 /var/log/user_welcome.log

### 2. Move and set SUID
- sudo mv user_welcome_logger /usr/local/bin/
- sudo chmod 4755 /usr/local/bin/user_welcome_logger

## 🚀 Run as Normal User
```
./user_welcome_logger
```  
You will see the Welcome <username>! message appended in /var/log/user_welcome.log.

## 🧠 Learning Outcome
 * 🔐 Understand how SUID works in Linux.
 * 👑 Understand how passwd works even without direct permission to /etc/shadow.
 * 🧪 Practice real-world system programming and privilege escalation responsibly.

## ⚠️ Security Warning

- Never set SUID on scripts or sensitive binaries carelessly.
- Misuse can lead to privilege escalation and system compromise.
- Use this only for educational/demo purposes.

## 📜 License

- MIT License – Free to use for educational purposes.

## 👨‍💻 Author

**Jyoti Swaroop Mani Tripathi**  
Linux & DevOps Learner | Exploring System Internals
