def is_leap_year(year):
    # if mod of 100 is 0 & mod 400 does not equal 0 return false
    # return false if mod 4 is not 0, else return true
    if((year % 100 == 0) and (year % 400 != 0) or (year % 4 != 0)):
        return False
    return True
