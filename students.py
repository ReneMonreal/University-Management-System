import csv

Student_Info = [
    {'ID': 'S100100100', 'Student': 'Rene Monreal', 'Major': 'Cybersecurity', 'EnrolledCourses': 'Calculus 1020.001, CSCE 1035.001, CJUS 2700.001, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100101', 'Student': 'Lionel Messi', 'Major': 'Computer Science', 'EnrolledCourses': 'CSCE 1035.001, CSCE 1040.002, MATH 1710.001, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100102', 'Student': 'Cristiano Ronaldo', 'Major': 'Cybersecurity', 'EnrolledCourses': 'CYBR 2100.001, CYBR 3100.002, CSCE 1035.001, PHYS 2220.002, MATH 1720.002', 'Status': 'Actve'},
    {'ID': 'S100100103', 'Student': 'LeBron James', 'Major': 'IT Management', 'EnrolledCourses': 'ITMT 1500.001, ITMT 2500.002, CSCE 1035.001, MATH 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100104', 'Student': 'Serena Williams', 'Major': 'Electrical Engineering', 'EnrolledCourses': 'EENG 1910.001, EENG 2610.002, PHYS 1710.001, MATH 1720.002, PHYS 2220.002', 'Status': 'Actve'},
    {'ID': 'S100100105', 'Student': 'Tom Brady', 'Major': 'Mechanical Engineering', 'EnrolledCourses': 'MEEN 2210.001, MEEN 2301.002, PHYS 1710.001, MATH 1720.002', 'Status': 'Inactive'},
    {'ID': 'S100100107', 'Student': 'Usain Bolt', 'Major': 'Cybersecurity', 'EnrolledCourses': 'CYBR 2100.001, CYBR 3100.002, CSCE 1035.001, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100108', 'Student': 'Michael Jordan', 'Major': 'Computer Science', 'EnrolledCourses': 'CSCE 1035.001, CSCE 1040.002, CSCE 2100.003, MATH 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100109', 'Student': 'Steph Curry', 'Major': 'Mathematics', 'EnrolledCourses': 'MATH 1710.001, MATH 1720.002, MATH 2730.003, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100112', 'Student': 'Kylian Mbappé', 'Major': 'Electrical Engineering', 'EnrolledCourses': 'EENG 1910.001, EENG 2610.002, PHYS 1710.001, MATH 1720.002', 'Status': ''},
    {'ID': 'S100100113', 'Student': 'Lewis Hamilton', 'Major': 'IT Management', 'EnrolledCourses': 'ITMT 1500.001, ITMT 2500.002, ITMT 3500.003, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100114', 'Student': 'Checo Perez', 'Major': 'Cybersecurity', 'EnrolledCourses': 'CYBR 2100.001, CYBR 3100.002, CYBR 3200.003, CSCE 1035.001', 'Status': 'Actve'},
    {'ID': 'S100100116', 'Student': 'Carlos Sainz', 'Major': 'Computer Science', 'EnrolledCourses': 'CSCE 1035.001, CSCE 1040.002, CSCE 2100.003, PHYS 1710.001', 'Status': 'Actve'},
    {'ID': 'S100100117', 'Student': "Shaquille O'Neal", 'Major': 'Mechanical Engineering', 'EnrolledCourses': 'MEEN 2210.001, MEEN 2301.002, MEEN 3240.003, MATH 1720.002', 'Status': 'Actve'},
    {'ID': 'S100100119', 'Student': 'Neymar Jr.', 'Major': 'Cybersecurity', 'EnrolledCourses': 'CYBR 2100.001, CYBR 3100.002, CYBR 3200.003, MATH 1710.001', 'Status': 'Inactive'},
    {'ID': 'S100100120', 'Student': 'Dwyane Wade', 'Major': 'IT Management', 'EnrolledCourses': 'ITMT 1500.001, ITMT 2500.002, ITMT 3500.003, ITMT 4500.004', 'Status': 'Actve'},
    {'ID': 'S100100121', 'Student': 'Created 1', 'Major': 'hdshjd', 'EnrolledCourses': 'CYBR 3100.002, ITMT 1500.001', 'Status': 'Active'},
    {'ID': 'S100100122', 'Student': 'CREATED 2', 'Major': 'MAJOR', 'EnrolledCourses': 'EENG 2610.002', 'Status': 'Active'},
    {'ID': 'S100100123', 'Student': 'CREATED 3', 'Major': 'MAJOR', 'EnrolledCourses': 'MEEN 2301.002, EENG 2610.002', 'Status': 'Active'},
    {'ID': 'S100100124', 'Student': 'BUBBBBAAA', 'Major': 'MAjro', 'EnrolledCourses': 'CYBR 2100.001', 'Status': 'Active'},
    {'ID': 'S100100125', 'Student': 'CHECK IRT OUT', 'Major': 'ssssss', 'EnrolledCourses': 'PHYS 3020.004', 'Status': 'Active'},
    {'ID': 'S100100126', 'Student': 'FAMOUS ', 'Major': 'SCHOOL', 'EnrolledCourses': 'CYBR 2100.001, ITMT 1500.001', 'Status': 'Active'},
]

#Sync changes over to csv file
def syncToStudentsCSV():
    filename = "students.csv"
    Columns = ["ID", "Student", "Major", "EnrolledCourses", "Status"]
    with open(filename, mode="w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=Columns)
        writer.writeheader()
        for student in Student_Info:
            writer.writerow(student)
    print(f"{filename} updated...")
#Update list
def updateStudentsPyFile():
    filename = "students.py"
    with open(filename, "r") as file:
        lines = file.readlines()
    start_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Student_Info = ["):
            start_index = i
            break

    # Build new Student_Info text
    student_info_text = "Student_Info = [\n"
    for student in Student_Info:
        student_info_text += f"    {student},\n"
    student_info_text += "]\n"
    end_index = start_index
    while end_index < len(lines) and "]" not in lines[end_index]:
        end_index += 1
    end_index += 1 

    # Replace old list with new list
    new_lines = lines[:start_index] + [student_info_text] + lines[end_index:]
    with open(filename, "w") as file:
        file.writelines(new_lines)

    print(f"students.py successfully updated with latest Student_Info.")

def enrollStudentInCourses(student_id, courses_to_add):
    found = False
    for stu in Student_Info:
        if str(stu["ID"]) == str(student_id):
            enrolled_courses = stu["EnrolledCourses"].split(", ") if stu["EnrolledCourses"] else []
            for course in courses_to_add:
                if course not in enrolled_courses:
                    enrolled_courses.append(course)
            stu["EnrolledCourses"] = ", ".join(enrolled_courses)
            found = True
            break
    if found:
        syncToStudentsCSV()
        updateStudentsPyFile()
        print(f"Updated enrolled courses for student ID {student_id}.")
    else:
        print("Student ID not found.")

#manual
if __name__ == "__main__":
    syncToStudentsCSV()