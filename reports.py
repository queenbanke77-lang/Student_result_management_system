import os
from datetime import datetime

def list_all_students(students_dict, sort_by="name"):
    if not students_dict:
        print("No student records found.")
        return

    students_list = list(students_dict.values())
    
    if sort_by == "average":
        students_list.sort(key=lambda x: x.average_score, reverse=True)
        print("\n--- Students Sorted by Average Score (Highest to Lowest) ---")
    else:
        students_list.sort(key=lambda x: x.full_name)
        print("\n--- Students Sorted Alphabetically by Name ---")

    print("-" * 85)
    print(f"{'ID':<10} | {'Full Name':<22} | {'Class':<12} | {'Total':<8} | {'Average':<8} | {'Grade':<6}")
    print("-" * 85)
    for s in students_list:
        print(f"{s.student_id:<10} | {s.full_name:<22} | {s.student_class:<12} | {s.total_score:<8.2f} | {s.average_score:<8.2f} | {s.grade:<6}")
    print("-" * 85)

def show_class_statistics(students_dict):
    if not students_dict:
        print("No student records available for statistics.")
        return

    students = list(students_dict.values())
    averages = [s.average_score for s in students]

    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(averages)

    highest_student = max(students, key=lambda x: x.average_score)
    lowest_student = min(students, key=lambda x: x.average_score)

    print("\n" + "="*40)
    print(f"{'CLASS PERFORMANCE STATISTICS':^40}")
    print("="*40)
    print(f"Total Students Registered : {len(students)}")
    print(f"Class Average Score       : {class_avg:.2f}")
    print(f"Highest Average Score     : {highest_avg:.2f} ({highest_student.full_name} - {highest_student.student_id})")
    print(f"Lowest Average Score      : {lowest_avg:.2f} ({lowest_student.full_name} - {lowest_student.student_id})")
    print("="*40)

def generate_text_report(students_dict):
    if not students_dict:
        print("No records to generate report.")
        return

    report_filename = "data/class_performance_report.txt"
    try:
        os.makedirs("data", exist_ok=True)
        with open(report_filename, "w") as f:
            f.write("="*65 + "\n")
            f.write(f"{'OFFICIAL CLASS PERFORMANCE REPORT':^65}\n")
            f.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*65 + "\n\n")
            
            f.write(f"{'ID':<10} | {'Full Name':<22} | {'Class':<10} | {'Average':<8} | {'Grade':<6}\n")
            f.write("-" * 65 + "\n")
            for s in students_dict.values():
                f.write(f"{s.student_id:<10} | {s.full_name:<22} | {s.student_class:<10} | {s.average_score:<8.2f} | {s.grade:<6}\n")
            f.write("-" * 65 + "\n")
        print(f"Report successfully generated and saved to '{report_filename}'!")
    except Exception as e:
        print(f"Failed to generate text report: {e}")