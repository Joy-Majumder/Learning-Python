# # def sum(a,b) :
# #     s = a+b
# #     return s

# # x = sum(10,5)
# # print(x)

# # def noin():
# #     print("This is no return or anything")

# # noin()

# #  wap to print the len of the list

# lista = [1,2,3,4,56,"He"]



# # def lent(list):
# #     print(len(list))
# #     return list

# def lits(list):
#     for item in list:
#         print(item, end=" ")

# x = lits(lista)
# print()
# print(x)

def show(n):
    if n == 0 :
        return
    print(n)
    show(n-1)

show(5)