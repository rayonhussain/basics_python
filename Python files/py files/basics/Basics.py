Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Rayon")
Rayon
>>> a="Rayon"
>>> print(a)
Rayon
>>> #list
>>> a=[1,2,3,4]
>>> b=['Ray','Hus','Has']
>>> c=[]
>>> c.append('Num1')
>>> c.append('Num2')
>>> c.append('Num3')
>>> c
['Num1', 'Num2', 'Num3']
>>> c[-1]
'Num3'
>>> #IF statement
>>> if(c[0]=='Num3'):
	print("Position 1")
elif(c[1]=='Num3'):
	print("Position 2")
else:
	print("Position 3")

	
Position 3
>>> #FOR loop
>>> i=0
>>> for i in range(0,2)
SyntaxError: invalid syntax
>>> for i in range(0,2):
	print(c[i])

	
Num1
Num2
>>> for i in range(0,3):
	if(b[i])=='Has'):
		
SyntaxError: unmatched ')'
>>> for i in range(0,3):
	if b[i]=='Has':
		print(i)

		
2
>>> for i in range(0,3):
	if b[i]=='Has':
		print(i,b[i])

		
2 Has
>>> #DICTIONARIES
>>> d={'Name'='Rayon','Age'=24}
SyntaxError: invalid syntax
>>> d={'Name':'Rayon','Age':24}
>>> print(d)
{'Name': 'Rayon', 'Age': 24}
>>> print(Name)

>>> print('Name')
Name
>>> print(d['Name'])
Rayon
>>> print(d['Name'],d['Age'])
Rayon 24
>>> x_list=[1,2,3]
>>> x_dict={"A":x_list,"B":x_list}
>>> print(x_dict["A"])
[1, 2, 3]
>>> print(x_dict["A"][0])
1
>>> #GETTING INPUTS
>>> age=input("How old are you?")
How old are you?14
>>> print(age)
14
>>> pi=input("What is the value of PI?")
What is the value of PI?3.1454456
>>> type(pi)
<class 'str'>
>>> #DATATYPES
>>> type(c)
<class 'list'>
>>> type(pi)
<class 'str'>
>>> pi=int(pi)

>>> pi=float(pi)
>>> pi=int(pi)
>>> type(pi)
<class 'int'>
>>> print(pi)
3
>>> 