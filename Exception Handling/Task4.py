
def get_vowels(v):
    vowels = 'a','e','i','o','u'
    if len(v.strip())>1:
        return 'Must be char'
    elif v.isnumeric():
        return 'Cannot be integer'
    elif v.lower().strip() in vowels:
        return 'Vowel'
    else:
        return 'constant'

v = input("Enter char: ")

print(get_vowels(v))
