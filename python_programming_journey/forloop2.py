import os

try:
    while True:
        os.system("clear")
        num = int(input("Enter your value to print table: "))
        for i in range(1,11):
            if num == 0: #Indentation should be proper
                print(f"Bro if you know the table of {num} then tell me")
                os.system("sleep 3")
                os.system("clear")
                break
            else:
                print(i*num)
            
        input("\nPress Enter to continue...")
        os.system("clear")
        next_action = input("Do you want to Continue (C) or Exit (E)? ").strip().upper()
        if next_action == 'E':
            print("Exiting program... Goodbye!")
            os.system("sleep 2")
            os.system('clear')
            break
        elif next_action == 'C':
            os.system('clear')
            continue
        else:
            print("❌Invalid option! Exiting by default...")
            os.system("sleep 2")
            os.system('clear')
            break    

except ValueError:
    print("Ivalid Value! please enter intger only")