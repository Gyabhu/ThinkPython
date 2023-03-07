# WAP to check wether a string is an anagram

def anagram(a,b):
    c = a.lower()+b.lower()
    c = c.replace(" ","") #deepaklisten
    for i in c:
        d = c.count(i)
        if d % 2 ==0:
            return True

        return False

print(anagram("silent","listen"))