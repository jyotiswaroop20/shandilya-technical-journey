try:
    y = input("Enter your number- ")
    x = int(y)
    if x>10 and x<20:
        print(x, "is between 10 and 20")
    elif x>20 and x<30:
        print(x, "is between 20 and 30")
    elif x>30 and x<40:
        print(x, "is between 30 and 40")
    else:
        print("The value out of bound")
except ValueError:
    print("Value Invalid! Enter integer only")