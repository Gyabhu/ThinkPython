# Filter.py

# filter(function, iterable) takes 2 Arguments

a = [1,2,3,4,5,6,7,8,9]

# def is_even(values): # return type should be bool
    #return values%2==0
    # if values%2==0:
    #     return True
    # return False

#print(is_even(9))
result = list(filter(lambda x : x % 2==0, a))
print(result)

vowels = ["a", "e", "i", "o", "u"]
chars = "g","a","b","c","d","e","i","o"

def is_vowel(char):
    return char in vowels

vowelss = list(filter(is_vowel, chars))
maps = list(map(is_vowel,chars))

print(vowelss,maps)