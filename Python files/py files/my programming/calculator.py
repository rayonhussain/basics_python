Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x1,x2):
	return x1+x2

>>> def sub(x1,x2):
	return x1-x2

>>> def mul(x1,x2):
	return x1*x2

>>> def div(x1,x2):
	return x1/x2

>>> def calculator():
	print("Enter the two numbers")
	a=float(input("First number: "))
	b=float(input("Second number: "))
	print("Methods Available:")
	print("1. Addition")
	print("2. Subraction")
	print("3. Multiplication")
	print("4. Division")
	choose_option=int(input("Choose Option: "))
	if(choose_option==1):
		print("Addition of ",a," and ",b, " is " ,add(a,b))
	elif(choose_option==2):
		print("Addition of ",a," and ",b, " is " ,sub(a,b))
	elif(choose_option==3):
		print("Addition of ",a," and ",b, " is " ,mul(a,b))
	elif(choose_option==4):
		print("Addition of ",a," and ",b, " is " ,div(a,b))
	else:
		print("Invalid Input")

		
>>> calculator()
Enter the two numbers
First number: 10
Second number: 15
Methods Available:
1. Addition
2. Subraction
3. Multiplication
4. Division
Choose Option: 
None1
Addition of  10.0  and  15.0  is  25.0
>>> 
