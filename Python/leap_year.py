#Own generated----------------------------------------------------------------------
def is_leap(year):
    """Check if the current year is a leap year or not. """
    # A leap year is divisible by 4, but not divisible by 1
    # If it's divisible by 100, then it must also be divisible by 4
    leap= False
    if(year%4==0):
        divide= int(year/100)
        # print(divide)
        if(divide%4==0 and year%4==0):
            leap= True
            return leap
        else:
            return leap
    else:
        return leap
while True:
    year= int(input("\nEnter year: "))
    print(is_leap(year))

# AI Answer---------------------------------------------------------------------------
    
# def is_leap(year):
    """Check if the given year is a leap year or not.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# while True:
#     try:
#         year = int(input("\nEnter year: "))
#         if year <= 0:
#             print("Please enter a positive integer.")
#             continue
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

# print(is_leap(year))