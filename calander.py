import calendar
year = int(input("Enter The Year :"))
leap_year = calendar.isleap(year)
if leap_year:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")