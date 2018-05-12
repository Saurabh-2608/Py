# Program to generate a  fibonacci series 1 1 2 3 5 8 ......
i = int(input("Enter the No.:"))
if i<0:
    print("Error :: User enter -ve No. ")
elif i==0:
    print("Error :: User enter 0 ")    
else:
    if i==1:
        print(0)  
    elif i==2:
        print(0)  
        print(1)
    else:
        print(0)  
        print(1)
        sum1 = 0
        y = 0
        z = 1
        for x in range(i-2):
            sum1 = y + z
            y=z
            z=sum1
            print(sum1)