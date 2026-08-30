import math
def number_of_cars_needed(no_of_people):

     if no_of_people == 0 :
         print(0)
     elif no_of_people <= 5:
         print(1)
     else:
         no_of_people = no_of_people/5 
         print(math.ceil(no_of_people))
         
no_of_people = int(input())
result = number_of_cars_needed(no_of_people)