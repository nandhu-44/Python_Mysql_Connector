# To create table `Employee` to new database Student
import mysql.connector as sqltor

# Reading password!
passwordFile = open("password.txt","r+")
passWord = passwordFile.read()
passwordFile.close()

# Establishing connection
mydb = sqltor.connect(host='localhost',user='root',password=f'{passWord}',port ='4500',database='student')

# Using cursor() to prepare cursor
mc=mydb.cursor()
# mc.execute('CREATE DATABASE IF NOT EXISTS Student;')
# print("Created database \"Student\". ")
# mc.execute('USE Student;')
# print("Using database \"Student\". ")

# Preparing sql statement to create tables
# To create table
mc.execute('CREATE TABLE IF NOT EXISTS Student(admissionno int(4) primary key,name varchar(20) not null, marks int(3));')
# to Add data

Studno = int(input('Enter Student admission number: '))
Studname = input('Enter Student Name: ')
StudMarks = int(input('Enter the marks: '))
mc.execute(f'Insert into Student values({Studno},"{Studname}",{StudMarks})')
mydb.commit()
print("Successfully added record into table")

mydb.close()
