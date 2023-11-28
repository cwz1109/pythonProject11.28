
import random
hscore=0
cscore=0

r = 1

while True:
    if hscore < 3 and cscore < 3:
        print("ROUND",r)
    elif hscore==3:
        print("END")
        print("HUMAN WIN")
        break
    elif cscore==3:
        print("END")
        print("COMPUTER WIN")
        break
    # user' choice
    H=str(input("you choose:"))
    H=H.upper()
    # computer's choice
    C=random.randint(1,3)
    if C==1:
        print("Computer choose R")
    elif C==2:
        print("Computer choose S")
    elif C==3:
        print("Computer choose P")

    if H==str("R") and C==1:
        print("NO LOSE NO WIN")
    elif H==str("R") and C==2:
        print("YOU WIN")
        hscore+=1
    elif H==str("R") and C==3:
        print("YOU LOSE")
        cscore+=1
    elif H==str("S") and C==1:
        print("YOU LOSE")
        cscore+=1
    elif H==str("S") and C==2:
        print("NO LOSE NO WIN")
    elif H==str("S") and C==3:
        print("YOU WIN")
        hscore+=1
    elif H==str("P") and C==1:
        print("YOU WIN")
        hscore+=1
    elif H==str("P") and C==2:
        print("YOU LOSE")
        cscore+=1
    elif H==str("P") and C==3:
        print("NO LOSE NO WIN")
    print("Your score is",hscore)
    print("Computer's score is",cscore)
    r += 1

quit()




quit()


score=0
lives=3
for q in range(1,11):
    import random
    type = random.randint(1, 4)
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    if type == 1:
        print("Question",q)
        print(x, "+", y, "=")
        a = int(input("Answer:"))
        A = x+y
        if A == a:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            lives -= 1
    elif type == 2:
        print("Question", q)

        print(x, "-", y, "=")
        a = int(input("Answer:"))
        A = x - y
        if A == a:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            lives -= 1
    elif type == 3:
        print("Question",q)

        print(x, "*", y, "=")
        a = int(input("Answer:"))
        A = x * y
        if A == a:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            lives -= 1
    elif type == 4:
        print("Question",q)
        p = random.randint(1,20)
        q = random.randint(1,20)
        x = p*q
        y = p
        print(x, "/", y, "=")
        a = int(input("Answer:"))
        A = x / y

        if A == a:
            print("CORRECT")
            score += 1
        else:
            print("WRONG")
            lives -= 1
    if lives == 0:
        print("LOSE")
        break

print("OVER")
if score>8:
    print("WIN")
else:
    print("LOSE  (:")




