# Reflection 1:
# I would use .get() when I'm not sure if a key exists, like when a customer might not have an email on file. I would use brackets when I know the key should be there because it will show an error if something is missing.

# Reflection 2:
# This reminds me of PivotTables in Excel, where you can group sales by region and calculate totals. Python can be better for large datasets because it can automatically organize and calculate everything without having to do it manually.

# Exercise 1 

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2 

# Add a phone number
customer["phone"] = "239-555-1234"
print(customer)

# Change the tier to platinum
customer["tier"] = "platinum"
print(customer)

# Delete the email
del customer["email"]
print(customer)

# Exercise 3

# Use .get() to look for the deleted email
print(customer.get("email", "no email on file"))

# Use brackets to look for the same email
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4 

# Print each key and value using .items()
for key, value in customer.items():
    print(f"{key}: {value}")

# Loop without .items()
for key in customer:
    print(key)

# Without .items(), the loop only prints the keys. With .items(), the loop gives us both the keys and values.

# Exercise 5 

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

# Find the customer's discount
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

# Calculate the final price
price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6 

customers = [
    customer,
    {"name": "Bob", "tier": "silver", "ytd_spend": 500},
    {"name": "Carlos", "tier": "bronze", "ytd_spend": 200}
]

# Loop through each customer
for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{person['name']} - {tier} - ${discount_amount:.2f} discount")
   
    # Exercise 7 

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

# Check for products with low stock
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")

# Exercise 8 

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

# Create an empty summary dictionary
summary = {}

# Add up sales for each region
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount

# Print totals sorted by region
for region in sorted(summary):
    print(f"{region}: ${summary[region]}")
