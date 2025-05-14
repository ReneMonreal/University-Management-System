🎓 Final Project: University Management System

📝 Overview:
In this project, i built a basic University Management System in Python. The system will allows to create and manage students, faculty, and courses. Implement functionality to assign faculty to courses and enroll students in those courses. Student data is also saved and updated in a CSV file.


PROJECT REQUIRNMENTS:
Must've used the following concepts in the implementation:
  1.) Object-Oriented Programming (OOP): Classes and objects
  2.) Functions: To organize and reuse logic
  3.) Modules: To separate and structure your code
  4.) CSV File Handling: To store and update student records persistently


Features to Implement:
  1.) Create a Student
      Each student should have a unique ID, name, major, and a list of enrolled courses.
      Save student information in students.csv.
    When a new student is added, append or update their record in the CSV file.
  2.) Create a Faculty
    Each faculty should have an ID, name, department, and a list of assigned courses.
  3.) Create a Course
    Each course should have a unique course ID, course name, assigned faculty (instructor), and a list of enrolled students.
  4.) Assign Faculty to a Course
    You should be able to assign a faculty member to a specific course.
  5.) Enroll Students in a Course
    Students can be enrolled in multiple courses.
    Ensure no duplicate enrollments occur.
  6.) Display Reports
    List all students  
    List all courses with their assigned faculty
    Display enrolled students for a specific course

SCHOOL SUGGESTED FILE STRUCTURE:
  main.py: Main program where user interaction and logic flow are handled
  student.py: Contains the Student class
  faculty.py: Contains the Faculty class
  course.py: Contains the Course class
  utils.py: Helper functions such as saving to and reading from CSV (I Did not use this)
  students.csv: Stores all student information


PROJECT GRADING RUBRIC:
Category	Points
  1.) Student, Faculty, and Course classes are correctly created	25 points
  2.) Students can be enrolled in courses	15 points
  3.) Faculty can be assigned to courses	15 points
  4.) Data is saved and updated in a CSV file	15 points
  5.) Code is organized using functions and separate files (modules)	10 points
  6.) Project runs without major errors	10 points
  7.) Student/group is present and demonstrates the project in class	10 points


**FINAL GRADE**
<img width="1318" alt="image" src="https://github.com/user-attachments/assets/a1b1e295-09aa-40a8-8e30-070b10e17b08" />
