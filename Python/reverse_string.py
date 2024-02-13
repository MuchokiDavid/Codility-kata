def reverse(str):
    words= []
    split_str= str.split()
    join_str= ' '.join(split_str[::-1])
    words.append(join_str)
    return words

str= "at be cat dog"
print(reverse(str))