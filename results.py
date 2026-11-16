from student import Student

def input_scores():
    """Prompt user to enter scores for at least five subjects."""
    subjects = ["Mathematics", "English Language", "Basic Science", "Social Studies", "Computer Studies"]
    scores = {}
    print("\n--- Enter Subject Scores (0 - 100) ---")
    for subj in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subj}: "))
                if 0 <= score <= 100:
                    scores[subj] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
    return scores

def record_or_update_scores(students_dict):
    student_id = input("Enter Student ID to record/update scores: ").strip()
    if student_id not in students_dict:
        print("Student ID not found.")
        return
    
    student = students_dict[student_id]
    print(f"Recording scores for: {student.full_name} (ID: {student.student_id})")
    new_scores = input_scores()
    student.scores = new_scores
    student.calculate_results()
    print("Scores recorded and results updated successfully!")

def display_report_card(students_dict):
    student_id = input("Enter Student ID to view report card: ").strip()
    if student_id not in students_dict:
        print("Student ID not found.")
        return
    
    s = students_dict[student_id]
    print("\n" + "="*45)
    print(f"{'STUDENT REPORT CARD':^45}")
    print("="*45)
    print(f"Student ID   : {s.student_id}")
    print(f"Full Name    : {s.full_name}")
    print(f"Class        : {s.student_class}")
    print(f"Gender       : {s.gender}")
    print(f"Date of Birth: {s.dob}")
    print(f"Date Recorded: {s.date_recorded}")
    print("-"*45)
    print(f"{'Subject':<25} | {'Score':<10}")
    print("-"*45)
    if s.scores:
        for subj, score in s.scores.items():
            print(f"{subj:<25} | {score:<10.2f}")
    else:
        print("No scores recorded yet.")
    print("-"*45)
    print(f"Total Score  : {s.total_score:.2f}")
    print(f"Average Score: {s.average_score:.2f}")
    print(f"Overall Grade: {s.grade}")
    print("="*45)