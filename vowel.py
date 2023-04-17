string = input("enter aa word : ").lower()
result = []
vowels = ('a','e','i','o','u')
for letter in string:
    if letter in vowels:
        result.append(letter)
print(result)