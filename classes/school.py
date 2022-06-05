from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
    
    def list_students(self):
        for students in self.students:
            print(students.name, students.school_id)

    def find_student_by_id(self, student_id):
        for students in self.students:
            if students.school_id == student_id:
                return students
            

