# Program to create a triangle with stars
n = int(input('Enter the no of rows : '))
for i in range(n):
	print(" "*(n-i),end="")   # Remove for loop to print space
	for k in range(i+1):      # Remove if(k<=i) by i+1 in for loop
		print("* ",end="")	
	print("\r")		