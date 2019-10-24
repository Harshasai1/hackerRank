
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
credit_cards = [input() for i in range(n)]
        
for card in credit_cards:
    z = card.split('-')
    if (int(card[0]) in [4, 5, 6]):
        if len(z) == 1:
            temp = []
            t = z[0]
            l = 0
            for i,x in enumerate(z[0]):
                temp.append(x.isdigit())
                if i == 0:
                    pass
                else:
                    if x == t:
                        l += 1
                        t = x
                    else:
                        if l >= 3:
                            t = x
                        else:
                            l = 0
                            t = x
            
            if all(temp) and (l < 3) and (len(card) == 16):
                print("Valid")
            else:
                print("Invalid")
        elif len(z) == 4 and (all([len(i) == 4 for i in z])):
            temp = []
            l = 0
            for i in z:
                t = i[0]
                for j, x in enumerate(i):
                    temp.append(x.isdigit())
                    if j == 0:
                        pass
                    else:
                        if x == t:
                            l += 1
                            t = x
                        else:
                            if l >= 2:
                                t = x
                            else:
                                l = 0
                                t = x
                                
            if all(temp) and (l < 2):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
        
                        
                    
                
                
                
            
