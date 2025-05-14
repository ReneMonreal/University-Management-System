import random
import course
from course import Course_Info
import csv
import students
import faculty
from faculty import Faculty_Info, updateFacultyPyFile
import importlib

#1.) Create a student: Unique ID, Name, Major and list of enrolled courses - students.py - csv contains record
class student:
    def CreateStudent(self, name, major, Enrolling_to_Courses):
        self.ID = UnqiueStuID("students.csv")
        self.Name = name
        self.Major = major
        self.courses = Enrolling_to_Courses
        self.Status = "Active"
        #Comp packet
        new_student = {
            "ID": self.ID,  
            "Student": self.Name,
            "Major": self.Major,
            "EnrolledCourses": self.courses,
            "Status": self.Status
        }

        students.Student_Info.append(new_student)
        students.syncToStudentsCSV()
        students.updateStudentsPyFile()
        print(f"Student {self.Name} added successfully with the ID-{self.ID}")
# A.) Function that creates a unique ID (Ascending Structure)
def UnqiueStuID(filename):
    max_id = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            current_id = row["ID"]
            if current_id.startswith("S"):
                numeric_part = int(current_id[1:]) #Skip the letter & turn nums into int for comparison
                if numeric_part > max_id:
                    max_id = numeric_part
    max_id += 1 #Accending by 1
    return f"S{max_id}"
#B.)print enrolled classe
def PrintClasses(filename, ID):
    EnrolledClasses = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clean_row = {key.strip().strip('"'): value for key, value in row.items()}
            if clean_row["ID"] == ID:
                classes = clean_row["EnrolledCourses"].split(", ")
                EnrolledClasses.extend(classes)
                break
    if EnrolledClasses:
        print(f"Student {ID} is enrolled in the following classes:")
        for course in EnrolledClasses:
            print(f"- {course}")
    else:
        print(f"No enrollment records found for student ID {ID}.")

#2Create Faculty: Unique ID, Name, Department, and list of assigned courses
class Faculty:
    def CreateFaculty(self, name, department, course_Teaching):
        self.ID = self.UnqiueFacID()
        self.Name = name
        self.Department = department
        self.Course_Teaching = course_Teaching
        self.Status = "Active"
        #Packet
        new_Faculty = {
            "ID": self.ID,
            "Faculty": self.Name,
            "Department": self.Department,
            "Course_Teaching": self.Course_Teaching,
            "Status": self.Status
        }

        faculty.Faculty_Info.append(new_Faculty)
        faculty.updateFacultyPyFile()
        print(f"Student {self.Name} added successfully with the ID-{self.ID}")
#A Faculty must have unique ID
    def UnqiueFacID(self):
        max_id = 0
        for fac in faculty.Faculty_Info:
            current_id = fac["ID"]
            if current_id.startswith("F"):
                numeric_part = int(current_id[1:])
                if numeric_part > max_id:
                    max_id = numeric_part
        max_id += 1
        return f"F{max_id}"
#check if department exist
def departmentValidation(department_name):
    for item in Course_Info:
        if item["department"].lower() == department_name.lower():
            return True
    return False

#3 Create Course: Unique ID, Course Name, Assigned Faculty (prof), and enrolled students
class courseClass:
    @staticmethod #For some reason this was the only way i could make this function
    def CreateCourse(course_code, department, students, faculty):
        #Packet
        new_course = {
            "course_code": course_code,
            "department": department,
            "students": students,
            "faculty": faculty
        }

        Course_Info.append(new_course)
        course.updateCoursePyFile()
        print(f"Student {course_code} added successfully with {faculty} as instructor")

#4 Assign Faculty to a course option
def faculty_assigning_to_course(faculty_id, course_code):   
    for faculty in Faculty_Info:
        if faculty["ID"] == faculty_id:
            #Split current course teaching list (str) into a list
            current_courses = faculty["Course_Teaching"].split(", ")
            
            #Check if already in list
            if course_code not in current_courses:
                current_courses.append(course_code)
                #Update, new list of courses (converted to string)
                faculty["Course_Teaching"] = ", ".join(current_courses)
                print(f"Faculty member {faculty['Faculty']} has been assigned to course {course_code}")
                updateFacultyPyFile()

            else:
                print(f"Faculty member {faculty['Faculty']} is already teaching {course_code}")
            return
    print(f"Faculty member with ID {faculty_id} not found")


