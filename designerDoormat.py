n, m = (int(i) for i in input().split())
k = []
for i in range(int(n/2)):
    j = i + (i+1)
    k.append(j)
    print(int((m - (3 * j)) / 2 ) * '-' + j * '.|.' + int((m - (3 * j)) / 2 ) * '-')
    
print(int((m-7) / 2) * '-' + 'WELCOME' + int((m-7) / 2) * '-')
k.reverse()
for j in k:
    print(int((m - (3 * j)) / 2 ) * '-' + j * '.|.' + int((m - (3 * j)) / 2 ) * '-')
