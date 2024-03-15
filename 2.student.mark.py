class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
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
        return Course(course_id, name)

    def input_student_marks(self):
        course_id = input("Enter the course ID to input marks for: ")
        if course_id not in self.courses:
            print("Course not found.")
            return

        for student_id, student in self.students.items():
            mark = float(input(f"Enter marks for {student.name} ({student_id}): "))
            student.marks[course_id] = mark

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

    def main(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            student = self.input_student_information()
            self.students[student.student_id] = student

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            course = self.input_course_information()
            self.courses[course.course_id] = course

        while True:
            print("\nOptions:")
            print("1. Input student marks for a course")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.input_student_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.main()
