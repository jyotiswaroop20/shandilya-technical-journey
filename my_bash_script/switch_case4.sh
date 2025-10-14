#!/bin/bash
# ==========================================
#  Linux System Administration Menu Tool
# ==========================================

while true
do
    echo "=========================================="
    echo "     🐧 Linux System Admin Menu Tool"
    echo "=========================================="
    echo "1. System Uptime"
    echo "2. CPU Load"
    echo "3. Memory Usage"
    echo "4. Disk Usage"
    echo "5. Logged-in Users"
    echo "6. Check Active Services"
    echo "7. Network Information"
    echo "8. Exit"
    echo "------------------------------------------"
    read -p "Enter your choice [1-8]: " choice
    echo "------------------------------------------"

    case $choice in
        1)
            echo "🕒 System Uptime:"
            uptime
            ;;
        2)
            echo "⚙️  CPU Load Average:"
            top -bn1 | grep "load average"
            ;;
        3)
            echo "🧠 Memory Usage:"
            free -h
            ;;
        4)
            echo "💾 Disk Usage:"
            df -hT
            ;;
        5)
            echo "👥 Logged-in Users:"
            who
            ;;
        6)
            echo "🟢 Active Services (systemctl list-units --type=service --state=running):"
            systemctl list-units --type=service --state=running | head -20
            ;;
        7)
            echo "🌐 Network Information:"
            ip -br addr
            ;;
        8)
            echo "👋 Exiting... Have a great day!"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice! Please enter between 1 to 8."
            ;;
    esac

    echo
    read -p "Press Enter to continue..." pause
    clear
done

