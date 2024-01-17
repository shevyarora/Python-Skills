# Guess a number game 

import random

print("Welcome to Guess a Number game :")
print("You have total 5 chances to Guess a number ")

n=random.randrange(1,101)

sen1="You won ! You guess the number in {} attempts "
sen2="You Lose ! The number was {}"
i=1
flag=0
while i<=5:
    print("Enter a Number : (1 to 100)")
    guess=int(input())
    if guess==n:
        print(sen1.format(i))
        flag=1
        break
    elif guess<n:
        print("Please choose Higher Number")
    else :
        print("Please choose Lower Number")
    i+=1


if flag==0:
    print(sen2.format(n))
