#
# def hello_func(a):
#     for a in '110':
#         print(a)
#
# a = 1
# hello_func(a)
from StartingNewlyLoL.liststupleandsets import courses


# def a(greeding,name):
#     return '{}, {} Function'.format(greeding,name)


# print(a('Hello',name='Joy'))
# def stu(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# stu('math', 'art', name='Joy', age=23) # here 'math', 'art' is args and name gae is kqargs

ca = ['math','art']
info = {'name':'Joy', 'age':23}

def st(*ca,**info):
    print(ca)
    print(info)