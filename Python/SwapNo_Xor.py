# Swap no. using XOR
n = int(input("Enter the No.1: "))
n1 = int(input("Enter the No.2: "))
n = n ^ n1
n1 = n ^ n1
print(n1)
n = n ^ n1
print(n)

