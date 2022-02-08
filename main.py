# To create table `Employee` to new database company
import mysql.connector as sqltor

# Reading password!
passwordFile = open("password.txt","r+")
passWord = passwordFile.read()
passwordFile.close()

# Establishing connection
mydb = sqltor.connect(host='localhost',user='root',password=f'{passWord}')

# Using cursor() to prepare cursor
mc=mydb.cursor()
mc.execute('CREATE DATABASE IF NOT EXISTS Company;')
print("Created database \"Company\". ")
mc.execute('USE Company;')
print("Using database \"Company\". ")

# Preparing sql statement to create tables

mc.execute('CREATE TABLE Employee(empno int(4) primary key);')
