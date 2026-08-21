n = int(input())
if n%2 == 0 :
    print("even")
else:
    print("odd")
if n <= 1: 
    print("Not a prime number")
else:
    is_prime = True 
    for i in range(2,n):
        if n%i == 0:
            is_prime = False
if is_prime:
    print("prime number")
else:
    print("Not a prime number")