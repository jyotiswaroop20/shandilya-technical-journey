#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void showUptime();
void showCPULoad();
void showMemoryUsage();
void showDiskUsage();
void showLoggedUsers();
void showActiveServices();
void showNetworkInfo();

int main(void)
{
    int choice;
    char input[10];
    
    while(1){
        system("clear");
        printf("\033[1;34m==========================================\033[0m\n");
        printf("     \033[1;36m🐧 Linux System Admin Menu Tool\033[0m\n");
        printf("\033[1;34m==========================================\033[0m\n");
        printf("\033[1;33m1.\033[0m System Uptime\n");
        printf("\033[1;33m2.\033[0m CPU Load\n");
        printf("\033[1;33m3.\033[0m Memory Usage\n");
        printf("\033[1;33m4.\033[0m Disk Usage\n");
        printf("\033[1;33m5.\033[0m Logged-in Users\n");
        printf("\033[1;33m6.\033[0m Active Services\n");
        printf("\033[1;33m7.\033[0m Network Information\n");
        printf("\033[1;33m8.\033[0m Exit\n");
        printf("\033[1;34m------------------------------------------\033[0m\n");
        printf("\033[1;36mEnter your choice [1-8]: \033[0m");
        fgets(input, sizeof(input),stdin);
        if (input[0] == '\n'){
            printf("\033[1;31m❌ Input cannot be blank! Please enter a valid choice.\033[0m\n");
            printf("Press Enter to continue...");
            getchar();
            continue;
        }

        printf("\033[1;34m------------------------------------------\033[0m\n");
        choice = atoi(input);
        switch(choice){

            case 1:
                showUptime(); 
                break;

            case 2:
                showCPULoad();
                break;

            case 3:
                showMemoryUsage();
                break;

            case 4:
                showDiskUsage();
                break;

            case 5:
                showLoggedUsers();
                break;

            case 6:
                showActiveServices();
                break;

            case 7:
                showNetworkInfo();
                break;

            case 8:
                printf("\033[1;31m👋 Exiting... Have a great day!\033[0m\n");
                exit(0);

            default:
                printf("\033[1;31m❌ Invalid choice! Please enter between 1 to 8.\033[0m\n");

        }
        printf("\n\033[1;33mPress Enter to continue...\033[0m");
        getchar();

    }
    return 0;  
}

// 🕒 1. System Uptime
void showUptime() {
    printf("\033[1;32m🕒 System Uptime:\033[0m\n");
    system("uptime -p");
}

// ⚙️ 2. CPU Load
void showCPULoad() {
    printf("\033[1;32m⚙️  CPU Load Average:\033[0m\n");
    system("top -bn1 | grep 'load average'");
}

// 🧠 3. Memory Usage
void showMemoryUsage() {
    printf("\033[1;32m🧠 Memory Usage:\033[0m\n");
    system("free -h");
}

// 💾 4. Disk Usage
void showDiskUsage() {
    printf("\033[1;32m💾 Disk Usage:\033[0m\n");
    system("df -hT | awk 'NR==1 || /\\/$/'");
}

// 👥 5. Logged-in Users
void showLoggedUsers() {
    printf("\033[1;32m👥 Logged-in Users:\033[0m\n");
    system("who");
}

// 🟢 6. Active Services
void showActiveServices() {
    printf("\033[1;32m🟢 Active Services (Top 20):\033[0m\n");
    system("systemctl list-units --type=service --state=running | head -20");
}

// 🌐 7. Network Information
void showNetworkInfo() {
    printf("\033[1;32m🌐 Network Information:\033[0m\n");
    system("ip -br addr");
}