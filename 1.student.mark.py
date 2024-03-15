def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

def input_student_marks(courses, students):
    course_id = input("Enter the course ID to input marks for: ")
    if course_id not in courses:
        print("Course not found.")
        return

    marks = {}
    for student_id in students:
        mark = float(input(f"Enter marks for {students[student_id]['name']} ({student_id}): "))
        marks[student_id] = mark

    courses[course_id]['marks'] = marks

def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course in courses.items():
        print(f"{course_id}: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for student_id, student in students.items():
        print(f"{student_id}: {student['name']}")

def show_student_marks(courses, students):
    course_id = input("Enter the course ID to show student marks: ")
    if course_id not in courses or 'marks' not in courses[course_id]:
        print("No marks found for this course.")
        return

    print(f"\nStudent Marks for Course {courses[course_id]['name']}:")
    for student_id, mark in courses[course_id]['marks'].items():
        print(f"{students[student_id]['name']} ({student_id}): {mark}")

def main():
    students = {}
    courses = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student_info = input_student_information()
        students[student_info['id']] = student_info

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_information()
        courses[course_info['id']] = course_info

    while True:
        print("\nOptions:")
        print("1. Input student marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == 1:
            input_student_marks(courses, students)
        elif choice == 2:
            list_courses(courses)
        elif choice == 3:
            list_students(students)
        elif choice == 4:
            show_student_marks(courses, students)
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
