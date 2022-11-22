# function to reverse string and check if it's a palindrome
def is_palin(string):
    # make the string lowercase
    string = string.lower()
    # splits the string into a list of characters and symbols
    slist = list(string)
    # give i a value of 0
    i = 0
    # check each character in the list
    for ch in slist:
        # if character is an alphabet, nothing happens
        if ch.isalpha():
            pass
        # if character is not an alphabet, replace the value with nothing
        else:
            slist[i]=''
        # increment i by adding 1
        i=i+1
        # end of for loop, returns new list with no symbols or spaces
        return slist
    # joins the new list and saves as backwards string
    word = "".join(slist)
    print(word)
    backward = "".join(reversed(slist))
    print(backward)
    return backward == word


def is(word):
    word = word.lower()
    slist = list(word)
    i = 0
    for ch in slist:
        if ch.isalpha():
            print('')
        else:
            slist[i] = ''
        i = i+1
        return slist
    neword = "".join(slist)
    print(neword)
    backwards = reverse(word)
    print(backwards)
    if backwards == neword:
        print("yes")
    else:
        print('no')


is_palin("Go hang a salami I'm a lasagna hog")
