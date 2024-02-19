#Find the missing element

def solution(a):
    arr_len= len(a)
    for i in range(1,arr_len+1):
        if (i not in a):
            return i

print(solution([1,3,4,5,6])) # should return 2