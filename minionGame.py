def minion_game(string): 
    s, k = 0, 0
    for n, i in enumerate(string):
        if i in ['A', 'E', 'I', 'O', 'U']:
            k = k + (len(string) - n) 
        else:
            s = s + (len(string) - n) 

    if s > k:
        print('Stuart', s)
    elif s < k:
        print('Kevin', k)
    else:
        print('Draw')
                