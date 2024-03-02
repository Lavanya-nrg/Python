# Write a Python program to skip the headers of a given CSV file. Use csv.reader

# Import the csv module for handling CSV files
import csv

# Open the 'employees.csv' file in read mode
f = open("employees.csv", "r")

# Create a CSV reader object using the opened file
reader = csv.reader(f)

# Skip the header row (assuming it contains column names) using next() function
next(reader)

# Iterate through each row in the CSV file and print it
for row in reader:
    print(row)
