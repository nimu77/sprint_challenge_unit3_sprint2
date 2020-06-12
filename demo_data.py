import sqlite3

# filepath to connect
filepath = 'demo_data.sqlite3'

# connecting to sqlite database
connection = sqlite3.connect(filepath)

# cursor to manipulate data
cursor = connection.cursor()

# creating a table

query = '''
CREATE TABLE IF NOT EXISTS demo (
    s varchar,
    x int,
    y int
);
'''

# executing the query to populate table
cursor.execute(query)

# inserting data into the table

insertion_query = '''
INSERT INTO demo VALUES 
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
'''

cursor.execute(insertion_query)
connection.commit()
connection.close()

