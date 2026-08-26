ab = input()
an = input()

if ab == an :
    print(" it's a tie " )
elif (ab == "Rock" and an == "Scissors" )  or \
 (ab == "Scissors" and an == "Paper" ) or \
 (ab == "Paper" and an == "Rock" ):
     print("Abhinav Wins")
else:
    print("Anjali Wins")