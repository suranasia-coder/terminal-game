# Master Mind Game
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
    
def does_it_work(secret, nums, ):
    attempts = 10

    while attempts > 0:
        guess = input(f"\nAttempts left: {attempts} | Enter your guess: ").strip()

        if guess == "give":
            print(f"The correct code was {secret}")
            return

        if len(guess) != 5 or any(d not in nums for d in guess):
            print("Invalid guess. Use exactly 5 digits (1–6).")
            continue

        guess_list = list(guess)

        # Check positions
        correct = 0
        wrong = 0

        secret_copy = secret.copy()
        guess_copy = guess_list.copy()

        # First pass: correct positions
        for i in range(4, -1, -1):
            if guess_copy[i] == secret_copy[i]:
                correct += 1
                guess_copy.pop(i)
                secret_copy.pop(i)

        # Second pass: wrong positions
        for digit in guess_copy:
            if digit in secret_copy:
                wrong += 1
                secret_copy.remove(digit)

        print(f"Correct position(s): {correct}")
        print(f"Wrong position(s): {wrong}")

        if correct == 5:
            print(" CONGRATULATIONS! You cracked the code!")
            return

        attempts -= 1

    print(" Game over. The code was " ," " .join(secret))
        
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

while True:
    players = amount_players()
    secret = generate_code(players)

    does_it_work(secret, valid_nums)

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    
    if again != "yes":
        print("Thanks for playing!")
        break


