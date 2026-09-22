import math
x = int(input("Enter the value of x: "))

def dy_dx(x):
    return 2*x

def dz_dx(x):
    return 2*x*math.cos(x**2)

z = dy_dx(x)*dz_dx(x)
print(f"The value is : {z}")