#5.) Enroll students in a course, enrolled in multiple courses, no duplicate enrollments
#A.)Verify Student ID Exists
def validate_student_ids(input_ids, student_info_list):
    valid_students = []
    student_ids = input_ids.split(',')

    for sid in student_ids:
        sid = sid.strip() 
        if any(student["ID"] == sid for student in student_info_list):
            valid_students.append(sid)
            print(f"Student {sid} found")
        else:
            print(f"Student {sid} not found")

    return valid_students
#B.) Verify course
def courseValidation(course_code):
    for item in Course_Info:
        if course_code == item["course_code"]:
            return True 
    return False  




#*********MAIN
def main_menu():
    while True:
        print("\nWelcome to the University Management System!")
        print("1. Create a student")
        print("2. Create a faculty member")
        print("3. Create a course")
        print("4. Assign faculty to a course")
        print("5. Enroll student in a course")
        print("6. Display reports")
        print("7. Exit")
        try:
            choice = int(input("Please enter your choice (1-7): "))
        except ValueError:
            print("Invalid, Please enter a number between 1 and 7.")
            continue

#1.) Create a student: Unique ID, Name, Major and list of enrolled courses - students.py - csv contains record
        if choice == 1:
            name = input("Enter student name: ")
            major = input("Enter student major: ")
            valid_courses = []

            while True:
                new_courses_input = input("Enter enrolled courses (comma separated): ")
                new_courses = [course.strip() for course in new_courses_input.split(",")]
                #Remove duplicates from the new courses
                new_courses = list(set(new_courses))

                #Verify each course
                for course in new_courses:
                    if courseValidation(course):
                        valid_courses.append(course)
                    else:
                        print(f"Course {course} not found in course list")
                if valid_courses:
                    break
                else:
                    print("No valid courses entered. Please try again.")

            student().CreateStudent(name, major, ", ".join(valid_courses))

#2 Create Faculty: Unique ID, Name, Department, and list of assigned courses
        elif choice == 2:

            name = input("Enter Faculty member's name: ")
            #Verify department exists
            while True:
                department = input("Enter Faculty's Department: ")
                if departmentValidation(department):
                    break
                else:
                    print(f"Department '{department}' not found, Please try again")
            #Removes any non existing courses and keeps existing ones, if l=1 and L not existing then try again
            valid_courses = []
            while True:
                new_courses_input = input("Enter courses the faculty member is teaching (comma-separated, comma-separated): ")
                course_Teaching = [course.strip() for course in new_courses_input.split(",")]

                unique_courses = []
                for course in course_Teaching:
                    if course not in unique_courses:
                        unique_courses.append(course)

                valid_courses.clear()
                for course in unique_courses:
                    if courseValidation(course):
                        valid_courses.append(course)
                    else:
                        print(f"Course {course} not found in course list.")

                if valid_courses:
                    break
                else:
                    print("No valid courses entered. Please try again.")

            Faculty().CreateFaculty(name, department, ", ".join(valid_courses))
            print(f"\nFaculty member {name} has been added successfully.\n")

            updated_departments = faculty.update_department_faculty()  
            faculty.updateListInFile("Departments", updated_departments)  
            faculty.updateListInFile("Faculty_Info", faculty.Faculty_Info)  
            print("Department and Faculty_Info have been updated successfully")

#3 Create Course: Unique ID, Course Name, Assigned Faculty (prof), and enrolled students
        elif choice == 3:
            while True:
                department = input("Enter the department: ").lower()
                # Check if the department exist
                if any(course["department"] == department for course in Course_Info): 
                    print(f"Department '{department}' found !")
                    break
                else:
                    print(f"Department '{department}' not found, Please try again.")
            #Checks if Facutly ID exists
            while True:
                facultyInput = input("Enter Faculty ID: ").strip()
                
                if any(faculty["ID"] == facultyInput for faculty in faculty.Faculty_Info):
                    print("Faculty ID found !")
                    break
                else:
                    print(f"Faculty ID '{facultyInput}' not found, Please try again.")
            while True:
                course_name = input("Enter course name (EX: CSCE): ").strip()
                course_lbl = input("Enter course label/number (EX: 2200.001): ").strip()
                course_code = f"{course_name} {course_lbl}"
                
                # Check if the course exists
                if any(course_code == c["course_code"] for c in Course_Info):
                    print("Course code already exists. Please enter a different course name and label.")
                else:
                    break
            #Keeps valid students, removes invalid students, if s= 1 and s not valid -> try again
            while True:
                student_ids_input = input("Enter student IDs (comma-separated): ")

                valid_students = validate_student_ids(student_ids_input, students.Student_Info)

                if valid_students:
                    print(f"\n Proceeding with students: {', '.join(valid_students)}")
                    break  #exit the loop when at least one valid student is entered
                else:
                    print("\n No valid student IDs entered. Please try again.\n")

