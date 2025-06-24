#ASSIGNMENT 4:-
#question 1: create a CSV file for address book,
#file should have name,address,mobile,email,inset 2-3 dummy data
#-----------------------------------------------------------------------
import csv
details= [['Name','Address','Mobile','Email'],
['Tarun Singh', '123,Civil Lines, Alwar','9876543210','arun@example.com'],
    ['Shivani Faujdar', '35,Keshar Vihar, Delhi','9123456780','shivu@example.com'],
    ['Kirti Singh', 'Apex circle, jaipur', '9988776655', 'kirti@example.com']
]

with open('details.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for x in details:

         writer.writerow(x)
import  csv
with open('details.csv','r',) as file:
    read = csv.reader(file)
    for x in read:
        print(x)

# -----------------------------------------------------------------------------------
# question 2: Refer to our example of weather data and get more details. display them
# ------------------------------------------------------------------------------------
import requests
def weather(city,api):
     url = "https://api.openweathermap.org/data/2.5/weather?"
     final_url = f"{url}q={city}&appid={api}&units=metric"

     try:
        response = requests.get(final_url)
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")

     except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
     except KeyError:
            print("Error: Could not find weather information for this city. Please check the city name.")

city = input("Enter city name: ")
api_key = "1b42834476f72a199bb8833209b9ed5b"
weather(city,api)
# --------------------------------------------------
# Question 3:- Practice Databases
# ---------------------------------------------------
import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",
    user="root",
    password="pubg")

cursor = conn.cursor()
cursor.execute("create database assignment4")


import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",
    user="root",
    password="pubg",
    database="assignment4"
)
cursor = conn.cursor()
# creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    marks INT
)
""")

#inserting into table
cursor.execute("""
INSERT INTO student (name, marks) VALUES
('shivu', 50),
('tarun', 89),
('lucky', 67)
""")

# selecting and displaying records
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('next query...')
cursor.execute("SELECT * FROM student where marks>60")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("delete from student where id=2")


conn.commit()
cursor.close()
conn.close()

import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pubg",
    database="assignment4"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    salary INT
)
""")

# Insert data — without repeating id
cursor.execute("""
INSERT INTO employee (name, salary) VALUES 
('nia', 50000), 
('arti', 89000), 
('preeti', 67000),
('jasleen', 56000),
('rubina', 98000)
""")

# Select all
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()
for row in rows:
    print(row)

print('next query...')

# Select where salary > 60000
cursor.execute("SELECT * FROM employee WHERE salary > 60000")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update salary
cursor.execute("UPDATE employee SET salary = 99000 WHERE id = 2")

# Delete record
cursor.execute("DELETE FROM employee WHERE id = 5")

conn.commit()
cursor.close()
conn.close()