from abc import ABC, abstractmethod


class Employee(ABC):


    company = "Diggibyte"

    def __init__(self, salary, name, emp_id):
        self.__salary = salary      # Private Variable
        self.name = name            # Public Variable
        self.emp_id = emp_id


    def get_salary(self):
        return self.__salary


    def set_salary(self, new_salary):

        if new_salary < 0:
            print("Salary cannot be negative!")

        else:
            self.__salary = new_salary
            print("Salary Updated Successfully!")


    @abstractmethod
    def calculate_bonus(self):
        pass


    def display(self):
        print("\n----------------------------")
        print(f"Company : {Employee.company}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Name : {self.name}")
        print(f"Salary : ₹{self.get_salary()}")


    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


    @staticmethod
    def is_valid_employee_id(emp_id):

        if emp_id.startswith("EMP") and emp_id[3:].isdigit():
            return True

        return False




class Developer(Employee):

    def __init__(self, salary, name, emp_id, language):


        super().__init__(salary, name, emp_id)

        self.language = language

    def calculate_bonus(self):

        bonus = self.get_salary() * 0.20
        print(f"Developer Bonus : ₹{bonus}")


    def display(self):


        super().display()

        print(f"Language : {self.language}")




class Manager(Employee):

    def __init__(self, salary, name, emp_id, team_size):

        super().__init__(salary, name, emp_id)

        self.team_size = team_size

    def calculate_bonus(self):

        bonus = self.get_salary() * 0.30
        print(f"Manager Bonus : ₹{bonus}")

    def display(self):

        super().display()

        print(f"Team Size : {self.team_size}")



dev = Developer(
    salary=50000,
    name="Ashmitha",
    emp_id="EMP101",
    language="Python"
)

mgr = Manager(
    salary=80000,
    name="John",
    emp_id="EMP201",
    team_size=12
)


dev.display()
dev.calculate_bonus()

mgr.display()
mgr.calculate_bonus()


dev.set_salary(60000)
dev.display()

print("\nTrying Invalid Salary...")
dev.set_salary(-1000)


print("Current Company :", Employee.company)

Employee.change_company("OpenAI Technologies")

print("Updated Company :", Employee.company)


dev.display()
mgr.display()


print(Employee.is_valid_employee_id("EMP101"))
print(Employee.is_valid_employee_id("EMP10A"))
print(Employee.is_valid_employee_id("ABC123"))


employees = [dev, mgr]

for emp in employees:
    emp.display()
    emp.calculate_bonus()
