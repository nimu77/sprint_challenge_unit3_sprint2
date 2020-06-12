import sqlite3

# filepath to connect
filepath = 'demo_data.sqlite3'

# connecting to sqlite database
connection = sqlite3.connect(filepath)

# cursor to manipulate data
cursor = connection.cursor()

# count how many rows you have?

query = '''
SELECT count (*)
    FROM demo
'''
answer1 = cursor.execute(query).fetchall()
print('Count how many rows in the table?')
print(f'The number of rows in the table are: {answer1[0][0]}')

# How many rows are there where both 'x' and 'y' are at least 5?

query = '''
SELECT *
    FROM demo
    WHERE x >= 5 AND y >= 5
'''

answer2 = cursor.execute(query).fetchall()
answer2 = len(answer2)
print(' \n How many rows are there where both "x" and "y" are at least 5?')
print(f'The number of rows where both "x" and "y" are at least 5 are: {answer2}')

# How many unique values of `y` are there

query = '''
SELECT COUNT (DISTINCT y)
    FROM demo
'''

answer3 = cursor.execute(query).fetchall()
print(' \n How many unique values of `y` are there?')
print(f'There are {answer3[0][0]} unique values of y.')
