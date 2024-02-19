# for i in range(5):
#     print('*'*i)
def soln(n):
    for i in range(1, n + 1):
        for j in range(i):
            print ("*")
        print
soln(5)