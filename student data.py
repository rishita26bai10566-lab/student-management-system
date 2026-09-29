import json

FN = "students.json"

def view_students():
    try:
        fl = open(FN, "r")
        st = json.load(fl)
        fl.close()
        return st
    except FileNotFoundError:
        return []

def add_student(st):
    dt = view_students()
    dt.append(st)

    fl = open(FN, "w")
    json.dump(dt, fl, indent=4)
    fl.close()

def find_student(sid):
    dt = view_students()

    for st in dt:
        if st["id"] == sid:
            return st

    return None

def delete_student(sid):
    dt = view_students()
    new_dt = []
    found = False

    for st in dt:
        if st["id"] == sid:
            found = True
        else:
            new_dt.append(st)

    fl = open(FN, "w")
    json.dump(new_dt, fl, indent=4)
    fl.close()

    return found
