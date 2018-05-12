# Program to print Diamond with Stars
n = int(input("Enter the no. rows :"))
mid = n/2
mid = int(mid)
for i in range(mid):
	for j in range(n-i):
		print(" ",end="")
	for k in range(n):
		if(k<=i):
			print("* ",end="")
	print("\r")			
for i1 in range(mid+1,n+1):
	for j1 in range(i1):
		print(" ",end="")
	for k1 in range(n,mid,-1):
		if(k1>=i1):
			print("* ",end="")
	print("\r")		