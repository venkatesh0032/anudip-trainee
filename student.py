student = {}

student['id'] = input("Enter student ID: ")
student['name'] = input("Enter student Name: ")
student['age'] = int(input("Enter student Age: "))
student['city'] = input("Enter student City: ")
student['phone'] = input("Enter student Phone Number: ")

print("\n - Student Details -")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
