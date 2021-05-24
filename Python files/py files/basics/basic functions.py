Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #FUNCTIONS
>>> def shop_order()
SyntaxError: invalid syntax
>>> def shop_order():
	print("Shop order")

	
>>> shop_order()
Shop order
>>> def shop_order('Tablet'):
	
SyntaxError: invalid syntax
>>> def shop_order("Tablet"):
	
SyntaxError: invalid syntax
>>> def shop_order(shop_product):
	print("Do u need "+ shop_product)

	
>>> shop_order("Tablet")
Do u need Tablet
>>> def shop_order(shop_product + 'xtra'):
	
SyntaxError: invalid syntax
>>> def shop_order(shop_product='Randomized'):
	print("Do u need "+shop_product)

	
>>> shop_order()
Do u need Randomized
>>> shop_order("IPhone")
Do u need IPhone
>>> def update_shop_list(num_of_products,product):
	n=input("How many new items?")
	for i in range (1 to n):
		
SyntaxError: invalid syntax
>>> def update_shop_list(num_of_products,product[]):
	n=input("How many new items?")
	i=0
	while i<n:
		product[i]=input()
		i=i+1

		
SyntaxError: invalid syntax
>>> def update_shop_list(num_of_products,product_category):
	n=input("How many new items?")
	i=0
	while i<n:
		product[i]=input()
		i=i+1

		
>>> def update_shop_list(num_of_products,product_category):
	n=input("How many new items?")
	i=0
	while i<n:
		product[i]=input()
		i=i+1
	shop_dict={product_category:product}

	
>>> update_shop_list(5,"Accessories")
How many new items?5

>>> def update_shop_list(num_of_products,product_category):
	n=num_of_products
	i=0
	while i<n:
		product[i]=input()
		i=i+1
	shop_dict={product_category:product}

	
>>> update_shop_list(5,'Accessories')
Pen

>>> type (product)

>>> def update_shop_list(num_of_products,product_category):
    n=num_of_products
    i=0
    product = []
    print("Enter your list:")
    while i<n:
        product.append(input())
        i=i+1
    shop_dict={product_category:product}
    print(shop_dict)
    update_shop_list(5,"Acc")
    











	

