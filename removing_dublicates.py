n = int(input())
lists = []
for i in range(n):
    k = list(map(int,input().split()))
    if len(k) == len(set(k)):
        lists.append(k)
print(lists)
