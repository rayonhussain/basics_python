Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DICTIONARY
>>> #Dictionaries are key value pairs
>>> human={'features':'eyes','scope':'intelligence'}
>>> human_features=human['features']
>>> human_scope=human['scope']
>>> print(human_features,human_scope)
eyes intelligence
>>> alien={}
>>> alien['x']='Ray'
>>> alien['y']='Hus'
>>> print(alien)
{'x': 'Ray', 'y': 'Hus'}
>>> alien[1]=True
>>> alien[0]=False
>>> alien[2]='X'
>>> print(alien)
{'x': 'Ray', 'y': 'Hus', 1: True, 0: False, 2: 'X'}
>>> 
>>> #updation and deletion
>>> alien[2]='None'
>>> print(alien[2])
None
>>> del alien[2]
>>> print(alien)
{'x': 'Ray', 'y': 'Hus', 1: True, 0: False}
>>> users={1:'A',2:'B',3:'C',4:'D',5:'E'}
>>> for userid,name in users.items():
	print(userid +" : " +name)

	

>>> for userid,name in users.items():
	print(userid ," : " +name)

	
1  : A
2  : B
3  : C
4  : D
5  : E
>>> for userid in users.keys():
	print(userid)

	
1
2
3
4
5
>>> for name in users.keys():
	print(name)

	
1
2
3
4
5
>>> for name in users.values():
	print(name)

	
A
B
C
D
E
>>> 