number = int(input("Enter a number: "))

def time_convert(num):
    x= num%60
    y= int(num/60)
    return f'{y}:{x}'
print(time_convert(number))