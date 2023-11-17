from datetime import datetime
from time import time


class Person:
    def __init__(self, name: str, address: str, phone_number: str, email: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Person: {self.name}"


class Student(Person):
    def __init__(self, name: str, address: str, phone_number: str, email: str, class_status: str):
        super().__init__(name, address, phone_number, email)
        self.class_status = class_status

    def __str__(self):
        return f"Student: {super().__str__()}"


class Employee(Person):
    def __init__(self, name: str, address: str, phone_number: str, email: str, office: str, salary: float,
                 date_hired: datetime):
        super().__init__(name, address, phone_number, email)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __str__(self):
        return f'Employee: {super().__str__()}'


class Faculty(Employee):
    def __init__(self, name: str, address: str, phone_number: str, email: str, office: str, salary: float,
                 date_hired: datetime, office_hours: time, rank: str):
        super().__init__(name, address, phone_number, email, office, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __str__(self):
        return f"Faculty: {super().__str__()}"


class Staff(Employee):
    def __init__(self, name: str, address: str, phone_number: str, email: str, office: str, salary: float,
                 date_hired: datetime, title: str):
        super().__init__(name, address, phone_number, email, office, salary, date_hired)
        self.title = title

    def __str__(self):
        return f'Staff: {super().__str__()}'


person = Person("John Doe", "123 Main St", "555-1234", "john.doe@email.com")
student = Student("Alice Smith", "456 Oak St", "555-5678", "alice.smith@email.com", "Junior")
employee = Employee("Bob Johnson", "789 Pine St", "555-9876", "bob.johnson@email.com", "Office 101", 50000.0,
                    datetime.now())
faculty = Faculty("Jane Miller", "101 Elm St", "555-4321", "jane.miller@email.com", "Office 202", 80000.0,
                  datetime.now(), "Monday 2-4 PM", "Associate Professor")
staff = Staff("Chris Davis", "202 Maple St", "555-8765", "chris.davis@email.com", "Office 303", 60000.0, datetime.now(),
              "Administrative Assistant")


print(person)
print(student)
print(employee)
print(faculty)
print(staff)
