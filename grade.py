a = []
for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    a.append(mark)

average = sum(a) / 5
print("Average Marks:", average)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)
