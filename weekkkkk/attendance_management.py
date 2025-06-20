import os
from datetime import date


def take_attendance():
    with open("student.txt", "r") as file:
        student_data = file.readlines()
        student_attendance = []
        for student in student_data:
            student = student.strip()
            roll = student.split(",")[0]
            name = student.split(",")[1]
            while True:
                print(roll, name)
                attendance = input("Present (y/n)").lower()
                if attendance=="y" or attendance =="n":
                    student_attendance.append(f"{roll},{name},{attendance}\n")
                    break
                else:
                    print("Invalid input")
        with open(f"attendance/{date.today()}.txt","w") as file:
            file.writelines(student_attendance)


def view_attendance():
    date_input = input("Enter Date(yyyy-mm-dd) to View Attendance")
    if os.path.exists(f"attendance/{date_input}.txt"):
        with open(f"attendance/{date_input}.txt", "r") as file:
            attendance_data = file.readlines()
        for attendance in attendance_data:
            print(attendance.strip())
    else:
        print("file Does not Exist")