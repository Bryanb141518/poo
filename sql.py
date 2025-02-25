import sqlite3

square = lambda n : n*n
print(square(12))
conn =sqlite3.connect("northwind.db")