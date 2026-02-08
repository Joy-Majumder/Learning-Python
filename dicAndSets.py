# Dictionary
# its a collection of key value pairs

# a = {
#     "Joy" : 100,
#     "Pritom" : 95,
#     "Rohan" : 45,
#     "List" : [1,2,3,4,5]
# }
# a["Joy"] = 2 # by using this we can mutate the value of a dict like we did here
# print(a)
# print(a["Joy"])

# print(a[0]) # we cant access values through index in dict bt we cann access by using a["Joy] it means it will present values of that Joy assigned
# print(a["Joy"]) # here prints 100
# We use dict for easy to lookup values

# marks = [["Joy",100],["Pritom",200],["Rohan",12]] # we can do list under list in python

# print(marks) # if we do list under list we cant not access value of Joy directly and if we write complex logics that will be computationally expensive so thats why we use dict for easy and not for that much expensive.
# print(list) # if we make a list under dict then if we write print(list) then it will prints its class type like list in output : <class 'list'>
# print(a["Joy"]) # it will prints its value
# print("List : ",a["List"]) # prints the value of list; [1,2,3,4,5]
# print(a,"\n",type(a))

# Properties of python dict
#  1. it is unordered
#  2. its mutable
#  3. its indexed
#  4. cant contain duplicate keys

# Dict Methods

a = {
    "Joy" : 100,
    "Pritom" : 95,
    "Rohan" : 45,
    "List" : [1,2,3,4,5],
    0 : "Joy"
}

# print(a.items()) # by using this we get key value pairs and we got it in tuple form ; dict_items([('Joy', 100), ('Pritom', 95), ('Rohan', 45), ('List', [1, 2, 3, 4, 5]), (0, 'Joy')])
# print(type(a.items())) # btw its an dict item, although we get in tuple form or whot : <class 'dict_items'>
# print(a.keys()) # by using this function we get only keys of a dict like : dict_keys(['Joy', 'Pritom', 'Rohan', 'List', 0])
# print(a.values()) # By using this function we get only values of a dict not keys just values only like : dict_values([100, 95, 45, [1, 2, 3, 4, 5], 'Joy'])
# print(a.get("Joy")) # By using this function we can get values of any dict keys like a.get("Key_name") // value we get in output
# print(a.pop("Joy")) # Using this function we can popout that key with value from a dict
# # print(a.clear()) # this will clear the whole dict lol
# print(a.update({"Friends": 90})) # by using this function we can update in a dict like we did here! like : {'Pritom': 95, 'Rohan': 45, 'List': [1, 2, 3, 4, 5], 0: 'Joy', 'Friends': 90} we can see that here added friends with value 90
# print(a.copy()) # By using this function we can copy a dict lol in copy function there will be no arg.

# Whats the diff between a.get("Joy") and a["Joy"]
# print(a.get("Joy2")) # if we change Joy to Joy2 then it will give us means prints None
# print(a["Joy2"]) # in the other hand if we change here it will give use keyErr like this is not exists like : KeyError: 'Joy2'

# print(a)

#  Sets in python

# set is a collection of non-repetitive elements
# it means there no repetition allowed in sets

# d = {} # it will make empty dict

# print(type(d)) # this is dict
# set1 = {1,2,3,4,5} # we can make sets like this other wise we can make sets with set() s.add(1) this will make a set like {1,2} and so on!
# print(set1)
# s = set() # this is an empty set then we can add using func add to add in empty set
# s.add(1)
# s.add(2)
# print(s) # set {1,2}
# a = {1,2,2,3,4,4,5,6} # this will not gonna print repeated values , it will print only all values once not multiple times, also if we need ordered version then we need to use lists rather than set.

# print(a)

# PROPERTIES OF SETS in python
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# Set methods and OPERATIONS ON SETS in python

s = {1,2,3,4,5,"Joy"} # we can also add str in set and its type will be same as set
# s.add("Asa") # we can also add in a set using add function
# print(s.copy()) # we can copy through using copy function in set of python
# print(s.remove("Joy")) # by using this function we can remove any element from the set
# print(s.pop()) # This pop function does not have any specific order to popout elements its remove randomly
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# print(B.difference(A)) # by using this function we usually do (a-b) in set! A.difference(B) means A-B in set
# print(A.union(B)) # By using this we can do union with both sets in python
# print(s,s.discard("Joy")) # we do remove Joy using this function discard function
# print(A.intersection(B)) # Using this function it does take "common in all sets"
# print(A.issubset(B)) # false cause 1,2,3,4 is not available in B thats why it returns false if elements of A exists in B set then it will return True
# print(A.intersection(B)) # Elements of A should available in B set like : 3 and 4 are present in both sets.
# print(A.isdisjoint(B)) # There should No common elements in sets
# print(A.issuperset(B)) # issuperset() checks whether A set contains all elements of another set. A contains all elements of B
# A.difference_update(B) # difference_update() removes all elements from the original set that are also present in another set (or sets).3 and 4 are in both sets → removed from A 1 and 2 remain
# print(A)
# print(len(a)) # By using this len() function we can find length of the set
print(s, type(s))
