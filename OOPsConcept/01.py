# creating a class : also it is a blueprint for creating a object!
class Student:

    # default constructors
    # def __int__(self):
    #     print("Hello world")
    
    #  parameterized contructors
    college_name = "UIU"
    name = "Anon" # this is class attr
    def __init__(self,fullname, marks):
        self.marks = marks
        self.name = fullname # object attr > class attr
        print("Creating data for database\n")
        # print(self) # self and object named s1 boths addresses are same
    
    def hola(self): # this is methods
        print("Hello Student", self.name)

    def get_marks(self):
        return self.marks
    
    # static methods -> that dont use the self parameter(work at class level)
    @staticmethod #decorator
    def welcome():
        print("Welcome to UIU")

    # name = input("Enter Your name : ")
    # if len(name)>0:
    #     print(name)
# creating object (instance)
s1 = Student("Joy Majumder", 34)
# s1.hola()
s1.hola()
s1.welcome()
print(s1.get_marks())
print(s1.name, s1.college_name, s1.marks, Student.name)
# s2 = Student("Pial")
# # print(s2.name, s2.college_name)
# print(Student.college_name)


# there are four phillars of OOPs so those are 
#  1. Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user
#  2. Encapsulation -> wrapping data and function into a single unit (object)
#  3. inheritance
#  4. Polymorphism
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clch = False

    def start(self):
        self.clch = True
        self.acc = True
        print("Car started") # this is abstraction cause we hide unneccery things
car1 = Car()
car1.start()
