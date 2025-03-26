# Fifth Assignment: Object-Oriented Programming

## Overview

This is the eighth assignment for my OOP course in university. It includes classes for managing Employee database. The project is basically first touch to the concept of the databases, and managing them.

## Classes

### Database Class

The `Database` class is class which creates or connects this code to the employee database, using sqlite3 library

### EmployeeDAO Class

The "EmployeeDAO" class is a class in which all the Create, Reading, Update and Delete procceses are handled

### Employee Class

The `Employee` class is an entity class whoch takes name, salary etc. and creates an object, to then insert it to the database via 'EmployeeDAO' class


## Running the Code

To run the code, follow these steps:

1. Ensure you have Python installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory.
4. Run the `main.py` file to start the shopping application


## Example of the output:

Enter name: Sultanbek Muratbekov
Enter position: Teacher
Enter salary: 40000
Enter hire date: 2025-26-03
Inserting employee...
Getting employee by id...
id = 2, name = Sultanbek Muratbekov, position = Teacher, salary = 40000.0, hire date = 2025-26-03
Getting all employees...
id = 2, name = Sultanbek Muratbekov, position = Teacher, salary = 40000.0, hire date = 2025-26-03
Updating employee...
Deleting employee...
Employee not found
