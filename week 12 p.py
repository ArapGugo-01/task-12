class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []   # Association

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"Courses registered by {self.name}:")
        for course in self.courses:
            print(f"- {course.course_name}")


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name


class RegistrationSystem:
    # Dependency: uses Student and Course
    def register_student(self, student, course):
        student.add_course(course)
        print(f"{student.name} registered for {course.course_name}")


# Main program
s1 = Student(101, "Alice")
s2 = Student(102, "Bob")

c1 = Course("ENG101", "Engineering Mathematics")
c2 = Course("CSE102", "Programming in Python")

system = RegistrationSystem()

system.register_student(s1, c1)
system.register_student(s1, c2)
system.register_student(s2, c1)

print()
s1.display_courses()
print()
s2.display_courses()