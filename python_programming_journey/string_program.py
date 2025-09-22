class User:
    def __init__(self , first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(self.first_name , self.last_name, sep=" ")

    def print_length(self):
        print(len(self.first_name + self.last_name))

u1 = User(input("Enter your first name: ") , input("Enter your last name: "))
u1.print_length()