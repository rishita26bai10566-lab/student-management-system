def get_student_details():
    sid = input("\nEnter student ID: ")
    nm = input("Enter student name: ")
    cr = input("Enter course: ")
    age = input("Enter age: ")
    mk = input("Enter marks: ")

    if sid == "" or nm == "" or cr == "" or age == "" or mk == "":
        return None

    if not age.isdigit() or not mk.isdigit():
        return None

    st = {
        "id": sid,
        "name": nm,
        "course": cr,
        "age": int(age),
        "marks": int(mk)}

    return st
