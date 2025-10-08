import subprocess

def user_audit():
    print("=== 👤 User Audit Report ===")
    users = subprocess.getoutput("cut -d: -f1 /etc/passwd")
    print(users)

    print("\n--- Sudoers ---")
    sudoers = subprocess.getoutput("grep -v '^#' /etc/sudoers | grep ALL")
    print(sudoers)

if __name__ == "__main__":
    user_audit()