# 1
def enter_marks():
    marks = []
    try:
        for i in range(5):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Mark should be between 0 and 100")
            marks.append(mark)
        print("Marks entered:", marks)
    except ValueError as e:
        print("Error:", e)

enter_marks()

# 2
def validate_email():
    try:
        email = input("Enter your email: ")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        print("Valid email.")
    except ValueError as e:
        print("Error:", e)

validate_email()

# 3
def login_system():
    correct_username = "admin"
    correct_password = "1234"

    attempts = 0
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            print("Login failed.")
            attempts += 1
    else:
        raise PermissionError("Access denied after 3 failed attempts.")

try:
    login_system()
except PermissionError as e:
    print("Error:", e)

# 4
def check_password():
    try:
        password = input("Enter a password: ")
        if len(password) < 8:
            raise ValueError("Weak password")
        print("Password accepted.")
    except ValueError as e:
        print("Error:", e)

check_password()

# 5
class NegativeNumberError(Exception):
    pass

def get_positive_number():
    try:
        number = int(input("Enter a positive number: "))
        if number < 0:
            raise NegativeNumberError("Negative number entered")
        print("You entered:", number)
    except NegativeNumberError as e:
        print("Error:", e)

get_positive_number()
