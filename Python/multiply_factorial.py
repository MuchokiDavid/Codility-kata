def factorial(num):
    if num == 0:
        return 1;
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact

try:
    while True:
        num= int(input("Enter number: "))
        print(factorial(num))
except:
    print("\nError! Please enter a valid number.")