# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is : ", sum/len(self.marks))

# s1 = Student("Joy", [99, 23, 10])
# s1.name = "Pial"
# s1.get_avg()

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clch = False

#     def start(self):
#         self.clch = True
#         self.acc = True
#         print("Car started")

# car1 = Car()
# car1.start()

class Acc:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc = acc

    # debit
    def debit(self,ammount):
        self.balance -= ammount
        print("Tk.", ammount, "was debited")
        print("Total ammount left : ",self.get_bal())
    # credit
    def credit(self,ammount):
        self.balance += ammount
        print("Tk.", ammount, "was credited")
        print("Total ammount : ",self.get_bal())

    def get_bal(self):
        return self.balance

acc1 = Acc(5000, 696969)
acc1.debit(1000)
acc1.credit(500)
print("acc balance is :",acc1.balance,"\n","Account No : ",acc1.acc)