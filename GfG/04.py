# thisDict = {
#     "Name": "Joy",
#     "Sex" : "Male",
#     "age": 23,
#     "age": 24, # this will overwrite the age with before one so uea print 24 haah
#     "colors" : ["red","blue","green"]
# }

# print(type(thisDict["colors"]))

# so we can build dic with this also so here 

this = dict(name = "Joy", age = 23, Uni = "uiu")
# x = this.get("name")
# x = this.values()
# x = this.items()
# print(x)
print(type(this))

for x in this :
    if "Uni" in x :
        print(x)

# this["age"] = 24 # by doing this we can change age values from the dict
this.update({"age" : 24}) # correct way of doing this so we should follow this btw hehehe
# this.pop("age")
# this.popitem() # it will delete items from the last hehe 
# del this["age"] # we can do this also to delete data and value from the dict
# this.clear() # by doing this we can clear whole dict cleared
print(this,"\n")

for y in this.values() :
    print(y) # by doing we can print values only heheh

print("\n")

for x in this.keys() :
    print(x)


day = int(input("Enter the value here : "))

# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("Monday")
#     case 4:
#         print("Tuesday")
#     case 5:
#         print("Wednesday")
#     case 6:
#         print("Thursday")
#     case 7:
#         print("Friday")
#     case 8:
#         print("Stat")
#     case _: 
#         print("Invalid")

while day < 10:
    print(day)
    if day == 3:
        print("You have entered 3 so broke here")
        # break
        continue
    day += 5