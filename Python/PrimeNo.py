# Program to find prime no. between 1 to 20

for i in range(2,21):
	count = 0
	for j in range(1,21):
		if(i%j==0):
			count = count + 1			
	if(count == 2):
		print(i,' is a prime no.')
	else:
		print(i,' is not a prime no.')			