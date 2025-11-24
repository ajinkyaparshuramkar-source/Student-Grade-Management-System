# ==========================================
# STUDENT GRADE MANAGEMENT SYSTEM
# ==========================================

import os # Used to check if file exists

# Name of the file where data is stored
FILENAME = "students.txt"

# ==========================================
# MODULE 1: VALIDATORS
# (If splitting: Save this part as 'validators.py')
# ==========================================

def validate_marks(marks):
    """Checks if marks are numeric and between 0-100."""
    try:
        marks = float(marks)
        if 0 <= marks <= 100:
            return True
        else:
            print(">>> Error: Marks must be between 0 and 100.")
            return False
    except ValueError:
        print(">>> Error: Please enter a number, not text.")
        return False

def validate_name(name):
    """Checks if the name is not empty."""
    if len(name.strip()) > 0:
        return True
    else:
        print(">>> Error: Name cannot be empty.")
        return False

# ==========================================
# MODULE 2: DATA STORAGE
# (If splitting: Save this part as 'data_storage.py')
# ==========================================

def save_student(name, marks):
    """Appends a new student to the file."""
    try:
        # 'a' mode opens the file to Append data at the end
        f = open(FILENAME, "a")
        # We save it as "Name,Marks"
        f.write(f"{name},{marks}\n")
        f.close()
    except Exception as e:
        print(f"Error saving data: {e}")

def load_students():
    """Reads all students from the file into a list."""
    student_list = []
    
    # Check if file exists first to avoid errors
    if not os.path.exists(FILENAME):
        return []

    try:
        f = open(FILENAME, "r")
        lines = f.readlines()
        for line in lines:
            # Clean up the line and split by comma
            data = line.strip().split(",")
            if len(data) == 2: # Ensure line has both name and marks
                student = {"name": data[0], "marks": float(data[1])}
                student_list.append(student)
        f.close()
    except Exception as e:
        print(f"Error loading data: {e}")
        
    return student_list

# ==========================================
# MODULE 3: ANALYTICS
# (If splitting: Save this part as 'analytics.py')
# ==========================================

def show_class_average(students):
    """Calculates the average marks of the class."""
    if not students:
        print(">>> No records found to calculate average.")
        return

    total_marks = 0
    count = 0
    
    for s in students:
        total_marks = total_marks + s["marks"]
        count = count + 1
    
    average = total_marks / count
    print("\n------------------------------")
    print(f"CLASS AVERAGE: {average:.2f}")
    print("------------------------------")

def show_topper(students):
    """Finds the student with the highest marks."""
    if not students:
        print(">>> No records found.")
        return

    # Assume the first student is the topper initially
    top_student = students[0]
    
    # Compare with everyone else
    for s in students:
        if s["marks"] > top_student["marks"]:
            top_student = s
            
    print("\n------------------------------")
    print(f"CLASS TOPPER: {top_student['name']} ({top_student['marks']} Marks)")
    print("------------------------------")

# ==========================================
# MODULE 4: OPERATIONS
# (If splitting: Save this part as 'operations.py')
# ==========================================

def add_new_student():
    print("\n--- ADD NEW STUDENT ---")
    name = input("Enter Student Name: ")
    
    # Using the validator function defined above
    if validate_name(name):
        marks = input("Enter Marks (0-100): ")
        
        if validate_marks(marks):
            save_student(name, marks)
            print(">>> Success: Student added successfully!")

def view_all_students():
    print("\n--- ALL STUDENTS ---")
    students = load_students()
    
    if len(students) == 0:
        print(">>> No data found.")
    else:
        print(f"{'Name':<20} {'Marks':<10}") # Formatting for neatness
        print("-" * 30)
        for s in students:
            print(f"{s['name']:<20} {s['marks']:<10}")
    
    return students

# ==========================================
# MODULE 5: MAIN (Entry Point)
# (If splitting: Save this part as 'main.py')
# ==========================================

def main_menu():
    while True:
        print("\n=================================")
        print(" STUDENT GRADE MANAGEMENT SYSTEM ")
        print("=================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Check Class Average")
        print("4. Find Topper")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_new_student()
        
        elif choice == '2':
            view_all_students()
            
        elif choice == '3':
            students = load_students()
            show_class_average(students)
            
        elif choice == '4':
            students = load_students()
            show_topper(students)
            
        elif choice == '5':
            print("Exiting... Thank you!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# This line starts the program
if __name__ == "__main__":
    main_menu()
