def calculate_subtotal(items):
    """Calculates the total cost before tax and discounts."""
    subtotal = 0
    for item in items:
        subtotal += item["quantity"] * item["price"]
    return subtotal

def apply_discount(subtotal, discount_percentage):
    """Calculates the discount amount."""
    return subtotal * (discount_percentage / 100)

def apply_tax(amount_after_discount, tax_percentage):
    """Calculates the tax amount."""
    return amount_after_discount * (tax_percentage / 100)

def generate_bill():
    items = []
    print("=== Welcome to the Shopping Bill Generator ===")
    
    # Input loop for products
    while True:
        name = input("Enter product name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        try:
            quantity = int(input(f"Enter quantity for {name}: "))
            price = float(input(f"Enter unit price for {name}: "))
            
            if quantity < 0 or price < 0:
                print("Quantity and price must be positive numbers. Try again.")
                continue
                
            items.append({"name": name, "quantity": quantity, "price": price})
        except ValueError:
            print("Invalid input! Please enter valid numbers for quantity and price.")
            
    if not items:
        print("No items were added to the bill.")
        return

    # Get discount and tax rates from user
    try:
        discount_rate = float(input("\nEnter discount percentage (%): "))
        tax_rate = float(input("Enter tax percentage (%): "))
    except ValueError:
        print("Invalid percentage input. Setting discount and tax to 0%.")
        discount_rate, tax_rate = 0.0, 0.0

    # Calculations
    subtotal = calculate_subtotal(items)
    discount_amount = apply_discount(subtotal, discount_rate)
    taxable_amount = subtotal - discount_amount
    tax_amount = apply_tax(taxable_amount, tax_rate)
    final_amount = taxable_amount + tax_amount

    # Formatting and Printing the Bill
    print("\n" + "=" * 40)
    print(f"{'TAX INVOICE / SHOPPING BILL':^40}")
    print("=" * 40)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<8} {'Total':<8}")
    print("-" * 40)
    
    for item in items:
        item_total = item["quantity"] * item["price"]
        print(f"{item['name']:<15} {item['quantity']:<5} {item['price']:<8.2f} {item_total:<8.2f}")
        
    print("-" * 40)
    print(f"{'Subtotal:':<30} ${subtotal:>8.2f}")
    print(f"{'Discount (' + str(discount_rate) + '%):':<30} -${discount_amount:>7.2f}")
    print(f"{'Tax (' + str(tax_rate) + '%):':<30} +${tax_amount:>7.2f}")
    print("=" * 40)
    print(f"{'Final Amount:':<30} ${final_amount:>8.2f}")
    print("=" * 40)
    print(f"{'Thank you for shopping with us!':^40}")

# Run the program
if __name__ == "__main__":
    generate_bill()
