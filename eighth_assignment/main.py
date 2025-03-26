from database import Database 
from employee import Employee
from employee_dao import EmployeeDAO
from time import sleep


if __name__ == "__main__":
    
    db = Database()
    db.setup_database()

    dao = EmployeeDAO()

    name = input('Enter name: ')
    position = input('Enter position: ')
    salary = float(input('Enter salary: '))
    hire_date = input('Enter hire date: ')


    print('Inserting employee...')
    sleep(2)
    emp1 = Employee(None, name, position, salary, hire_date)
    dao.insert(emp1)

    print('Getting employee by id...')
    sleep(2)
    emp2 = dao.get_by_id(emp1.get_id())
    print(emp2)

    print('Getting all employees...')
    sleep(2)
    for emp in dao.get_all():
        print(emp)

    print('Updating employee...')
    sleep(2)
    emp2.set_name('John Doe')
    emp2.set_position('Manager')
    emp2.set_salary(5000)
    emp2.set_hire_date('2020-01-01')
    dao.update(emp2)

    print('Deleting employee...')
    sleep(2)
    if dao.delete(emp2.get_id()):
        print('Employee deleted')
    else:
        print('Employee not found')