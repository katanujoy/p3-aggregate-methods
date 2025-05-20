# lib/enrollment.py
from datetime import datetime

class Student:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}
        Student.all.append(self)

    def enroll(self, course, date, grade=None):
        enrollment = Enrollment(self, course, date)
        self._enrollments.append(enrollment)
        if grade is not None:
            self._grades[enrollment] = grade
        return enrollment

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total = sum(self._grades.values())
        return total / len(self._grades)


class Course:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []
        Course.all.append(self)

    def enroll(self, student, date):
        enrollment = Enrollment(student, self, date)
        self._enrollments.append(enrollment)
        student._enrollments.append(enrollment)
        return enrollment

    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []

    def __init__(self, student, course, date):
        self.student = student
        self.course = course
        self._date = date
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        result = {}
        for e in cls.all:
            date = e.get_enrollment_date().date()
            result[date] = result.get(date, 0) + 1
        return result
