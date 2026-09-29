from student_data import add_student, view_students, find_student, delete_student
from student_display import show_students, show_student
from student_utils import get_student_details

while True:
    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    ch = input("\nEnter your choice: ")

    if ch == "1":

        st = get_student_details()

        if st is None:
            print("\nPlease enter all details correctly.")

        else:
            add_student(st)
            print("\nStudent added successfully.")

    elif ch == "2":

        st = view_students()
        show_students(st)

    elif ch == "3":

        sid = input("\nEnter student ID: ")
        st = find_student(sid)

        if st is None:
            print("\nStudent not found.")

        else:
            show_student(st)

    elif ch == "4":

        sid = input("\nEnter student ID: ")

        if delete_student(sid):
            print("\nStudent deleted successfully.")

        else:
            print("\nStudent not found.")

    elif ch == "5":

        print("\nThank you for using the system!")
        break

    else:

        print("\nInvalid choice. Please enter 1 to 5.")
