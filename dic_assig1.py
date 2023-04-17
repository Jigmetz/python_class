#I/P

# hellooo

#O/P

# {'h':1, 'e':1, 'l':2, 'o':1}

string = input("enter a string:")
dic = {}
max_char = ''
max_count = 1
for letter in string:
    if letter not in dic:
        dic[letter] = 1
    else :
        dic[letter] += 1
        if dic[letter] > max_count:
            max_count = dic[letter]
            max_char = letter

print({max_char:dic[max_char]})
        



# print(dic)/
