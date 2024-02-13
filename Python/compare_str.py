def longestCommonSubsequence(text1: str, text2: str) -> int:
    txt1= text1.split(", ")
    txt2= text2.split(", ")
    print(txt1)
    # txt3= set(txt1)
    # txt4= set(txt2)
    # return txt3 & txt4
    
strg= longestCommonSubsequence('abcde', 'abdkef')
print(strg)