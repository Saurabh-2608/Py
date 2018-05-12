''' Program to print pattern 
	1
	2 2
	3 3 3
	.
	.
'''
n = int(input("Enter the No.: "))	
for i in range(1,n+1):
	for j in range(1,n+1):
		if(j<=i):
			print(i,end="")
	print("\r")		