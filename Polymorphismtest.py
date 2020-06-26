#This is the parent Class for all Users
class User:
    name = "steven"
    email = "steven@steven.com"
    password = "passwordisinsecure"

    def getLoginInfo(self):
        entry_name = input("Enter your name:\n ").lower()
        entry_email = input("enter your email:\n ").lower()
        entry_password = input("Enter your password:\n ").lower()
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#This child class is for employees
class Employee(User):
    base_pay = 15.00
    department = "Sporting Goods"
    pin_number = "4546"
    admin = False

    def getLoginInfo(self):
        entry_name = input("Enter your name:\n ").lower()
        entry_email = input("enter your email:\n ").lower()
        entry_pin = input("Enter your pin:\n ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

#Manager class granting administrator rights
class Manager(User):
    base_pay = 32.00
    department = "Grocery"
    pin_number = "9687"
    admin = True

    def getLoginInfo(self):
        entry_name = input("Enter your name:\n ").lower()
        entry_email = input("enter your email:\n ").lower()
        entry_pin = input("Enter your pin:\n ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")
customer = User()
employee = Employee()
Manager = Manager()


def UserType():
    user_type = input("Are you a customer or employee:\n ").lower()
    if user_type == "customer":
        customer.getLoginInfo()
    elif user_type == "employee":
        employee.getLoginInfo()
    elif user_type == "manager":
        Manager.getLoginInfo()
    else:
        print('Please choose customer or employee')
        UserType()


if __name__ == '__main__':
    UserType()