# -----------------------------------------
# Existing student data (example starter)
# -----------------------------------------
students = [
    {
        "cps_id": "123456",
        "name": "Lopez, Maria",
        "middle_name": "Isabel",
        "homeroom": "301",
        "grade": 7,
        "primary_email": "mlopez@cps.edu",
        "secondary_email": "mlopez2@cps.edu"
    },
    {
        "cps_id": "789012",
        "name": "Johnson, Malik",
        "middle_name": "Andre",
        "homeroom": "204",
        "grade": 8,
        "primary_email": "mjohnson@cps.edu",
        "secondary_email": "mjohnson2@cps.edu"
    }
]


# -----------------------------------------
# SEARCH FUNCTION
# -----------------------------------------
def search_student(full_name):
    for student in students:
        if student["name"].lower() == full_name.lower():
            return student
    return None


# -----------------------------------------
# ADD NEW STUDENT FUNCTION
# -----------------------------------------
def add_student():
    print("\n--- Add a New Student ---")

    cps_id = input("CPS ID: ")

    for student in students:
        if student["cps_id"] == cps_id:
            print("Error: A student with this CPS ID already exists.")
            return

    first = input("First Name: ")
    last = input("Last Name: ")
    middle = input("Middle Name: ")
    homeroom = input("Homeroom: ")
    grade = int(input("Grade Level: "))
    primary = input("Primary Email: ")
    secondary = input("Secondary Email: ")

    full_name = f"{last}, {first}"

    new_student = {
        "cps_id": cps_id,
        "name": full_name,
        "middle_name": middle,
        "homeroom": homeroom,
        "grade": grade,
        "primary_email": primary,
        "secondary_email": secondary
    }

    students.append(new_student)

    print("\nStudent added successfully.")
    print(new_student)


# -----------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------
while True:
    print("\n===== STUDENT LOOKUP TOOL =====")
    print("1. Search for a student")
    print("2. Add a new student")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("\nEnter the student's full name (Last, First): ")
        result = search_student(name)

        if result:
            print("\nStudent found:")
            print(result)
        else:
            print("\nStudent not found.")

    elif choice == "2":
        add_student()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
    