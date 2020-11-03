s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
for vowel in vowels:
    num_vowels+=s.count(vowel)
print(num_vowels)
