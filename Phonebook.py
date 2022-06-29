#!/usr/bin/env  python3

import sys 
import sqlite3
import re

connection = sqlite3.connect('PhoneDirectory.db')    #connecting to database
print('\nConnecting to database')
print('Connection successful....\n')
cur = connection.cursor()                            #creating cursor for database

cur.execute('CREATE TABLE IF NOT EXISTS Phonebook(Name TEXT PRIMARY KEY, Phone INTEGER)')

connection.commit()            #commit is used to make permanent changes to db

#usr_inp = input("Enter your choice").lower()

#x = input("Enter the command\n").upper()

x = sys.argv

def Add(a, b):
  contact_name = a
  contact_phone = b

  phone = re.compile("\d{5,6}|\(\d{3}\)\d{3}-\d{3,}|" + "\d\(\d{3}\)\d{3}-\d{3,}|" + "\d{3}-\d{4}|\+\d{1,2}\(\d{3}\)\d{3}-\d{3,}|"+
  	             "\+\d{1,2}\s\(\d{2}\)\s\d{3}-\d{3,}|" + "\d{5}\.\d{5}")
  name = re.compile(r"^([A-Za-z]*[\s',]*)?([a-zA-Z']*[',\s-]*[a-zA-Z.']*[',\s-]*)$")
	
  if (re.match(name, contact_name)):
    if (re.match(phone, contact_phone)):
      connection=sqlite3.connect('PhoneDirectory.db')
      cur=connection.cursor()
			
      cur.execute("INSERT INTO PhoneBook (Phone,Name) VALUES(" + contact_phone + ", '" + contact_name + "')")
			
      connection.commit()
      print("\nentry added")
      return 0
    else:
      print("\nInvalid Phone No")
      return 1      
  else:
    print("\nInvalid name")
    return 1
 
def Delete(c):
  contact = c
  connection=sqlite3.connect('PhoneDirectory.db')
  cur= connection.cursor()
  cur.execute("SELECT Name FROM PhoneBook WHERE Name =(?) or Phone = (?)",[contact, contact]);
  x1=cur.fetchall()
  print(x1)
  if not x1:
    print("Invalid entry")
    return 1
  else:
    cur.execute("DELETE FROM PhoneBook WHERE Name =(?)", [x1[0][0]]);
    connection.commit()
    print("\nEntry Deleted")
    return 0
  
   


    
def List():
  connection=sqlite3.connect('PhoneDirectory.db')
  cur= connection.cursor()
   
  #selecting all the data from table PhoneBook
  cur.execute("SELECT * FROM PhoneBook");
  contact_data=cur.fetchall()
  connection.commit()
   
  print('\n The Phone Directory Details are as follow:')
  print('\n', contact_data, '\n')  
  return 0
  
if x[1] == 'ADD':
  Add(x[2], x[3])
elif x[1] == 'DEL':
  Delete(x[2])
elif x[1] == 'LIST':
  List()


  
  

  

			
	


	
	
	

