import sqlite3
from employee import Employee

class EmployeeDAO:

    def __init__(self):
        self.conn = sqlite3.connect('employee.db')
        self.cursor = self.conn.cursor()

    def insert(self, employee):
        self.cursor.execute('''
        INSERT INTO employee(name, position, salary, hire_date)
        VALUES(?, ?, ?, ?)
        ''', (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date()))

        self.conn.commit()
        employee.id  = self.cursor.lastrowid
        return employee.id
    
    def get_by_id(self, id):
        self.cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
        employ = self.cursor.fetchone()
        if employ:
            return Employee(employ[0], employ[1], employ[2], employ[3], employ[4])
        return None
    
    def get_all(self):
        self.cursor.execute('SELECT * FROM employee')
        return [Employee(employ[0], employ[1], employ[2], employ[3], employ[4]) for employ in self.cursor.fetchall()]
    
    def update(self, employee):
        self.cursor.execute('''
        UPDATE employee
        SET name = ?, position = ?, salary = ?, hire_date = ?
        WHERE id = ?
        ''', (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date(), employee.get_id()))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM employee WHERE id = ?', (id,))
        self.conn.commit()


        