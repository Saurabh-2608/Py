'''
Created on 12-Jan-2018

@author: Chino Steve
'''
# Program to print Pattern
'''       1
        1 * 1
       1 * * 1
      1 * * * 1
'''
n = int(input("Enter the No.: ")) 
for i in range(n):
    print(" "*(n-i),end="")
    for k in range(i+1):
        if i==0 or k==0 or k==i:
            w = 1
        else:
            w = w*(i-k+1)//k
        if w == 1:
            print(w,end=' ')
        else:
            print('* ',end="")            
    print("\r")             