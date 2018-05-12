# Program to print triangle with nos. as in pattern 2
n = int(input(" Enter the no. of rows : "))
for i in range(n):
	count = 0
	for j in range(n-i):
		print(" ",end="")
	for k in range(n):
		if(k<=i):
			count = count + 1
			print(count,"",end="")
	print("\r")			