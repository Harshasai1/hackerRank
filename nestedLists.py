if __name__ == '__main__':
    s_list, scores, s = [], [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s_list.append([name, score])
    for i in s_list:
        if i[1] not in scores:
            scores.append(i[1])
    scores.sort()
    s_list.reverse()
    for i in s_list:
        if scores[1] == i[1]:
            s.append(i[0])
    s.sort()
    for i in s:
        print(i)