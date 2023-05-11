import random

while True:
    try:
        level = int(input ("Level: "))
        number = random.randrange(1, level)
        if level <= 0:
            pass
    except:
        pass
    else:
        break
    

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        elif guess == number:
            print("Just right!")
            break
    except:
        pass

    
