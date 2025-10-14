#!/bin/bash
# ==========================================
#   🐧 Linux System Administration Menu Tool
# ==========================================

# 🎨 Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

while true
do
    clear
    echo -e "${BLUE}==========================================${NC}"
    echo -e "     ${CYAN}🐧 Linux System Admin Menu Tool${NC}"
    echo -e "${BLUE}==========================================${NC}"
    echo -e "${YELLOW}1.${NC} System Uptime"
    echo -e "${YELLOW}2.${NC} CPU Load"
    echo -e "${YELLOW}3.${NC} Memory Usage"
    echo -e "${YELLOW}4.${NC} Disk Usage"
    echo -e "${YELLOW}5.${NC} Logged-in Users"
    echo -e "${YELLOW}6.${NC} Active Services"
    echo -e "${YELLOW}7.${NC} Network Information"
    echo -e "${YELLOW}8.${NC} Exit"
    echo -e "${BLUE}------------------------------------------${NC}"
    read -p "$(echo -e ${CYAN}"Enter your choice [1-8]: "${NC})" choice
    echo -e "${BLUE}------------------------------------------${NC}"

    case $choice in
        1)
            echo -e "${GREEN}🕒 System Uptime:${NC}"
            uptime
            ;;
        2)
            echo -e "${GREEN}⚙️  CPU Load Average:${NC}"
            top -bn1 | grep "load average"
            ;;
        3)
            echo -e "${GREEN}🧠 Memory Usage:${NC}"
            free -h
            ;;
        4)
            echo -e "${GREEN}💾 Disk Usage:${NC}"
            df -hT | awk 'NR==1 || /\/$/'
            ;;
        5)
            echo -e "${GREEN}👥 Logged-in Users:${NC}"
            who
            ;;
        6)
            echo -e "${GREEN}🟢 Active Services:${NC}"
            systemctl list-units --type=service --state=running | head -20
            ;;
        7)
            echo -e "${GREEN}🌐 Network Information:${NC}"
            ip -br addr
            ;;
        8)
            echo -e "${RED}👋 Exiting... Have a great day!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Invalid choice! Please enter between 1 to 8.${NC}"
            ;;
    esac

    echo
    read -p "$(echo -e ${YELLOW}"Press Enter to continue..."${NC})"
done

