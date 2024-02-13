def count(number):
    numbers= []
    while number>0:
        numbers.append(number)
        number=number-1
    # print(numbers)
    for num in sorted(numbers):
        print (num)
   

number= int(input("Enter a number: "))
count(number)