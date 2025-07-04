# Q1: How many products to enter?
num_products = int(input("How many products do you want to enter? "))
print("You will enter", num_products, "products.")

# Q2: Collect product details and store in a list of tuples
products = []

for i in range(num_products):
    print(f"\nEnter details for Product {i + 1}:")
    name = input("Product Name: ")
    price = float(input("Price per Unit: "))
    quantity = int(input("Quantity: "))
    product = (name, price, quantity)
    products.append(product)

print("\nAll product entries complete.")

# Q3: Display bill with product name, price, quantity, and total per product
print("\n--- Product Details ---")
print("{:<15} {:<12} {:<10} {:<12}".format("Product", "Unit Price", "Quantity", "Total"))

for name, price, quantity in products:
    total = price * quantity
    print("{:<15} ₹{:<11.2f} {:<10} ₹{:<10.2f}".format(name, price, quantity, total))

# Q4: Calculate total bill
total_bill = 0
for _, price, quantity in products:
    total_bill += price * quantity

print("\nTotal Bill Amount: ₹{:.2f}".format(total_bill))

# Q5: Final formatted bill
print("\n=== Final Bill ===")
print("{:<15} {:<12} {:<10} {:<12}".format("Product", "Unit Price", "Quantity", "Total"))

for name, price, quantity in products:
    total = price * quantity
    print("{:<15} ₹{:<11.2f} {:<10} ₹{:<10.2f}".format(name, price, quantity, total))

print("-" * 50)
print("Total Amount to Pay: ₹{:.2f}".format(total_bill))
