import random
import getpass

def amount_players():
    while True:
        choice = input("Enter number of players (1 or 2):\n").strip()
        if choice == "1" or choice == "2":
            num_players = int(choice)
            break
        print("Invalid choice. Please enter 1 or 2.")
    return int(num_players)

def generate_code(a):
    
    if a == 2:
        print("\n ***PLAYER 2: LOOK AWAY***")
        while True:
            secret_input = str(getpass.getpass("Player 1 enter a secret 5-digit code (1-6)").strip())
            ba=[]
            for i in secret_input:
                if i in valid_nums:
                    ba.append("true")
                else:
                    ba.append("false")
            if len(secret_input)==5 and "false" not in ba:
                secret_code = list(secret_input)
                print("\nSecret code set! Now Player 2 guess the secret code")
                break
            else:
                print("***Invalid code***")
    else:
        secret_code = [random.choice(list(valid_nums.keys())) for i in range(5)]
        print("\nComputer has generated a secret 5-digit code")
    return secret_code
    
def does_it_work(cod, nums):
    attempt=0
    while True:
        attempt += 1
        guess = input(f"\nAttempt No#: {attempt} | Enter your guess: ").strip()
        ka=[]
        if guess == "give":
            print(f"The correct code is {str(cod)}")
            break
        for i in guess:
                if i in nums:
                    ka.append("true")
                else:
                    ka.append("false")
        if len(guess) != 5 or "false" in ka:
            print("Invalid guess. Use exactly 5 digits and numbers 1 to 6")
            continue
        return (list(guess))
        
def testing_guess (gu, sec):
        cor = 0
        wro = 0
        attempts=10
        for i in range(5): 
            
            guesscop = gu.copy()
            secretcop = sec.copy()
            gues = gu.copy()
            secr = sec.copy()
            if guesscop[i] == secretcop[i]:
                cor += 1
                guesscop.pop(i)
                secretcop.pop(i)
        for i in range(5):
            if guesscop[i] in secretcop:
                wro += 1
        if cor == 5:
            print("CONGRAGULATION!! You have guessed the right code! You won!")
            return
        attempts -= 1
            
        print(f"Correct position(s): {cor}")
        print(f"Wrong position(s): {wro}")
        print(secretcop)


print("\n***INSTUCTIONS***")
print("Guess the secret 5-digit code using the numbers: 1, 2, 3, 4, 5 and 6")
print("- 'Correct Position': Right number in the right spot")
print("- 'Wrong Position': Number exists in the code, but its in the wrong spot")
print("You will get 10 attempts to get the right code")
print("If you give up, write 'give'")
valid_nums = {str(i): f"Digit {i}" for i in range(1,7)}    

    
players = amount_players()
secret = generate_code(players)

does_it_work(secret, valid_nums)




