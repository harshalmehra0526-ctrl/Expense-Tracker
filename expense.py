from abc import ABC, abstractmethod
import csv
import os

# ---------------- Abstract Base Class ---------------- #

class Transaction(ABC):

    def __init__(self, date, amount, category):
        self.date = date
        self.__amount = amount
        self.category = category

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def display(self):
        pass


# ---------------- Income Class ---------------- #

class Income(Transaction):

    def display(self):
        print(f"{self.date} | Income | ₹{self.get_amount()} | {self.category}")


# ---------------- Expense Class ---------------- #

class Expense(Transaction):

    def display(self):
        print(f"{self.date} | Expense | ₹{self.get_amount()} | {self.category}")


# ---------------- Expense Tracker ---------------- #

class ExpenseTracker:

    def __init__(self):
        self.records = []

    def add_income(self, date, amount, category):
        self.records.append(Income(date, amount, category))
        print("Income Added Successfully!")

    def add_expense(self, date, amount, category):
        self.records.append(Expense(date, amount, category))
        print("Expense Added Successfully!")


tracker = ExpenseTracker()
# ---------------- View All Records ---------------- #

def view_records():

    if len(tracker.records) == 0:
        print("\nNo Records Found.")
        return

    print("\n--------- All Transactions ---------")

    for record in tracker.records:
        record.display()


# ---------------- Search by Category ---------------- #

def search_category():

    category = input("Enter Category: ").lower()

    found = False

    print("\nSearch Results")

    for record in tracker.records:

        if record.category.lower() == category:
            record.display()
            found = True

    if not found:
        print("No Records Found.")


# ---------------- Monthly Summary ---------------- #

def monthly_summary():

    income = 0
    expense = 0

    for record in tracker.records:

        if isinstance(record, Income):
            income += record.get_amount()

        elif isinstance(record, Expense):
            expense += record.get_amount()

    print("\n--------- Monthly Summary ---------")
    print("Total Income  : ₹", income)
    print("Total Expense : ₹", expense)
    print("Savings       : ₹", income - expense)


# ---------------- Add Transaction ---------------- #

def add_transaction():

    print("\n1. Add Income")
    print("2. Add Expense")

    choice = input("Enter Choice: ")

    date = input("Enter Date (DD/MM/YYYY): ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount!")
        return

    category = input("Enter Category: ")

    if choice == "1":
        tracker.add_income(date, amount, category)

    elif choice == "2":
        tracker.add_expense(date, amount, category)

    else:
        print("Invalid Choice!")

# ---------------- Save Records ---------------- #

def save_records():

    try:

        with open("expenses.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Type", "Date", "Amount", "Category"])

            for record in tracker.records:

                if isinstance(record, Income):
                    record_type = "Income"
                else:
                    record_type = "Expense"

                writer.writerow([
                    record_type,
                    record.date,
                    record.get_amount(),
                    record.category
                ])

        print("Records Saved Successfully!")

    except Exception as e:
        print("Error:", e)


# ---------------- Load Records ---------------- #

def load_records():

    if not os.path.exists("expenses.csv"):
        return

    try:

        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                record_type, date, amount, category = row

                amount = float(amount)

                if record_type == "Income":
                    tracker.records.append(
                        Income(date, amount, category)
                    )

                else:
                    tracker.records.append(
                        Expense(date, amount, category)
                    )

    except Exception as e:
        print("Error Loading File:", e)

# ---------------- Main Menu ---------------- #

def main():

    load_records()

    while True:

        print("\n" + "=" * 40)
        print("        EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Transaction")
        print("2. View All Records")
        print("3. Search by Category")
        print("4. Monthly Summary")
        print("5. Save Records")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_records()

        elif choice == "3":
            search_category()

        elif choice == "4":
            monthly_summary()

        elif choice == "5":
            save_records()

        elif choice == "6":
            save_records()
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid Choice! Please try again.")


# ---------------- Run Program ---------------- #

if __name__ == "__main__":
    main()                