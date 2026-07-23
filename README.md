# 💰 Expense Tracker

A simple **Python-based Expense Tracker** that helps users manage their personal finances by recording **Income** and **Expenses**. The application stores data in a **CSV file**, allowing users to save and load records even after closing the program.

---

# 📌 Project Overview

The Expense Tracker is a **menu-driven console application** developed using **Python** and **Object-Oriented Programming (OOP)** concepts. It enables users to:

✅ Add Income  
✅ Add Expenses  
✅ View All Transactions  
✅ Search Transactions by Category  
✅ View Monthly Summary  
✅ Save Records to CSV File  
✅ Load Saved Records Automatically

---

# ✨ Features

💵 **Add Income**
- Record income with date, amount, and category.

💸 **Add Expense**
- Record expenses with date, amount, and category.

📋 **View All Records**
- Display every saved transaction.

🔍 **Search by Category**
- Find transactions based on categories like Food, Salary, Shopping, etc.

📊 **Monthly Summary**
- Calculate:
  - Total Income
  - Total Expenses
  - Total Savings

💾 **Save Records**
- Store all transactions in a CSV file.

📂 **Load Records**
- Automatically loads previously saved data when the program starts.

⚠️ **Error Handling**
- Prevents invalid amount entries using exception handling.

---

# 🛠️ Technologies Used

- 🐍 Python 3
- 📄 CSV Module
- 📁 OS Module
- 💻 Object-Oriented Programming (OOP)

---

# 🧠 OOP Concepts Used

### 🔹 Abstraction
Implemented using the abstract `Transaction` class.

### 🔹 Inheritance
`Income` and `Expense` classes inherit from the `Transaction` class.

### 🔹 Encapsulation
The amount is stored as a private variable using getter and setter methods.

### 🔹 Polymorphism
Both child classes implement their own version of the `display()` method.

---

# 📂 Project Structure

```
Expense Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

---

# ▶️ How to Run

### Step 1️⃣
Install **Python 3**.

### Step 2️⃣
Download or clone the project.

### Step 3️⃣
Open the project folder in **VS Code** or any Python IDE.

### Step 4️⃣
Run the program:

```bash
python expense_tracker.py
```

---

# 📋 Menu

```
========================================
        EXPENSE TRACKER
========================================

1. Add Transaction
2. View All Records
3. Search by Category
4. Monthly Summary
5. Save Records
6. Exit
```

---

# 📝 Sample Output

```
Enter your choice: 1

1. Add Income
2. Add Expense

Enter Date (DD/MM/YYYY): 15/07/2026
Enter Amount: 5000
Enter Category: Salary

✅ Income Added Successfully!
```

---

# 💾 Data Storage

All transaction records are stored inside:

```
expenses.csv
```

The CSV file contains:

| Type | Date | Amount | Category |
|------|------|--------|----------|
| Income | 15/07/2026 | 5000 | Salary |
| Expense | 16/07/2026 | 1200 | Food |

---

# 📈 Future Enhancements

🚀 User Login System

✏️ Edit Transactions

🗑️ Delete Transactions

📅 Date-wise Filtering

📊 Graphical Reports & Charts

🖥️ GUI Version using Tkinter

☁️ Database Integration (MySQL)

📱 Mobile App Version

---

# 🎯 Learning Outcomes

Through this project, I learned:

- 🐍 Python Programming
- 🧩 Object-Oriented Programming
- 🔒 Encapsulation
- 🏛️ Abstraction
- 👨‍👩‍👧 Inheritance
- 🔄 Polymorphism
- 📄 CSV File Handling
- ⚠️ Exception Handling
- 📊 Data Management
- 📋 Menu-driven Program Development

---

# 👨‍💻 Author

**Name:** Harshal Mehra

🎓 **Course:** B.Com (Hons)

💻 **Project:** Expense Tracker using Python

---

# ⭐ Thank You

Thank you for checking out this project! 😊

If you find it useful, don't forget to ⭐ the repository (if hosted on GitHub).

**Happy Coding! 🚀🐍**