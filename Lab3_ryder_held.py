'''
Ryder Held
9/6/2024

This program caculates the amount of tax a person would pay in the year 2023 depending on their income and marital status
'''
#User enters income amount
earned_income = float(input('Enter the amount of income you earned in 2023: '))

print('Are you married or single?')

#user enters marital status
marital_status = input('Type m for married and s for single: ')

# Determines the taxes of a single person that makes at most $11000
if (0 <= earned_income <= 11000) and (marital_status == 's'):
	print('This year you owe', f'{(earned_income * 0.10):.2f}', 'in taxes')

# Determines the taxes of a single person that makes at most $44725
elif (11001 <= earned_income <= 44725) and (marital_status == 's'):
	print('This year you owe', f'{(11000 * 0.10) + ((earned_income - 11000) * 0.12):.2f}', 'in taxes')

# Determines the taxes of a single person that makes at most $95375
elif (44726 <= earned_income <= 95375) and (marital_status == 's'):
	print('This year you owe', f'{(11000 * 0.10) + ((44725 - 11000) * 0.12) + ((earned_income - 44725) * 0.22):.2f}', 'in taxes')

# Determines the taxes of a married person that makes at most $22000	
elif (0 <= earned_income <= 22000) and (marital_status == 'm'):
	print('This year you owe', f'{earned_income * 0.10:.2f}', 'in taxes')

# Determines the taxes of a married person that makes at most $89450
elif (22001 <= earned_income <= 89450) and (marital_status == 'm'):
	print('This year you owe', f'{(22000 * 0.10) + ((earned_income - 22000) * 0.12):.2f}', 'in taxes')
	
# Determines the taxes of a married person that makes at most $190750
elif (89451 <= earned_income <= 190750) and (marital_status == 'm'):
	print('This year you owe', f'{(22000 * 0.10) + ((89450 - 22000) * 0.12) + ((earned_income - 89450) * 0.22):.2f}', 'in taxes')
	
# If a person makes too much money, the program prints the following message
else:
	print('You made too much for this calculater. Hurray!')
