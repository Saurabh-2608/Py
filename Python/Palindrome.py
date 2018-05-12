# Program to check weather a no. is palindrome or not
import math
n = int(input('Enter the No.:'))
n1 = n
sum1 = 0
while (n>0):
	d = n%10
	sum1 = sum1 * 10 + d
	n = n/10
	n = round(n,0)
if(n1 == sum1):
	print(sum1,'palindrome')
else:
	print(sum1," Not palindrome")		