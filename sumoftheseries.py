x = int(input())
n = int(input())

sum = 0 
for i in range(1,n+1):
    power = 2*i-1 
    if i%2==0:
        sum = sum - x**power
    else:
        sum = sum + x**power
print(sum)