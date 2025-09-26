import os
import math

while True:
    try:
        student_details = {                   #nested dictionary declearation
                "subject" :{

                }
            }
        os.system("clear")
        student_details["stu_name"] = input("Enter the name of student: ")
        if student_details["stu_name"].isdigit() or len(student_details["stu_name"]) < 3:
            print("❌ Invalid input. Please enter your full name (not numbers, not single/double character).")
            os.system("sleep 5")
            continue
        student_details["subject"]["physics_marks"] = int(input("Enter the marks of Physics: "))
        student_details["subject"]["chemistry_marks"] = int(input("Enter the marks of Chemistry: "))
        student_details["subject"]["math_marks"] = int(input("Enter the marks of Math: "))

        p = student_details["subject"]["physics_marks"]
        c = student_details["subject"]["chemistry_marks"]
        m = student_details["subject"]["math_marks"]
        print("\n")
        os.system("clear")

        student_details.update({"percentage" : float(p + c + m)/3})
        student_details.update({"address" : input("Enter your Address: ")})
        os.system("clear")
        print("Student Name : ", student_details["stu_name"])
        print("Address : ", student_details["address"])
        print("Score List:---- ", "\nPhysics_Marks : ", student_details["subject"]["physics_marks"], "\nChemistry_Marks : ", student_details["subject"]["chemistry_marks"], "\nMath_Marks : ", student_details["subject"]["math_marks"])
        print("Percentage : ", student_details["percentage"])
        print("\n")
        print(student_details)
        print("\n")
    except ValueError:
        print(f"❌Invalid Value! Please enter an integer Only.")
        os.system("sleep 3")
        os.system('clear')
        input("\nPress Enter to Exit and try again...") 

