import random

while True:
    try:
        level = int(input ("Level: "))

        if level <= 0:
            pass
    except:
        pass

    number = random.randrange(1, level)
    break
    

while True:
    try:
        guess = int(input("Guess: "))
        
    except:
        pass
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")
    elif guess == number:
        print("Just right!")
        break

    
