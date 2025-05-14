Faculty_Info = [
    {'ID': 'F100100100', 'Faculty': 'Rene Monreal', 'Department': 'cybersecurity', 'Course_Teaching': 'CYBR 2100.001, PHYS 1710.001', 'Status': 'Active'},
    {'ID': 'F100100101', 'Faculty': 'Lionel Messi', 'Department': 'computer_science', 'Course_Teaching': 'CSCE 1035.001', 'Status': 'Active'},
    {'ID': 'F100100102', 'Faculty': 'Cristiano Ronaldo', 'Department': 'cybersecurity', 'Course_Teaching': 'CYBR 3100.002', 'Status': 'Active'},
    {'ID': 'F100100103', 'Faculty': 'LeBron James', 'Department': 'it_management', 'Course_Teaching': 'ITMT 2500.002, ITMT 3500.003', 'Status': 'Active'},
    {'ID': 'F100100104', 'Faculty': 'Serena Williams', 'Department': 'electrical_engineering', 'Course_Teaching': 'EENG 2610.002', 'Status': 'Active'},
    {'ID': 'F100100105', 'Faculty': 'Tom Brady', 'Department': 'mechanical_engineering', 'Course_Teaching': 'MEEN 2301.002', 'Status': 'Inactive'},
    {'ID': 'F100100107', 'Faculty': 'Usain Bolt', 'Department': 'cybersecurity', 'Course_Teaching': 'CYBR 3200.003', 'Status': 'Active'},
    {'ID': 'F100100108', 'Faculty': 'Michael Jordan', 'Department': 'computer_science', 'Course_Teaching': 'CSCE 2610.005, CSCE 1040.002', 'Status': 'Active'},
    {'ID': 'F100100109', 'Faculty': 'Crewated 1', 'Department': 'physics', 'Course_Teaching': 'CSCE 2610.005', 'Status': 'Active'},
    {'ID': 'F100100110', 'Faculty': 'CREATED 2', 'Department': 'math', 'Course_Teaching': 'CYBR 3100.002', 'Status': 'Active'},
    {'ID': 'F100100111', 'Faculty': 'BUBBBA', 'Department': 'cybersecurity', 'Course_Teaching': 'MATH 3680.004, max 2222', 'Status': 'Active'},
    {'ID': 'F100100112', 'Faculty': 'CHECK NEW OUR', 'Department': 'Cybersecurity', 'Course_Teaching': 'PHYS 3020.004, max 2222', 'Status': 'Active'},
]
Departments = [
    {'Department': 'computer_science', 'faculty': ['F100100101', 'F100100108']},
    {'Department': 'math', 'faculty': ['F100100110']},
    {'Department': 'cybersecurity', 'faculty': ['F100100100', 'F100100107', 'F100100102', 'F100100111']},
    {'Department': 'it_management', 'faculty': ['F100100103']},
    {'Department': 'electrical_engineering', 'faculty': ['F100100104']},
    {'Department': 'mechanical_engineering', 'faculty': ['F100100105']},
    {'Department': 'physics', 'faculty': ['F100100109']},
]

#Updates lists
def updateFacultyPyFile():
    filename = "faculty.py"
    with open(filename, "r") as file:
        lines = file.readlines()
    start_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Faculty_Info = ["):
            start_index = i
            break

    #Build new Faculty_Info text
    faculty_info_text = "Faculty_Info = [\n"
    for fac in Faculty_Info:
        faculty_info_text += f"    {fac},\n"
    faculty_info_text += "]\n"

    end_index = start_index
    while end_index < len(lines) and "]" not in lines[end_index]:
        end_index += 1
    end_index += 1 

    # Replace old list with new list
    new_lines = lines[:start_index] + [faculty_info_text] + lines[end_index:]
    with open(filename, "w") as file:
        file.writelines(new_lines)
    print(f"faculty.py successfully updated with latest Faculty_Info!")

def update_department_faculty():
    import copy

    # Create a deep copy so we don't modify the global Departments list directly
    department_dict = {dept['Department']: copy.deepcopy(dept) for dept in Departments}

    # Get list of all valid faculty IDs
    valid_faculty_ids = [faculty['ID'] for faculty in Faculty_Info]
    for department in department_dict.values():
        department['faculty'] = [fid for fid in department['faculty'] if fid in valid_faculty_ids]

    # Add current faculty IDs to their respective department
    for faculty_member in Faculty_Info:
        faculty_id = faculty_member['ID']
        department_name = faculty_member['Department']
        if department_name in department_dict:
            department = department_dict[department_name]
            if faculty_id not in department['faculty']:
                department['faculty'].append(faculty_id)
                print(f"Added Faculty ID {faculty_id} to the {department_name} department.")
        else:
            print(f"Department {department_name} not found.")

    return list(department_dict.values())

def updateListInFile(list_name, updated_list):
    filename = "faculty.py"
    with open(filename, "r") as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{list_name} = ["):
            start_index = i
            break
    if start_index is None:
        print(f"{list_name} not found in {filename}.")
        return
    bracket_count = 0
    for j in range(start_index, len(lines)):
        bracket_count += lines[j].count('[')
        bracket_count -= lines[j].count(']')
        if bracket_count == 0:
            end_index = j + 1
            break
    if end_index is None:
        print(f"Could not find end of {list_name} in {filename}.")
        return

    #Build new list text
    list_text = f"{list_name} = [\n"
    for item in updated_list:
        list_text += f"    {item},\n"
    list_text += "]\n"

    #Replace old list with new list
    new_lines = lines[:start_index] + [list_text] + lines[end_index:]

    with open(filename, "w") as file:
        file.writelines(new_lines)

    print(f"{filename} successfully updated with latest {list_name}.")
#Manual Update
if __name__ == "__main__":

    print("\nUpdating department faculty lists...\n")
    updated_departments = update_department_faculty()

    print("\nSaving updated Departments list to faculty.py...\n")
    updateListInFile("Departments", updated_departments)

    print("\nSaving updated Faculty_Info list to faculty.py...\n")
    updateListInFile("Faculty_Info", Faculty_Info)

    print("\nUpdates complete.\n")