# Instantiate the Course class correctly
            courseClass.CreateCourse(course_code, department, valid_students, facultyInput)

            # Check if faculty is already teaching the course
            for f in Faculty_Info:
                if f["ID"] == facultyInput:
                    if course_code in f["Course_Teaching"]:
                        print(f"Faculty member {facultyInput} is already assigned to {course_code}")
                    else:
                        faculty_assigning_to_course(facultyInput, course_code)
                    break  # Exit loop after handling the faculty

            # Create course

#4.) Assign Faculty to a course option
        elif choice == 4:
            while True:
                #Check if faculty memeber exists
                faculty_id = input("Enter the Faculty Member's ID: ")
                faculty_exists = any(faculty_member['ID'] == faculty_id for faculty_member in faculty.Faculty_Info)
                if faculty_exists:
                    print(f" Faculty ID {faculty_id} found.")
                    break
                else:
                    print(" Faculty ID not found. Please try again.")

            while True:
                course_name = input("Enter the Course Code (e.g., 'CYBR 2100.001'): ").strip()
                
                #check if the course exists
                if courseValidation(course_name):
                    print(f" Course {course_name} found.")
                    break
                else:
                    print(" Course not found. Please try again.")

            faculty_assigning_to_course(faculty_id, course_name)
            
#5.) Enroll students in a course, enrolled in multiple courses, no duplicate enrollments
        elif choice == 5:
            while True:
                student_id = input("Enter the student ID to enroll in new course(s): ")
                
                # Check if student ID exists
                if any(str(stu["ID"]) == student_id for stu in students.Student_Info):
                    break
                else:
                    print(f"Student ID {student_id} not found, Please try again.")
            
            valid_courses = []
            while True:
                new_courses_input = input("Enter course(s) to enroll (comma separated): ")
                new_courses = [course.strip() for course in new_courses_input.split(",")]

                #Check each course
                for course in new_courses:
                    if courseValidation(course):
                        valid_courses.append(course)
                    else:
                        print(f"Course {course} not found in course list.")
                if valid_courses:
                    break
                else:
                    print("No valid courses entered. Please try again.")

            students.enrollStudentInCourses(student_id, valid_courses)

#6 Display reports: List all students, List all courses, Display enrolled students in courses
        elif choice == 6:
            #Display all students from students.py
            print("\n--- Student List ---")
            for stu in students.Student_Info:
                print(f"ID: {stu['ID']}, Name: {stu['Student']}, Major: {stu['Major']}, Status: {stu['Status']}")

            #Display students in courses
            print("\n--- Enrolled Students in Courses ---")
            for c in Course_Info:
                course_code = c.get('course_code', 'Unknown Course Code')
                enrolled_students = c.get('students', [])
                if enrolled_students:
                    print(f"Course {course_code}: Enrolled Students: {', '.join(enrolled_students)}")
                else:
                    print(f"Course {course_code}: No students enrolled.")

            #Display faculty info from faculty.py
            print("\n--- Faculty List ---")
            for fac in faculty.Faculty_Info:
                print(f"ID: {fac['ID']}, Name: {fac['Faculty']}, Department: {fac['Department']}")

            #Display unique departments from faculty.py
            print("\n--- Departments ---")
            departments = {fac['Department'] for fac in faculty.Faculty_Info}
            for dept in departments:
                print(dept)

            #Display course list
            print("\n--- Course List ---")
            for c in Course_Info:
                course_code = c.get('course_code', 'Unknown Code')
                department = c.get('department', 'Unknown Department')
                faculty_list = ''.join(c.get('faculty', []))
                students_list = ', '.join(c.get('students', []))
                print(f"Course Code: {course_code}, Department: {department}, Faculty: {faculty_list}, Enrolled Students: {students_list}")
        elif choice == 7:
            print("Goodbye - Rene M!")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main_menu()
