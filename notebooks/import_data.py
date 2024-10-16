import mysql.connector
import csv

cnx = mysql.connector.connect(user='root', password='Formation20!',
host='127.0.0.1', port=3306,
database='student_performance')
mycursor = cnx.cursor()

csv_path = r'C:\Users\johan\Documents\IRONHACK\Student_performance\data\raw\Student_performance.csv'
csvreader = csv.reader(csv_path)
data = csvreader.readlines()
print(data)
