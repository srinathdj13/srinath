import random
def game():
    a=(2,3,4,5)
    b=int(input("enter the another value"))
    c=random.choice(a)
    print(c)
    if(b!=c):
        print("you have lost game")
        game()
    else:
        print("you have win game")
game()
