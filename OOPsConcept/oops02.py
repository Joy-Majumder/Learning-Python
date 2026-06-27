# # # del keyword
# # class Student:
# #     def __init__(self,name): 
# #         self.name = name # here name is the property(attribute)

# # s1 = Student("joy")
# # # del s1.name
# # # del s1  # by using del keyword we can delete whole class or we can even delete object of that class 

# # print(s1.name)

# # NOTE : private(like) attributes and methods
# # Private attributes and methods are meant to be used only within the class and are not
# # accessible fromt the outside of the class
# # 
# # class Acc:
# #     def __init__(self, no,acc_pass):
# #         self.ano = no
# #         self.__passwd = acc_pass # if i add __ before passwd that time its now private so yea

# #     def reset(self):
# #             print(self.__passwd)


# # acc1= Acc("2121", "asdsd")
# # acc1.reset()
# # print("Acc no : ",acc1.__passwd)

# # class Person:
# #     __name = "anon"

# #     def __hello(self): 
# #         print("Hello wrold")

# #     def welcome(self): # whenever we write a function ina class it called methods so yea
# #         self.__hello() # we can access these using another func within this class cause name is private so yea 

# # p1 = Person()
# # print(p1.welcome())


# #  NOTE : Inheritance :
# #  whne one class(child or derived) derives the properties and methods of another class(parent/base)

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self,brand):
#         self.name = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type
        

# # car1 = Toyota("benZ")
# # car2 = Toyota("BMW")
# # print(car1.name)
# # print(car1.color)
# # print(car2.name)
# # print(car2.color)

# car1 = Fortuner("diseal")
# car1.start()


# NOTE : multiple inheritance

# class A:
#     varA = "welcome to class a"

# class B :
#     varB = "Welcome to class b"

# class C(A,B):
#     varC = "Welcome to class c"


# c1 = C()
# # print(c1.varA)
# # print(c1.varB)
# print(c1.varC)


# super() method
#  is used to access methods of the parent class

# class Car:
#     color = "black"
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self,brand,type):
#         self.name = brand
#         super().__init__(type) # by using this we can call parent class property
#         super().start()

# car1 = Toyota("MSA", "elect")
# print(car1.type)


# class method
# a class method is bound to the class and receives the class as an implicit first arguement
# NOTE : static method cant access or modify class state and generally for utility


class Person:
    name = "anon"
    
    # def changeName(self, name):
        # self.name = name
        # self.__class__.name = name # by using this we also can accesss class method name
        # Person.name = name # by using this we can also change name of name also in class
    @classmethod # by using this we can change both class attribute name 
    def changeName(self, name): # NOTE: this is the best method of ding this! 
        self.name = name

p1 = Person()
p1.changeName("Joy")
print(p1.name)
print(Person.name)


# Property 
# We use @property decorator on any method in the class to use the method as a property!

class Student:
    def __init__(self, phy,che,math):
        self.ch = che
        self.math = math
        self.phy = phy
        # self.per = str((self.phy + self.ch + self.math)/3) + "%"

    # def cal(self):
    #     self.per = str((self.phy + self.ch + self.math)/3) + "%" 

    @property
    def perce(self):
        return str((self.phy + self.ch + self.math)/3) + "%"

st1 = Student(98,97,99)
print(st1.perce)

st1.phy = 89
# st1.cal()
print(st1.perce)

# NOTE : Polymorphism : Operator Overloading 
#  when the same operator is allowed to have diff meanings according to the context.
#  operators and Dunders functions
#  a+b # addition          a.__add__(b)
#  a-b # subtraction       a.__sub__(b)
#  a*b # multiplication    a.__mul__(b)
#  a/b # Division          a.__truediv__(b)
#  a%b # addition          a.__mod__(b)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shwNum(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self,num2): # now it become dunder func
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, number2):
        newReal = self.real - number2.real
        newImg = self.img - number2.img
        return Complex(newReal, newImg)
    
    def __mul__(self,number):
        newReal = self.real * number.real
        newImg = self.img * number.img
        return Complex(newReal, newImg)

cmplx1 = Complex(10,30)
cmplx2 = Complex(3,8)
cmplx1.shwNum()
cmplx2.shwNum()
print("Sum is :")
# num3 = cmplx1.add(cmplx2)
num3 = cmplx1 + cmplx2
num3.shwNum()
# now here is the substraction part
print("Substraction here : ")
num4 = cmplx1 - cmplx2
num4.shwNum()
# print(num3)
print("from here it does multiplication : ")
num5 = cmplx1 * cmplx2
num5.shwNum()
