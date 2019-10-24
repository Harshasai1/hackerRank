# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
n_array = input().split()
A = set(input().split())
B = set(input().split())


print(sum((ele in A) - (ele in B) for ele in n_array))
