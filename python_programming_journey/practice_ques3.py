import os
import math

# Clear screen function (Linux/Mac)
def clear():
    os.system("clear")

# Main loop
while True:
    clear()
    student_details = {"subject": {}} #Nested Dict Declearation

    # ---------- 1️⃣ Student Name Input ----------
    student_name = input("Enter the name of student: ").strip()
    if student_name.isdigit() or len(student_name) < 3:
        print("❌ Invalid input. Please enter your full name (only letters, at least 3 characters).")
        os.system("sleep 2")
        continue
    else:
        student_details["stu_name"] = student_name

    # ---------- 2️⃣ Marks Input ----------
    try:
        student_details["subject"]["physics_marks"] = int(input("Enter the marks of Physics: "))
        student_details["subject"]["chemistry_marks"] = int(input("Enter the marks of Chemistry: "))
        student_details["subject"]["math_marks"] = int(input("Enter the marks of Math: "))
    except ValueError:
        print("❌ Invalid Value! Please enter integer marks only.")
        os.system("sleep 2")
        continue  # केवल marks दोबारा लेगा, नाम नहीं

    # ---------- 3️⃣ Percentage Calculation ----------
    try:
        p = student_details["subject"]["physics_marks"]
        c = student_details["subject"]["chemistry_marks"]
        m = student_details["subject"]["math_marks"]

        student_details["percentage"] = round((p + c + m) / 3, 2)
    except Exception as e:
        print(f"⚠️ Error calculating percentage: {e}")
        os.system("sleep 2")
        continue

    # ---------- 4️⃣ Address Input ----------
    student_details["address"] = input("Enter your Address: ")

    # ---------- 5️⃣ Final Output ----------
    clear()
    print("📚 Student Report Card 📚")
    print("=" * 35)
    print("Student Name  :", student_details["stu_name"])
    print("Address       :", student_details["address"])
    print("\n📊 Score List:")
    print("Physics Marks :", student_details["subject"]["physics_marks"])
    print("Chemistry Marks:", student_details["subject"]["chemistry_marks"])
    print("Math Marks    :", student_details["subject"]["math_marks"])
    print("Percentage    :", student_details["percentage"], "%")
    print("=" * 35)
    print("\nFull Dictionary:", student_details)

    # ---------- 6️⃣ Ask to Continue ----------
    choice = input("\nDo you want to enter another student? (y/n): ").strip().lower()
    if choice != 'y':
        print("✅ Program exited.")
        break
