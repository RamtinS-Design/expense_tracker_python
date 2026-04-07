# Expense Tracker Python
A simple Python program that stores expenses in a file, reads them back, and calculates the total spending for each category.

## Features
- Save expenses to a text file
- Read expense data from a file
- Categorize expenses 
- Calculate total spending per category

## How It Works
- The program writes expense data to a file called expenses.txt.
- Each expense is stored in the format:
- category,amount
- The program reads each line from the file.
- It splits the category and amount using split(",").
- A Python dictionary is used to store and update totals for each category.
- Finally, the program prints the total spending per category.

## What I Learned
- Using file handling with open() and with open()
- Reading and writing data to files
- Working with dictionaries to store grouped data
- Using loops to process file data
- Using split() to separate text values

## Future Improvements
- Allow users to input their own expenses
- Add dates to track spending history
- Save data using CSV or JSON
- Create a monthly spending summary
- Build a simple GUI interface
- Add charts or graphs for spending visualization

## Author
Made by (RamtinS-Design)
