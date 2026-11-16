from student import Student
from storage import load_data, save_data
from results import record_or_update_scores, display_report_card
from reports import list_all_students, show_class_statistics, generate_text_report

def add_student(students_dict):
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID (e.g., ST101): ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students_dict:
        print("A student with this ID already exists.")
        return
    
    full_name = input("Enter Full Name: ").strip()
    student_class = input("Enter Class/Form (e.g., SS1): ").strip()
    gender = input("Enter Gender (Male/Female/Other): ").strip()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()

    new_student = Student(student_id, full_name, student_class, gender, dob)
    students_dict[student_id] = new_student
    save_data(students_dict)
    print(f"Student {full_name} added successfully!")

def view_all_students(students_dict):
    if not students_dict:
        print("No student records found.")
        return
    print("\n--- Registered Students ---")
    print(f"{'ID':<10} | {'Full Name':<22} | {'Class':<12} | {'Gender':<10} | {'DOB':<12}")
    print("-" * 75)
    for s in students_dict.values():
        print(f"{s.student_id:<10} | {s.full_name:<22} | {s.student_class:<12} | {s.gender:<10} | {s.dob:<12}")
    print("-" * 75)

def search_student(students_dict):
    if not students_dict:
        print("No student records found.")
        return
    query = input("Enter Student ID or Full Name to search: ").strip().lower()
    found = False
    print("\n--- Search Results ---")
    for s in students_dict.values():
        if query in s.student_id.lower() or query in s.full_name.lower():
            print(f"ID: {s.student_id} | Name: {s.full_name} | Class: {s.student_class} | Gender: {s.gender} | DOB: {s.dob} | Average: {s.average_score:.2f} | Grade: {s.grade}")
            found = True
    if not found:
        print("No matching student found.")

def update_student(students_dict):
    student_id = input("Enter Student ID to update: ").strip()
    if student_id not in students_dict:
        print("Student ID not found.")
        return
    
    s = students_dict[student_id]
    print(f"Updating details for {s.full_name}. Press Enter to keep existing value.")
    
    new_name = input(f"Enter Full Name [{s.full_name}]: ").strip()
    if new_name:
        s.full_name = new_name
        
    new_class = input(f"Enter Class [{s.student_class}]: ").strip()
    if new_class:
        s.student_class = new_class
        
    new_gender = input(f"Enter Gender [{s.gender}]: ").strip()
    if new_gender:
        s.gender = new_gender
        
    new_dob = input(f"Enter DOB [{s.dob}]: ").strip()
    if new_dob:
        s.dob = new_dob

    save_data(students_dict)
    print("Student information updated successfully!")

def delete_student(students_dict):
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id not in students_dict:
        print("Student ID not found.")
        return
    
    confirm = input(f"Are you sure you want to delete student {students_dict[student_id].full_name}? (y/n): ").strip().lower()
    if confirm == 'y':
        del students_dict[student_id]
        save_data(students_dict)
        print("Student record deleted successfully!")
    else:
        print("Deletion cancelled.")

def main():
    students_dict = load_data()
    print("Welcome to the Student Result Management System")
    
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Add New Student")
        print("2. View All Registered Students")
        print("3. Search Student (by ID or Name)")
        print("4. Update Student Information")
        print("5. Delete Student Record")
        print("6. Record / Update Student Scores")
        print("7. Display Student Report Card")
        print("8. List Students (Sorted by Name)")
        print("9. List Students (Sorted by Average Score)")
        print("10. Show Class Performance Statistics")
        print("11. Generate Text Report to File")
        print("12. Save & Exit")
        print("===========================================")
        
        choice = input("Enter your choice (1-12): ").strip()
        
        if choice == '1':
            add_student(students_dict)
        elif choice == '2':
            view_all_students(students_dict)
        elif choice == '3':
            search_student(students_dict)
        elif choice == '4':
            update_student(students_dict)
        elif choice == '5':
            delete_student(students_dict)
        elif choice == '6':
            record_or_update_scores(students_dict)
            save_data(students_dict)
        elif choice == '7':
            display_report_card(students_dict)
        elif choice == '8':
            list_all_students(students_dict, sort_by="name")
        elif choice == '9':
            list_all_students(students_dict, sort_by="average")
        elif choice == '10':
            show_class_statistics(students_dict)
        elif choice == '11':
            generate_text_report(students_dict)
        elif choice == '12':
            save_data(students_dict)
            print("Data saved successfully. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()