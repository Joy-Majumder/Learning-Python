# Dict is actually is Hashmaps
# also dict is mutable it means we can change values brooo
from jedi.inference.compiled import value

student = {'name': 'John', 'Age':25, 'Courses': ['math','Sci']} # the fomat is actually is first is key then value name is key and john is value so yeap
student['phone'] = '1234567890'
student['name'] = 'Joy'
print(student.get('name')) # we should use get method brooo if we passes something dont exist they will print None otherwise it will print value
print(student.get('phone'))

student.update({'name':'Johny','phone':'223232', 'Age':'23'})
del student['phone'] # by using del we can delete specific dict.
age = student.pop('Age') # by using this we can actually pop out a specific value from the dict. yayyyy
# keys
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    if key == 'name':
        print(f"The '{key}' is : '{value}'")
print(student)
