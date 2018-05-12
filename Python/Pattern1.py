# Program to print triangle fo nos.
n = int(input('Enter the no. of Row :'))
for i in range(n):
	c = 0
	for j in range(n):
		if(j<=i):
			c = c + 1
			print(c,end="")
	print("\r")		
	
