''' Program to print pattern 
	1
	2 2
	3 3 3
	.
	.
'''
n = int(input("Enter the No.: "))	
for i in range(n):
	for j in range(n):
		if(j<=i):
			print(i,end="")
	print("\r")		