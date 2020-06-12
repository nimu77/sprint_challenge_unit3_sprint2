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

query = '''
SELECT City, avg (HireDate - BirthDate) as City_average_hired_age
    FROM Employee
    GROUP BY City
'''

answer3 = cursor.execute(query).fetchall()
print(' \n # How does the average age of employee at hire vary by city??')
print(f'The average age of an employee hired by city {answer3}.')


# part 3
# What are the ten most expensive items (per unit price) in the database *and* their suppliers?

query = '''
SELECT p.ProductName, s.CompanyName, p.UnitPrice
    FROM Product p
    JOIN Supplier s ON p.SupplierId = s.Id
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

# Who's the employee with the most territories?

query = '''
SELECT et.EmployeeId, e.FirstName, e.LastName, count (et.TerritoryId) as territory_count
    FROM Employee e
    JOIN EmployeeTerritory et ON e.Id = et.EmployeeId
    GROUP BY et.EmployeeId
    ORDER BY territory_count DESC
    LIMIT 1
'''

answer6 = cursor.execute(query).fetchall()
print(' \n # Who"s the employee with the most territories?')
print(f'The employee with most territories is: {answer6[0][1] + " " + answer6[0][2] + " " + "with" + " " + str(answer6[0][3])}')
