def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return( str(year) + " is not a leap year. ")
        else:
            return( str(year) + " is a leap year. ")