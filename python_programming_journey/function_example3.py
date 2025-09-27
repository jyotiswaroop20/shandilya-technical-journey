import os

def clear():
    os.system("clear")

def sleep():
    os.system("sleep 3")

def converter(dollor):
    print("=" * 35)
    print("Now Converting USD to INR...")
    inr = round(dollor * 88.67,2)
    print(f"{dollor} USD = {inr} INR")
    print("=" * 35)

try:
    clear()
    values = int(input("Enter your USD to convert INR: "))
    converter(values)
except ValueError:
    print("❌Invalid Amount Try again")
    sleep()
    clear()
