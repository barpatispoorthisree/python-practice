D = input() 
N  = int(input())

if D == "Monday" :
    x = 0 
elif D == "Tuesday" :
    x =  1
elif D == "Wednesday" :
    x = 2
elif D == "Thursday" :
    x = 3
elif D == "Friday" :
    x = 4
elif D == "Saturday" :
    x = 5
elif D == "Sunday" :
    x = 6

x = (x + N - 1)% 7

if x == 0 :
    print("Monday")
elif x == 1 :
    print("Tuesday")
elif x == 2 :
    print("Wednesday")
elif x == 3 :
    print("Thursday")
elif x == 4 :
    print("Friday")
elif x == 5 :
    print("Saturday")
elif x == 6 :
    print("Sunday")
