Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello world!')
hello world!
>>> print('hello'*10)
hellohellohellohellohellohellohellohellohellohello
>>> name= input('enter your name:')
enter your name:Aakancha
>>> age= input('enter your age:')
enter your age:print('your name is' + name + "and age is" + age)
>>> print('your name is {} and age is {}'.format(name,age))
your name is Aakancha and age is print('your name is' + name + "and age is" + age)
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a= input('enter the age')
enter the age18
>>> int (a)
18
>>> print(bool(x))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(bool(x))
NameError: name 'x' is not defined
>>> x= True
>>> print(bool(x))
True
>>> x= 3
>>> y=4
>>> print(x/y)
0.75
>>> print(x//y)
0
>>> print(x%y)
3
>>> 
