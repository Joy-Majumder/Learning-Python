# Comparisons :
# Equal : ==
# Not Equal : !=
#  Greater than : >
# Less than : <
# Greater or equal : >=
# Less  or equal : <=
# Object identity : is

user = "admin"
logged_in = False

# if user == 'admin' and logged_in == True:
#     print("Admin page broo")
# else:
#     print("Try again later")

if not logged_in:
    print("pls login.")
else:
    print("Hlell")

# lang = "Java"
#
# if lang == 'Python':
#     print("OK")
# elif lang == 'Java':
#     print("Matched")
# else:
#     print("Not ok")
a = 10
b = 10
print(a is b) # basically it actually works like == so nothing to say more bye

n = [1,2,3]
m = [1,2,3]

print(n == m) # true
print(f"Id of n is :{id(n)} and the id of m is : {id(m)}") # ouhoo at 'is' it checks actually the both value's id is same or not if same then True otherwise it will return false..v
print(id(n)==id(m)) # false
print(n is m) # false cause ouhoo at 'is' it checks actually the both value's id is same or not if same then True otherwise it will return false..v

