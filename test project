from student_data import add_student, find_student, delete_student

sid = "T001"

add_student({
    "id": sid,
    "name": "Test Student",
    "course": "CSE",
    "age": 18,
    "marks": 80
})

r1 = find_student(sid)

print("Test 1: Student added and found")
assert r1 is not None
assert r1["name"] == "Test Student"

r2 = delete_student(sid)

print("Test 2: Student deleted")
assert r2 is True

r3 = find_student(sid)

print("Test 3: Deleted student not found")
assert r3 is None

print("\nAll tests passed successfully.")
