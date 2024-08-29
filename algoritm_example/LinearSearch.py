class Employee:
    def __init__(self, employee_id, first_name, last_name, birth_date, hire_date, salary):
        self.EmployeeID = employee_id
        self.FirstName = first_name
        self.LastName = last_name
        self.BirthDate = birth_date
        self.HireDate = hire_date
        self.Salary = salary

    def display(self):
        print(f"ID: {self.EmployeeID}")
        print(f"First Name: {self.FirstName}")
        print(f"Last Name: {self.LastName}")
        print(f"Birth Date: {self.BirthDate}")
        print(f"Hire Date: {self.HireDate}")
        print(f"Salary: {self.Salary}")


emp = Employee(1, "John", "Doe", "1995-01-24", "2018-09-03", 50000.00)
# emp.display()


def linear_Search(list, n, key):
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1


list = [1, 3, 5, 4, 7, 9, 15, 26, 18, 23]
key = 26

n = len(list)
res = linear_Search(list, n, key)
if (res == -1):
    print("Element topilmadi")
else:
    print("Element indeksi: ", res)
