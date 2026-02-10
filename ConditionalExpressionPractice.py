# 01

# b = int(input('Enter the first number: '))
# a2 = int(input('Enter the second number: '))
#
# if b > a2:
#     print(f"a1 is grater than a2 : {b} ")
# elif b == a2:
#     print(f"a1 is equal of a2 : {b} ")
# else:
#     print(f"a1 is less than a2 ")

# 02

p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = 'Have this'
p4 = "Get it now"

msg = input("Enter your message: ")

if p1 in msg or p2 in msg or p3 in msg or p4 in msg :
    print(f"You have entered the message is : {msg}")
else:
    print("U didnt enter the correct message")