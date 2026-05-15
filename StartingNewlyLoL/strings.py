msg = "Hello'W'orld"

print("hello world")
print(msg[11]) # by this we are accessing index values
print(msg[0:9]) # by this we can access through range this is called slicing

print("The length is : ",len(msg), "And a type we are in :", type(msg))
print(msg.lower())
print(msg.upper())
print(msg.count('l')) # by using this we can found how many words has been used here lol
print(msg.find('Hello')) # if we cant find then it will return -1 as usual
avg = msg.replace('Hello', 'Bye')
print(avg)

n1 = "hello"
n2 = "Joy"
#msgg = n1 + " "+ n2
# print(msgg)

msgg = f'{n1} {n2.upper()}, Welcome here!'#.format(n1,n2) # by doing we can easily format broooo easy formatt we can do using f string brooo
print(msgg)

print(dir(msg)) # gives you all available attributes lol
print(help(str.lower)) # by this we can get help from it yayyyyy

