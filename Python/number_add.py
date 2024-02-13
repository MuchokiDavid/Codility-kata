#Cumurate sum
def cumurate_sum():
    try:
        number= int(input("Enter a number: "))
        # print(f"You entered {number}")
        sum= 0
        for num in range(0,number+1):
            sum= num+sum
        print(f"The sum is: {sum}")

    except:
        print("Enter a number")
cumurate_sum()