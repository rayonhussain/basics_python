Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> users=['A','B','C','D','E']
>>> #APPEND and INSERT
>>> users.append('F')
>>> print(users)
['A', 'B', 'C', 'D', 'E', 'F']
>>> users.insert('G')

>>> users.insert(0,'G')
>>> print(users)
['G', 'A', 'B', 'C', 'D', 'E', 'F']
>>> #Position
>>> users[-2]
'E'
>>> users[:2]
['G', 'A']
>>> #DEL and REMOVE
>>> del users[-1]
>>> print(users)
['G', 'A', 'B', 'C', 'D', 'E']
>>> users.remove('C')
>>> print(users)
['G', 'A', 'B', 'D', 'E']
>>> #LEN and FOR loop
>>> print(len(users))
5
>>> for user in users:
	print(user)

	
G
A
B
D
E
>>> #POP and SORT
>>> users.pop()
'E'
>>> users.pop(-1)
'D'
>>> users.pop(0)
'G'
>>> users.sort()
>>> print(users)
['A', 'B']
>>> users.sort(reverse=True)
>>> print(users)
['B', 'A']
>>> #copy of list
>>> copy_users=users[:]
>>> print(copy_users)
['B', 'A']
>>> 