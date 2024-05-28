"""
Author: Christian Paul Marco
Date: May 26, 2024
Purpose: Assignment Part A At-Home

You are contracted to write a program for the development of your payroll
system similar to your in-class activity. The program should prompt the
user to enter values for three variables representing the full name of an
employee and their ID number eg. firstName, lastName empID.

1. The program should concatenate both first and last name variables and
display the result on screen Eg. My name is Serena Williams. Additionally
you should also display the employee's ID number. Though the variables can
be any arbitrary variables be conceptual and demonstrate good programing
practices in relation to the naming of variables as discussed in class.
2. Your program should display the result using the escape character for
tabs.
3. In addition to that your program should also demonstrate appropriate
formatting. 
4. You program should also utilize comments to explain the nature of your
code. 
"""

print("Welcome to Fanshawe Payroll System \n")

#Constants
outputLabel = "First Name \tLast Name \tID "
answer = "y"
tabList = []

# If the answer to add more rows is yes, the loop will keep repeating
# to add more rows
while answer.lower() == "y":
    # Prompt the user to enter their employee ID number
    empID = input("Enter your employee ID number: ")

    # Prompt the user to enter their first name
    firstName = input("Enter your first name: ")
    firstName = firstName[:10].ljust(10) # Adjusts the First name to 10 chars

    # Prompt the user to enter their last name
    lastName = input("Enter your last name: ")
    lastName = lastName[:10].ljust(10) # Adjusts the Last name to 10 chars

    # Concatenate the first name and last name to form the full name
    fullRow = firstName + "\t" + lastName + "\t" + empID

    # Add a row to the tabList list
    tabList.append(fullRow)

    # Prompt the user to add more employee details
    answer = input("Do you want to input another employee details(y/n): ")
    print()

# Output
print(outputLabel)

# Loops in the tabList based on the number of members on the list then
# prints each employee details
for i in range(len(tabList)):
    print(tabList[i])
