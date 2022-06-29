# Input Validation

Produced a command-line driven telephone listing program. The program is capable of 
receiving and storing a list of people with their full name and telephone. The program shall include 
the following commands:
• ADD “<Person>” “<Telephone #>” - Add a new person to the database
• DEL “<Person>” - Remove someone from the database by name
• DEL “<Telephone #>” - Remove someone by telephone #
• LIST - Produce a list of the members of the database
  
  Created regular expressions for <Person> and <Telephone #> and used these regular expressions to 
  verify that the user is supplying valid data
  
  Stored the entries in databse SQLite3.
  Used an API supporting parametrized queries(prepared statements) in SELECT and INSERT statements, which will avoid SQL injection vulnerabilities.
  
  
  DESCRIPTION OF THE PROJECT IN DETAIL CAN BE FOUND IN ASSIGNMENT REPORT
