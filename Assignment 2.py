def splited(a):
    strings = a.split("+")
    done = []
    for i in strings:
        s = i.strip()
        done.append(s)

    answer =" ".join(done)
    return answer

r = splited("Python + is + an + awesome + language")

print(r)
