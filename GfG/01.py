# chck even or odd number

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False

num = int(input())
isEven(num)
print(isEven(num))
