import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name, credit_hours):
        self.course_id = course_id
        self.name = name
        self.credit_hours = credit_hours
        self.marks = {}

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit_hours = float(input("Enter course credit hours: "))
        return Course(course_id, name, credit_hours)

    def input_student_marks(self):
        course_id = input("Enter the course ID to input marks for: ")
        if course_id not in self.courses:
            print("Course not found.")
            return

        for student_id, student in self.students.items():
            mark = float(input(f"Enter marks for {student.name} ({student_id}): "))
            rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            student.marks[course_id] = rounded_mark

    def calculate_student_gpa(self, student):
        total_credit_hours = 0
        total_weighted_points = 0

        for course_id, mark in student.marks.items():
            credit_hours = self.courses[course_id].credit_hours
            total_credit_hours += credit_hours
            total_weighted_points += self.calculate_gpa(mark) * credit_hours

        if total_credit_hours == 0:
            return 0.0
        else:
            return total_weighted_points / total_credit_hours

    def calculate_gpa(self, mark):
        if mark >= 90:
            return 4.0
        elif mark >= 80:
            return 3.0
        elif mark >= 70:
            return 2.0
        elif mark >= 60:
            return 1.0
        else:
            return 0.0

    def list_courses(self):
        print("\nList of Courses:")
        for course_id, course in self.courses.items():
            print(f"{course_id}: {course.name}")

    def list_students(self):
        print("\nList of Students:")
        for student_id, student in self.students.items():
            print(f"{student_id}: {student.name}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to show student marks: ")
        if course_id not in self.courses or not any(student.marks.get(course_id) for student in self.students.values()):
            print("No marks found for this course.")
            return

        print(f"\nStudent Marks for Course {self.courses[course_id].name}:")
        for student_id, student in self.students.items():
            mark = student.marks.get(course_id, "N/A")
            print(f"{student.name} ({student_id}): {mark}")

    def calculate_average_gpa(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]
        gpa_array = np.array([self.calculate_gpa(mark) for mark in student.marks.values()])
        credit_hours_array = np.array([self.courses[course_id].credit_hours for course_id in student.marks.keys()])

        if np.sum(credit_hours_array) == 0:
            return 0.0
        else:
            weighted_gpa = np.sum(gpa_array * credit_hours_array)
            total_credit_hours = np.sum(credit_hours_array)
            return weighted_gpa / total_credit_hours

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students.items(), key=lambda x: self.calculate_student_gpa(x[1]), reverse=True)
        return dict(sorted_students)

    def curses_ui(self):
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Options:")
            stdscr.addstr(1, 0, "1. Input student marks for a course")
            stdscr.addstr(2, 0, "2. List courses")
            stdscr.addstr(3, 0, "3. List students")
            stdscr.addstr(4, 0, "4. Show student marks for a course")
            stdscr.addstr(5, 0, "5. Show average GPA for a student")
            stdscr.addstr(6, 0, "6. Sort students by GPA (Descending)")
            stdscr.addstr(7, 0, "7. Quit")

            choice = stdscr.getch()

            if choice == ord('1'):
                self.input_student_marks()
            elif choice == ord('2'):
                self.list_courses()
            elif choice == ord('3'):
                self.list_students()
            elif choice == ord('4'):
                self.show_student_marks()
            elif choice == ord('5'):
                student_id = input("Enter student ID to show average GPA: ")
                if student_id in self.students:
                    avg_gpa = self.calculate_average_gpa(student_id)
                    print(f"Average GPA for {self.students[student_id].name} ({student_id}): {avg_gpa:.2f}")
                else:
                    print("Student not found.")
            elif choice == ord('6'):
                sorted_students = self.sort_students_by_gpa()
                print("\nSorted Students by GPA (Descending):")
                for student_id, student in sorted_students.items():
                    gpa = self.calculate_student_gpa(student)
                    print(f"{student.name} ({student_id}): {gpa:.2f}")
            elif choice == ord('7'):
                curses.endwin()
                print("Exiting program. Goodbye!")
                break

if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.curses_ui()

