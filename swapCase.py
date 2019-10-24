def swap_case(s):

    l, k = [], ''
    for i in s:
        l.append(i)
    for i in l:
        if i.islower():
            k = k + ''.join(i.upper())
        elif i.isupper():
            k = k + ''.join(i.lower())
        else:
            k = k + ''.join(i)
    return k