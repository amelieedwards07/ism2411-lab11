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
