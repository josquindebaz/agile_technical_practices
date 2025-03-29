def leap_year(year):
    if year % 4 or (not year % 100 and year % 400):
        return False

    return True
