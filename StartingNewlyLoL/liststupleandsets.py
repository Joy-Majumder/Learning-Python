from operator import truediv

courses = ['Math','Physics','History']
# cou2 = [1,2,3,4]
# print(len(courses))
# print(courses[0]) # accessing through index brooo
#
# updated = courses[0].replace('Math','Bio')
#
# print(updated)
# print(courses[0:2]) # this will print 0,1 indexes bt not gonna print index 2 so yeap
#
# courses.append('Bio')
# courses.insert(0,'Biolody')
#
# courses_2 = ['art','education','se']
# # courses.insert(0,courses_2) # by this we can also add 2 lists together
#
# courses.extend(courses_2)# we shoudl use extend instead of insert
# # courses.remove('Math')
# popped = courses.pop()
# print(popped)
# print(courses)

# courses.reverse()
# courses.extend()
courses.sort()
# cou2.reverse()
# cou2.sort(reverse=True)
# print(sorted(cou2))
# print(cou2)
# print(sum(cou2))
# print(max(cou2))
# print(courses.index('Math'))

# print('Math' in courses)
# print('Matha' in courses)
#
# for item in courses :
#     if item=='Math':
#         print("Ok")
#     else:
#         print(item)
#
# for index, courses in enumerate(courses, start=2):
#     print(index,courses)

courses_str = ', '.join(courses)
new = courses_str.split(' - ')
print(new)
print(courses_str)

# tupple and sets also mind it that tuples are immutable bro they cant be change

tup = ('Hell', 'Hello')
tup2 = tup
# tup = tuple(courses)
print(tup2)
print(type(tup))


# Sets here brooooo

cs_courses = {'ICs', 'Statistics and probability', 'System design and analysis', 'Microcontroller'}
cs = cs_courses.union(courses)
print(cs)
print(type(cs_courses))
print(cs_courses.intersection(cs))

#  empty list tuples and lists

l1ist = []
list1= list()

tup = []
tup1 =tuple()

seee = {} # its actually a dict broo lol

see1 = set()
print(type(seee))
print(type(see1))