# Initializing a Dictionary

# Empty Dictionaries

# d = {}

# d = dict()

# Dictionary with Value

# d = {'t':50}

# Printing values from the Dictionary

# print(d['t'])
# print(d['t'])

d = {'username':'john','password':'john@0012'}
#print(d['username'], d['password']) 

username = input("enter username:")
password = input("enter your password:")
# if username == d['username'] and password == d['password']:
#     print('welcome')
# elif username != d['username']:
#     print('enter valid username')
# elif username == d['username'] and password != d['password']:
#     print('enter correct password')
if username == d['username']:
    if password == d['password']:
        print('welcome,logged in!')
    else :
        print('enter correct password')
else :
    print('enter correct username ')
    