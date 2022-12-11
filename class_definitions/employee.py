"""
Program: employee.py
Auther: Katie Freerksen
Last Date Modified: 11/18/2022
This creates an employee class, and puts together a string of the attributes
"""
class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phone, sal, start, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone = phone
        self._salaried = sal
        self._start_date = start
        self._salary = salary

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, addy):
        self.address = addy

    def set_phone(self, phone):
        self.phone = phone

    def set_salaried(self, sal):
        self._salaried = sal

    def set_start_date(self, start):
        self._start_date = start

    def set_salary(self, salary):
        self._salary = salary

    def display(self):
        string = self.last_name + ", " + self.first_name + "\n" + self.address + "\n"
        if self._salaried == 'true':
            string += "Salaried employee: " + "${:.0f}".format(self._salary) + "/year\n"
        else:
            string += "Hourly employee: " + "${:.2f}".format(self._salary) + "/hour\n"
        string += "Start date: " + str(self._start_date) + "\n"
        return string

# Driver
emp = Employee('Ruiz', 'Matthew', '123 south street\nAnkeny, Iowa', '555-867-5309', 'true', '7/18/2022', 45000 )
# call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp                             # clean up!

emp = Employee('Ruiz', 'Matthew', '123 south street\nAnkeny, Iowa', '555-867-5309', 'false', '7/18/2022', 15.25 )
# call the construtor, needs to have a first and last name in parameter
print(emp.display())                # display returns a str, so print the information
del emp                             # clean up!
