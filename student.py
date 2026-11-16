from datetime import datetime

class Student:
    def __init__(self, student_id, full_name, student_class, gender, dob, scores=None):
        self.student_id = student_id
        self.full_name = full_name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        # scores is a dictionary like {"Mathematics": 85, "English Language": 78, ...}
        self.scores = scores if scores is not None else {}
        self.total_score = 0.0
        self.average_score = 0.0
        self.grade = "F"
        self.date_recorded = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.scores:
            self.calculate_results()

    def calculate_results(self):
        if self.scores:
            scores_list = list(self.scores.values())
            self.total_score = sum(scores_list)
            self.average_score = self.total_score / len(scores_list)
            self.grade = self.assign_grade(self.average_score)
        else:
            self.total_score = 0.0
            self.average_score = 0.0
            self.grade = "F"

    @staticmethod
    def assign_grade(avg):
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 45:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "student_class": self.student_class,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "total_score": self.total_score,
            "average_score": self.average_score,
            "grade": self.grade,
            "date_recorded": self.date_recorded
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            student_id=data.get("student_id"),
            full_name=data.get("full_name"),
            student_class=data.get("student_class"),
            gender=data.get("gender"),
            dob=data.get("dob"),
            scores=data.get("scores", {})
        )
        student.total_score = data.get("total_score", 0.0)
        student.average_score = data.get("average_score", 0.0)
        student.grade = data.get("grade", "F")
        student.date_recorded = data.get("date_recorded", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return student