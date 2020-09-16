#Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
# as well as a method that prints the total number of employees and a method
# that displays information about each employee in particular, namely the name and salary.
#In addition to creating a class, display information about the base classes
# from which the employee class is inherited (__base__), the class namespace (__dict__),
# the class name (__name__), the module name in which the class is defined (__module__), the documentation bar ( __doc__)

class Employee():
    """Employee class. Each employee has characteristics such as name and salary."""

    total_employee = 0

    def __init__(self, name,salary):
        Employee.total_employee += 1
        self.name = name
        self.salary = salary

    def view_tolal_number_of_employee(self):
        print (f"The total number of Employee :{Employee.total_employee}")

    def display_info(self):
        print(f"Employee name is {self.name}. Her / His salary is {self.salary}")



Empl1=Employee('Victor',20000)
Empl2=Employee('Ivan',20000)
Empl1.view_tolal_number_of_employee()
Empl3=Employee('Olya',20600)
Empl1.view_tolal_number_of_employee()
Empl1.display_info()

print(f"--> employee class is inherited from {Employee.__base__},\n--> the class namespace is {Employee.__dict__},\n--> the class name is {Employee.__name__} \n\
--> the module name in which the class is defined is {Employee.__module__} ,\n--> the documentation bar is : {Employee.__doc__}")

