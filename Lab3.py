# 1
def is_palindrome(text):
    return text == text[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# 2
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

text = input("Enter text: ")
print("Number of vowels:", count_vowels(text))

# 3
text = input("Enter text: ")
new_text = text.replace(" ", "-")
print("Modified text:", new_text)

# 4
import re

def is_strong_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'\d', password)):
        return True
    return False

password = input("Enter password: ")
if is_strong_password(password):
    print("Strong password.")
else:
    print("Weak password.")

# 5
def extract_domain(email):
    return email.split('@')[-1]

email = input("Enter email: ")
print("Domain:", extract_domain(email))
