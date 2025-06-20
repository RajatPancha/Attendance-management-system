def add_student_record():
    roll_no = input("Enter Your Roll No")
    name = input("Enter Your Name")
    contact_no = input("Enter Your Contact No")

    with open("student.txt", "r") as student_record:
        students = student_record.readlines()
        # [
        #     "1, name1,contact1/n",
        #     "2, name2,contact2/n",
        # ]

    for student in students:
        # "1,name1,contact1/n"
        
        student = student.strip()
        # "1,name2,contact1"
        if student.startswith(f"{roll_no}"+","):
            # user roll number == first comma separated value
            print("student with this Roll No already exists")
            return
            
    with open("student.txt", "a") as file:
        file.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added Successfully")


def view_student_record():
    with open("student.txt", "r") as student_data:
        students = student_data.readlines()
        for student in students:
            print(student.strip())

def update_student_record():
    roll_no = input("Enter Student Roll No: ")
    is_update = False
    updated_record = []
    # step 1 read student record
    with open("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.split().split(",")
            student_roll = student_record[0]
            if student_roll == roll_no:
                print(f"Student Records: {student_record}")
                name = input("Enter Your Name: ")
                contact_no = input("Enter Your Contact No: ")
                updated_record.append (f"{roll_no}, {name}, {contact_no}\n")
                is_update = True
            else:
                updated_record.append(student)
            if is_update:
                with open("student.txt", "w") as file:
                    file.writelines(updated_record)
                print("student record updated successfully")
            else:
                print("Student record not found")


def delete_student():
    roll_no = input("Enter Student Roll No: ")
    is_deleted = False
    updated_record = []

    # Step 1: Read student records
    with open("student.txt", "r") as file:
        students = file.readlines()
        for student in students:
            student_record = student.strip().split(",")
            student_roll = student_record[0]
            if student_roll == roll_no:
                is_deleted = True
                print(f"Student Records: {student_record}")
                is_deleted = True    
            else:
                updated_record.append(student)
    if is_deleted:
        with open("student.txt", "w") as file:
            file.writelines(updated_record)
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")
