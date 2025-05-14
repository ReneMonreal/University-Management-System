Course_Info = [
    {'course_code': 'CSCE 1035.001', 'department': 'computer_science', 'students': ['S100100101', 'S100100108', 'S100100113', 'S100100116'], 'faculty': ['F100100101', 'F100100108']},
    {'course_code': 'CSCE 1040.002', 'department': 'computer_science', 'students': ['S100100101'], 'faculty': ['F100100108']},
    {'course_code': 'CSCE 2100.003', 'department': 'computer_science', 'students': ['S100100108'], 'faculty': ['F100100101']},
    {'course_code': 'CSCE 2110.004', 'department': 'computer_science', 'students': [], 'faculty': ['F100100101']},
    {'course_code': 'CSCE 2610.005', 'department': 'computer_science', 'students': ['S100100108'], 'faculty': ['F100100108']},
    {'course_code': 'MATH 1710.001', 'department': 'math', 'students': ['S100100109', 'S100100101', 'S100100103'], 'faculty': ['F100100110']},
    {'course_code': 'MATH 1720.002', 'department': 'math', 'students': ['S100100109'], 'faculty': ['F100100110']},
    {'course_code': 'MATH 2730.003', 'department': 'math', 'students': ['S100100109'], 'faculty': ['F100100111']},
    {'course_code': 'MATH 3680.004', 'department': 'math', 'students': [], 'faculty': ['F100100111']},
    {'course_code': 'CYBR 2100.001', 'department': 'cybersecurity', 'students': ['S100100100', 'S100100107'], 'faculty': ['F100100100']},
    {'course_code': 'CYBR 3100.002', 'department': 'cybersecurity', 'students': ['S100100102', 'S100100107'], 'faculty': ['F100100102']},
    {'course_code': 'CYBR 3200.003', 'department': 'cybersecurity', 'students': ['S100100114'], 'faculty': ['F100100107']},
    {'course_code': 'CYBR 4100.004', 'department': 'cybersecurity', 'students': [], 'faculty': ['F100100102']},
    {'course_code': 'ITMT 1500.001', 'department': 'it_management', 'students': ['S100100103', 'S100100120'], 'faculty': ['F100100103']},
    {'course_code': 'ITMT 2500.002', 'department': 'it_management', 'students': ['S100100103', 'S100100120'], 'faculty': ['F100100103']},
    {'course_code': 'ITMT 3500.003', 'department': 'it_management', 'students': ['S100100103'], 'faculty': ['F100100103']},
    {'course_code': 'ITMT 4500.004', 'department': 'it_management', 'students': ['S100100120'], 'faculty': ['F100100103']},
    {'course_code': 'EENG 1910.001', 'department': 'electrical_engineering', 'students': ['S100100104', 'S100100112'], 'faculty': ['F100100104']},
    {'course_code': 'EENG 2610.002', 'department': 'electrical_engineering', 'students': ['S100100104', 'S100100112'], 'faculty': ['F100100104']},
    {'course_code': 'EENG 2710.003', 'department': 'electrical_engineering', 'students': [], 'faculty': ['F100100104']},
    {'course_code': 'EENG 3510.004', 'department': 'electrical_engineering', 'students': [], 'faculty': ['F100100104']},
    {'course_code': 'MEEN 2210.001', 'department': 'mechanical_engineering', 'students': ['S100100105'], 'faculty': ['F100100105']},
    {'course_code': 'MEEN 2301.002', 'department': 'mechanical_engineering', 'students': ['S100100105'], 'faculty': ['F100100105']},
    {'course_code': 'MEEN 3240.003', 'department': 'mechanical_engineering', 'students': ['S100100117'], 'faculty': ['F100100105']},
    {'course_code': 'MEEN 3310.004', 'department': 'mechanical_engineering', 'students': [], 'faculty': ['F100100105']},
    {'course_code': 'PHYS 1710.001', 'department': 'physics', 'students': ['S100100100', 'S100100108', 'S100100119'], 'faculty': ['F100100109']},
    {'course_code': 'PHYS 2220.002', 'department': 'physics', 'students': ['S100100102', 'S100100119'], 'faculty': ['F100100109']},
    {'course_code': 'PHYS 3010.003', 'department': 'physics', 'students': [], 'faculty': ['F100100109']},
    {'course_code': 'PHYS 3020.004', 'department': 'physics', 'students': [], 'faculty': ['F100100109']},
    {'course_code': 'VALCANIC 12', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'Rice 2222', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'trats 11111', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'KRIPS 1111', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'pepsi 12111', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'ACOG 333', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
    {'course_code': 'max 2222', 'department': 'cybersecurity', 'students': ['S100100125'], 'faculty': 'F100100112'},
]

    #Updates the list
def updateCoursePyFile():
    filename = "course.py"
    with open(filename, "r") as file:
        lines = file.readlines()
    start_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Course_Info = ["):
            start_index = i
            break
    if start_index is None:
        print("Course_Info definition not found in course.py.")
        return

    #Find the end of Course_Info list
    end_index = start_index + 1
    bracket_balance = 1  
    while end_index < len(lines):
        line = lines[end_index]
        bracket_balance += line.count("[")
        bracket_balance -= line.count("]")
        if bracket_balance == 0:
            end_index += 1  
            break
        end_index += 1

    #Build new Course_Info text
    course_info_text = "Course_Info = [\n"
    for course in Course_Info:
        course_info_text += f"    {course},\n"
    course_info_text += "]\n"

    #Replace old Course_Info with Course_Info text
    new_lines = lines[:start_index] + [course_info_text] + lines[end_index:]

    with open(filename, "w") as file:
        file.writelines(new_lines)

    print(f"course.py successfully updated with latest Course_Info!")

#Manual Update
if __name__ == "__main__":
    updateCoursePyFile()