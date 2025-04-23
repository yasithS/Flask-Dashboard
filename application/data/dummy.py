import csv
import random
from datetime import datetime, timedelta
import os


# defining expenses and income categories for generation
expense_categories = [
    "Rent", "Groceries", "Utilities", "Transportation", 
    "Dining Out", "Entertainment", "Shopping", "Healthcare",
    "Education", "Travel", "Insurance", "Subscriptions"
]

income_categories = [
    "Salary", "Freelance", "Investments", "Gifts", 
    "Refunds", "Side Business", "Bonus", "Other Income"
]

types = ["income", "expense"]

# generate random data
entries = 20
data = []

# set starting date
start_date = datetime.now() - timedelta(days=30)

# prepare the data
for _ in range(entries):

    entry_type = random.choice(types)

    if entry_type == "income":
        entry_category = random.choice(income_categories)
    else:
        entry_category = random.choice(expense_categories)

    # generating a random date
    entry_date = start_date + timedelta(days=random.randint(0, 30)) 
    
    if entry_type == "income":
        entry_amount = round(random.uniform(100, 3000), 2)
    else:
        entry_amount = round(random.uniform(100, 1000), 2)

    data.append({
        "type": entry_type,
        "category": entry_category,
        "date": entry_date.strftime("%Y-%m-%d"),
        "amount": entry_amount
    })

# test
# print("Generated Data:")
# for entry in data:
#     print(entry)

# write data into a CSV file
csv_file = "application/data/expenses.csv"

with open( csv_file, 'w', newline='' ) as file:
    fieldnames = ["type", "category", "date", "amount"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Data written to CSV file successfully.")


    


