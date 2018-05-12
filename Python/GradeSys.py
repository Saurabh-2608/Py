# Program to Display grade acc to marks
i = int(input('Enter Marks(70 to 100) :'))
if i<=100 and i>=90:
	print('Grade O ')
elif i<=89 and i>=80:
	print('Grade E ')
elif i<=79 and i>=70:
	print('Grade A ')
else:
	print("Marks is not in given Range")		
