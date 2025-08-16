import datetime
import json
import os

# File name
FILE_NAME = "data.json"

# If file doesn't exist, create an empty one
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump({"finance": [], "tasks": []}, f)

# Load data
def load_data():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add income or expense
def add_finance(amount, description):
    data = load_data()
    record = {
        "amount": amount,
        "description": description,
        "date": str(datetime.date.today())
    }
    data["finance"].append(record)
    save_data(data)
    print("✅ Saved successfully!")

# Add daily task
def add_task(task):
    data = load_data()
    record = {
        "task": task,
        "date": str(datetime.date.today())
    }
    data["tasks"].append(record)
    save_data(data)
    print("✅ Task added!")

# Show report
def show_report():
    data = load_data()
    incomes = sum(item["amount"] for item in data["finance"] if item["amount"] > 0)
    expenses = sum(-item["amount"] for item in data["finance"] if item["amount"] < 0)

    print("\n📊 Today's Report:")
    print(f"Total Income: {incomes}")
    print(f"Total Expenses: {expenses}")
    print("\n📝 Today's Tasks:")

    today = str(datetime.date.today())
    tasks_today = [t["task"] for t in data["tasks"] if t["date"] == today]
    if tasks_today:
        for t in tasks_today:
            print("-", t)
    else:
        print("No tasks recorded.")

# Main program
while True:
    print("\n--- Main Menu ---")
    print("1. Add Income/Expense")
    print("2. Add Task")
    print("3. Show Report")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = int(input("Amount (negative = expense, positive = income): "))
        desc = input("Description: ")
        add_finance(amount, desc)

    elif choice == "2":
        task = input("Task: ")
        add_task(task)

    elif choice == "3":
        show_report()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice!")