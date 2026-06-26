# f = open("sample.txt", "r")
# f = open("sample.txt", "w")
# f = open("sample.txt", "a")
# f = open("sample.txt", "r+")
# f.write("\n>_<")
# data = f.read(5)
# data  = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()

# # with syntax
# with open("sample.txt", "a") as f:
#     data = f.write(" Hello World")
#     print(data)

# with open("demo.txt", "w") as a:
#     data = a.write("Hello")
#     print(data) # it prints the character len

# Deleting a file 
# using os module

# import os as o
# a = o.getcwd()
# print(a)
# # o.remove("sample.tx")

def chck():
    word = "Hello"
    with open("demo.txt", "r") as a:
        data = a.read()
        # if (data.find(word) != -1):
        if (word in data != -1):
            print("Found")
        else : 
            print("Not found")

def chckline():
    word = "Hello"
    data = True
    line_no = 1
    with open("demo.txt", "r") as a:
        while data:
            data=a.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1

chckline()