Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> b=[]
>>> for x in range(10):
	a.append(x)

	
>>> for y in range(1,100):
	b.append(y)

	
>>> #INBUILT functions
>>> b_max=max(b)
>>> b_min=min(b)
>>> b_sum=sum(b)
>>> print(b_max,b_min,b_sum)
99 1 4950
>>> 
>>> #simplified for loop
>>> squares=[x**2 for x in range(1,15)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
>>> 
>>> #UPPER and LOWER
>>> str1=['ABC','abc','AbC']
>>> names=str1[:]
>>> str_upper=[]
>>> str_upper2=[]
>>> for name in names:
	str_upper.append(name.upper())

	
>>> print(str_upper)
['ABC', 'ABC', 'ABC']
>>> for x in range(0,len(str1)):
	str_upper2.append(str1[x].upper())

	
>>> print(str_upper2)
['ABC', 'ABC', 'ABC']
>>> 
>>> #TUPLES
>>> dimension=(220,1540)
>>> 
KeyboardInterrupt
>>> dimensions=(220,1540)
>>> for dimension in dimensions:
	print(dimension)

	
220
1540
>>> #overwriting tuples
>>> dimensions=(1000,1330)
>>> for dimension in dimensions:
	print(dimension)

	
1000
1330
>>> 