students_list=[]

while True:
    print("\n----Student Management System----\n")
    print("1.add a student")
    print("2.view a student")
    print("3.search a student")
    print("4.delete a student")
    print("5.exit")
     
    choice=input("enter your choice(1-5):")

    if choice == "1":
        name=input("enter name:")
        roll=input("enter roll:")
        course=input("enter course:")

        student_data={
            "name":name,
            "roll":roll,
            "course":course
        }

        students_list.append(student_data)
        print("Student added successfully")
        print(students_list)

    elif choice == "2":
        print(f"total students_list={students_list}")  

    elif choice == "3":
        search_roll=input("enter roll no to search roll")

        found=False

        for student in students_list:
            if student["roll"]==search_roll:
                print("Student Found")
                print(student)
                found=True
                break

        if found == False:
            print("Student not found")  

    elif choice == "4":
        del_roll=input("Enter roll no to delete:")
        found=False
        for student in students_list:
            if student["roll"]==del_roll:
                students_list.remove(student)
                print("Student deleted successfully")
                found=True
                break

        if found == False:
            print("Student not found")

    elif choice == "5":
            print("exiting the program...")
            break
    else:
            print("Invalid choice")
                          

   
