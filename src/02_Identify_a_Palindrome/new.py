str = "whales? -i"

def wording(string):
    string = string.lower()
    slist = list(string)
    i = 0
    for ch in slist:
        if ch.isalpha():
            print(f'{i} good')
        else:
            print(f'{i} bad')
            slist[i] = ''
        i = i+1
        return slist
    x = "".join(slist)
    print(x)
    backwards = "".join(reversed(slist))
    print(backwards)
    return backwards


