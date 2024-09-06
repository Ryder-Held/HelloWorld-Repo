'''
Ryder Held
9/6/2024

This program takes a humans age and translates it into a dogs age. This includes years, months, and days.
'''
#Basic Pythoid info
days_per_month = int(30)
days_per_year = int(360)
months = int(12)
years = int(1)

#30 days a month, 12 months a year

#Put your age here
human_age = float(input('Enter your age: '))

#Your age in dog
dog_age = human_age * int(7)

#Years in dog age
dog_years = dog_age // 1

#Months in dog age
reg_dog_months = dog_age % 1 * months
dog_months = dog_age % 1 * months // 1

#Days in dog age
dog_days = reg_dog_months % 1 * days_per_month // 1

print('Your age in dog years is ', dog_years, 'years', dog_months, 'months', dog_days, 'days')





'''
Ryder Held
9/6/2024

This program continues from the previous by taking a humans age and translates it into a cats age. This includes years, months, and days.
'''
#Basic Pythoid info
days_per_month = int(30)
days_per_year = int(360)
months = int(12)
years = int(1)

#30 days a month, 12 months a year

#Your age in cat
cat_age = human_age / int(9)

#Years in cat age
cat_years = cat_age // 1

#Months in cat age
reg_cat_months = cat_age % 1 * months
cat_months = cat_age % 1 * months // 1

#Days in cat age
cat_days = reg_cat_months % 1 * days_per_month // 1

print('Your age in cat years is ', cat_years, 'years', cat_months, 'months', cat_days, 'days')





'''
Ryder Held
9/6/2024

This program continues from the previous by taking a humans age and translates it into a horses age. This includes years, months, and days.
'''
#Basic Pythoid info
days_per_month = int(30)
days_per_year = int(360)
months = int(12)
years = int(1)

#30 days a month, 12 months a year

#Your age in horse
horse_age = 3 * (((human_age ** 2 - 47) / 7) + 12)

#Years in horse age
horse_years = horse_age // 1

#Months in cat age
reg_horse_months = horse_age % 1 * months
horse_months = horse_age % 1 * months // 1

#Days in horse age
horse_days = reg_horse_months % 1 * days_per_month // 1

print('Your age in horse years is ', horse_years, 'years', horse_months, 'months', horse_days, 'days')
