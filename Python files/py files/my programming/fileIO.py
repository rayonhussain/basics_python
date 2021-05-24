Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file_name='textIO.txt'
with open(file_name) as obj:
	lines=obj.readlines()
for line in lines:
		print(line)
		
>>> with open(file_name, 'w') as obj:
	obj.write("New Line 2")

	
10
>>> with open(file_name, 'a') as obj:
	obj.write("\n Appending New Line")

	
20
>>> 