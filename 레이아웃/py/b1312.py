import random
number = random.randint(1,100)
while 1:
    num = input("Guess my random number (Q to exit): ")
    if num=='Q' or num=='q' :
        break
    num = int(num)
    if num > number:
        print("DOWN")
    elif num < number:
        print("UP")
    else :
        print("RIGHT")
        break