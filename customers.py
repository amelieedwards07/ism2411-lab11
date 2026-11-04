# Reflection 1:
# I would use .get() when I'm not sure if a key exists, like when a customer might not have an email on file. I would use brackets when I know the key should be there because it will show an error if something is missing.

# Reflection 2:
# This reminds me of PivotTables in Excel, where you can group sales by region and calculate totals. Python can be better for large datasets because it can automatically organize and calculate everything without having to do it manually.

# Exercise 1 - One Customer

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