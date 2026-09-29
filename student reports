def show_summary(st):
    print("\n" + "=" * 50)
    print("              STUDENT SUMMARY")
    print("=" * 50)

    if len(st) == 0:
        print("No records available.")
        return

    total = len(st)
    marks = 0

    for s in st:
        marks = marks + s["marks"]

    avg = marks / total

    print("Total Students:", total)
    print("Average Marks:", avg)
