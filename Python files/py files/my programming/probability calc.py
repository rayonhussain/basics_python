Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def mean(x):
	j=0
	n=len(x)
	y=0
	z=0
	while j<n:
		y=y+x[j]
		j=j+1
	z=y/n
	return z

>>> def median(x):
	n=len(x)
	if(n%2==0):
		y=x[int(n/2)-1]
	else:
		y=x[int((n+1)/2)-1]
	z=y
	return z

>>> 
>>> def variance(x):
	j=0
	n=len(x)
	y=0
	z=0
	while j<n:
		y=y+((x[j]-mean(x))**2)
		j=j+1
	z=y/(n-1)
	return z

>>> def std(x):
	z=(variance(x)**(1/2))
	return z

>>> def calc(num):
	i=0
	a=[]
	print("Enter the input numbers: ")
	for i in range (0,num):
		a[i]=int(input())
	print("Entered numbers are",a)
	print("Mean is ", mean(a))
	print("Median is ", median(a))
	print("Variance is ", variance(a))
	print("Standard Deviation is ", std(a))

	
>>> calc(4)
Enter the input numbers: 
10

>>> def calc(num):
	i=0
	a=[]
	print("Enter the input numbers: ")
	for i in range (0,num):
		a.append(int(input()))
	print("Entered numbers are",a)
	print("Mean is ", mean(a))
	print("Median is ", median(a))
	print("Variance is ", variance(a))
	print("Standard Deviation is ", std(a))

	
>>> calc(4)
Enter the input numbers: 
10
11
12
13
Entered numbers are [10, 11, 12, 13]
Mean is  11.5
Median is  11
Variance is  1.6666666666666667
Standard Deviation is  1.2909944487358056
>>> 