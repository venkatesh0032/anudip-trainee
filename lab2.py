a = int(input("Enter a number: "))
print("Even" if a % 2 == 0 else "Odd")

b = int(input("Enter first number (b): "))
c = int(input("Enter second number (c): "))

b, c = c, a

print(f"After swapping: b = {b}, c = {c}")


km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} kilometers is equal to {miles:.2f} miles")


P = 200     
T = 5       
R = 5       

SI = (P * T * R) / 100
print(f"Simple Interest is: Rs. {SI}")
