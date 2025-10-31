import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize CSV file if not exists
def init_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass

# Add a new expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: ₹"))
    
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            total = 0
            print("\n📘 Expense List:")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | ₹{row[3]}")
                total += float(row[3])
            print("-" * 50)
            print(f"💰 Total Spent: ₹{total}\n")
    except FileNotFoundError:
        print("❌ No expense records found.\n")

# View total by category
def category_summary():
    summary = {}
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cat = row["Category"]
                summary[cat] = summary.get(cat, 0) + float(row["Amount"])
        
        print("\n📊 Expense Summary by Category:")
        print("-" * 40)
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")
        print("-" * 40)
    except FileNotFoundError:
        print("❌ No expense records found.\n")

# Main menu
def main():
    init_file()
    while True:
        print("""
==== 💼 PERSONAL EXPENSE TRACKER ====
1. Add Expense
2. View All Expenses
3. View Category Summary
4. Exit
""")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("👋 Goodbye! Your data is saved in expenses.csv.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
