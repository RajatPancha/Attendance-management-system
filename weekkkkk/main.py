from student_management import (
    add_student_record, update_student_record,
    view_student_record, delete_student
)

from attendance_management import (
    take_attendance,
    view_attendance,
)


def menu():
    run = True
    while run:
        print("Enter 1 To Add Student")
        print("Enter 2 To View Student Details")
        print("Etner 3 to Update Student")
        print("Etner 4 To Delete Student")
        print("Etner 5 To Take Attendance")
        print("Enter 6 to View Attendance")
        print("Enter 7 to end")
        option = input("Enter Menu No: ")
        if option == "1":
            add_student_record()
        elif option == "2":
            view_student_record()
        elif option == "3":
            update_student_record()
        elif option == "4":
            delete_student()
        elif option == "5":
            take_attendance()
        elif option == "6":
            view_attendance()
        elif option == "7":
            run = False
        else:
            print("Invalid choices")


menu()