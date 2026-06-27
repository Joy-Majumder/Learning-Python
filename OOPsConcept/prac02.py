class Circle:
    # global pi 
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return self.pi * self.radius ** 2
    
    def parameter(self):
        return 2* self.pi * self.radius

c1 = Circle(21)
print(c1.Area())
print(c1.parameter())

class Employee:
    def __init__(self,role, dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def shwDetails(self):
        print("Role = ", self.role)
        print("Dept = ", self.dept)
        print("Salary = ", self.salary)

class Engr(Employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.sal = salary
        super().__init__("Engr", "IT", "100000")
print("Hello world first")
e1 = Employee("Cse Engr.", "IT sector", "1,000,000")
e1.shwDetails()
print("Hello world Second")
eng1 = Engr("Elon Mask", 23, "232")
eng1.shwDetails()

class Order: 
    def __init__(self,iteam, price):
        self.iteam = iteam
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("Chips", 20)
order2 = Order ("Banana", 15)
print(order1 > order2) # if does this yayyy