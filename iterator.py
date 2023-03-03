names = ["labs","gyabhs","dada_don"]
name = iter(names)

print(next(iter(name)))
print(next(iter(name)))
print(next(iter(name)))

strings = "IamGroot"
string = iter(strings)
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))
print(next(iter(string)))


# for loop using a while loop XD
# unconventional variable naming XD
namaiwa = ["luffy", "zoro"]
namaiwo = iter(namaiwa)

while True:
    try:
        namaiwas = next(namaiwo)
        print(namaiwas)
    except StopIteration:
        break