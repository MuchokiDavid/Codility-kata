def solution(a):
    #a is a list of numbers
    a.sort()
    b= [*set(a), ]
    s1=0
    s2= 0
    for i in range(len(b)+1):
        s2+=i #sum(a)
    for n in b:
        s1+=n
    return s1-s2
print(solution([1,2,5,6,8,3,8,6,7]))
