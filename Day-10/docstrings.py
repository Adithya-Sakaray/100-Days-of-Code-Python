def is_leap(year):
  #the docstring should be the written immediately after the function name and it should be enclosed in 3 quotes.
  """ Takes a year and returns a bool based on leap year or not
  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    #the docstring should be the written immediately after the function name and it should be enclosed in 3 quotes.
    """Takes year and month as input and returns the number of days in that month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if(is_leap(year)):
        return month_days_leap[month-1]
    else:
        return month_days[month-1]
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







