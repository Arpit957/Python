

try:
    employee_file = open("employees.txt", "r")
    # print(employee_file.read())
    for line in employee_file.readlines():
        print(line)
    # print(employee_file.readlines()[2])
    employee_file.close()
except FileNotFoundError:
    print("Error: 'employees.txt' file not found.")