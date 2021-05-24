Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Rayon")
Rayon
>>> arr1=[1,2,3,4,5,6,7]
>>> i=0
>>> while(i<7):
	print(arr1[i])
	i=i+1

	
1
2
3
4
5
6
7
>>> while(i<7):
	arr1[i]=arr1[i]**2
	print(arr1[i])
	i=i+1

	
>>> print(arr1)
[1, 2, 3, 4, 5, 6, 7]
>>> i=0
>>> while(i<7):
	arr1[i]=arr1[i]**2
	print(arr1[i])
	i=i+1

	
1
4
9
16
25
36
49
>>> print(arr1)
[1, 4, 9, 16, 25, 36, 49]
>>> i=1
>>> while i<7:
	arr1[i-1]=arr1[i]+(arr1[i-1]**2)
	print(arr1[i-1])
	i=i+1

	
5
25
97
281
661
1345
>>> 