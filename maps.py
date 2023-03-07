b = ["a", "b", "c", "d"]

def caps_lock(char):
    return char.upper()

ans = list(map(lambda caps:caps.upper(), b))
ans2 = list(filter(caps_lock, b))
print(ans, ans2)
