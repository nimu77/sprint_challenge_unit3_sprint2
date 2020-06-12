import sqlite3

# filepath to connect
filepath = 'northwind_small.sqlite3'

# connecting to sqlite database
connection = sqlite3.connect(filepath)

# cursor to manipulate data
cursor = connection.cursor()

# queries

# part 2
# What are the ten most expensive items (per unit price)  in the database

query = '''
SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

answer1 = cursor.execute(query).fetchall()
print(' # What are the ten most expensive items (per unit price)  in the database?')
print(f'The top ten most expensive items (per unit price) in the database are: \n {answer1}')

# What is the average age of an employee at the time of their hiring?

query = '''
SELECT avg (HireDate - BirthDate)
    FROM Employee
'''

answer2 = cursor.execute(query).fetchall()
print(' \n # What is the average age of an employee at the time of their hiring?')
print(f'The average age of an employee at the time of their hiring is {answer2[0][0]:.2f}.')

# How does the average age of employee at hire vary by city?

# part 3
# What are the ten most expensive items (per unit price) in the database *and* their suppliers?

query = '''
SELECT p.ProductName, s.CompanyName, p.UnitPrice
    FROM Product p
    Left JOIN Supplier s ON p.Id = s.Id
    ORDER BY p.UnitPrice DESC
    LIMIT 10
'''

answer4 = cursor.execute(query).fetchall()
print(' \n # What are the ten most expensive items (per unit price) in the database *and* their suppliers?')
print(f'The top most expensive items in the database and their suppliers are: \n{answer4}')

# What is the largest category (by number of unique products in it)?

query = '''
SELECT c.CategoryName, count (c.Id) as category_count
    FROM Category c
    JOIN Product p ON c.Id = p.CategoryId
    GROUP BY c.CategoryName
    ORDER BY category_count desc
'''

answer5 = cursor.execute(query).fetchall()
print(' \n # What is the largest category (by number of unique products in it)?')
print(f'The largest category from top to bottom are: {answer5}')