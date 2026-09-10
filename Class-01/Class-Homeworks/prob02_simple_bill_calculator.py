while True:
    try:
        product_price = float(input("How much does the product cost?: "))
        quantity = int(input("How many product did you buy?: "))
        break
    except ValueError:
        print("You must insert a valid number. Please type digits only.")

total_cost = product_price * quantity
print(f"Total cost without tax ${total_cost:.2f}.")

total_cost_with_tax = total_cost * 1.05
print(f"Total cost with 5% tax ${total_cost_with_tax:.2f}$.")