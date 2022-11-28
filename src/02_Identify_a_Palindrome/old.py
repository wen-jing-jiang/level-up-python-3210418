def wordingfor(string):
    string = string.lower()
    slist = list(string)
    i = 0
    for ch in slist:
        if ch.isalpha():
            print(f'{i} good')
        else:
            print(f'{i} bad')
            slist[i+1] = ''
        i = i+1
        return slist
    fixed = "".join(slist)
    print(fixed)
    return fixed


def is_palindrome(string):
    forw = wordingfor(string)
    back = wordingback(string)
    if forw == back:
        print("yes")
    else:
        print("no")
