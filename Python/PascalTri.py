# program to print Pascal Triangle
import math
n = int(input('Enter the No.(0 to 9): '))
for i in range(n):
	print(" "*(n-i)*2,end="")
	for k in range(i+1):
		if i==0 or k==0:
			w = 1
		else:
			w = w*(i-k+1)//k
		if w<10:
			print(' ',end=" ")
		else:
			print(' ',end='')
		print(w,end=' ')		
	print("\r")		