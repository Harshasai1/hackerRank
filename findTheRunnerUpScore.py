if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    ordered_list = sorted(arr)    
    print(ordered_list[-2])