import random

def createOutput(quote, prevOutput, guess):
    output = ""
    for i in range(len(quote)):
        if quote[i].lower() == guess.lower():
            output += guess
        elif prevOutput != "" and prevOutput[i].isalpha():
            output += prevOutput[i]
        elif quote[i].isalpha():
            output += "_"
        else:
            output += quote[i]
    return output


def createGuess(turn, prevGuess, userMoney, compMoney, quote):
    if turn == 1:
        print("YOUR TURN")
        guess = "a"

        while guess in "aeiou":
            guess = input("Guess: ")

            if guess == "!vowel":
                if userMoney > 10:
                    userMoney -= 10
                    guess = input("Vowel: ")
                    break
                else:
                    print("Not enough money!")
                    guess = "a"

            if guess == "!phrase":
                guess = input("Guess the entire phrase: ")
                if guess.lower() == quote.lower():
                    userMoney += 100
                    return guess, userMoney, compMoney
                else:
                    userMoney -= 100
                    guess = "a"

            while guess in prevGuess or len(guess) > 1 or guess.isalpha() == False:
                print("Try again!")
                guess = "a"
    else:
        print("COMPUTER'S TURN")
        letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        for i in prevGuess:
            letters.remove(i)
        guess = letters[random.randint(0, len(letters) - 1)]

        while guess in "aeiou":
            if compMoney > 10:
                compMoney -= 10
                break
            else:
                guess = letters[random.randint(0, len(letters) - 1)]
    return guess, userMoney, compMoney


quotes = ["If you're nothing without the suit, then you shouldn't have it", "I can do this all day", "We have a Hulk",
          "Dormammu, I've come to bargain", "You should've gone for the head",
          "Well done, you just decapitated your grandfather", "I have been falling for thirty minutes",
          "With great power comes great responsibility", "I've never met this man in my life",
          "Doth mother know you weareth her drapes?"]

userMoney = 0
compMoney = 0
turn = 1

print("WELCOME TO THE")
print('''───────
──────▄▄████████████▄──────
────▄██▀▀────▐███▐████▄────
──▄██▀───────███▌▐██─▀██▄──
─▐██────────▐███─▐██───██▌─
─██▌────────███▌─▐██───▐██─
▐██────────▐███──▐██────██▌
██▌────────███▌──▐██────▐██
██▌───────▐███───▐██────▐██

  𝚆𝙷𝙴𝙴𝙻 𝙾𝙵 𝙼𝙰𝚁𝚅𝙴𝙻 𝚀𝚄𝙾𝚃𝙴𝚂

██▌───────███▌──▄─▀█────▐██
██▌──────▐████████▄─────▐██
██▌──────█████████▀─────▐██
▐██─────▐██▌────▀─▄█────██▌
─██▌────███─────▄███───▐██─
─▐██▄──▐██▌───────────▄██▌─
──▀███─███─────────▄▄███▀──
──────▐██▌─▀█████████▀▀────
──────███──────────────────

Text art credit: textart4u.blogspot.com''')
input("\nType enter to continue.")
print("\033[H\033[J")
introInput = input("Type !rules if you'd like the rules, and !play if you'd like to start. \n")
if introInput == "!rules":
    print('''You will be given n blanks to guess a Marvel quote of n length.
  Type a consonant for free.
  Vowels cost $10. Type !vowel to enter a vowel, then type the vowel.
  Guess the entire phrase with !phrase. If you get it right, you get $100, but if you get it wrong, you lose $100.
  You will also have to play against the computer. First to $500 wins!''')
    tempInput = input("Type space, then enter to exit.")
    if tempInput == " ":
        introInput = "!play"
if introInput == "!play":
    print("\033[H\033[J")

game = True
while game:
    quote = quotes[random.randrange(0, len(quotes))]
    output = createOutput(quote, "", "")
    prevGuess = []

    while "_" in output:
        if userMoney > 500 or compMoney > 500:
            break

        print(f'Your money: ${userMoney}\tComputer money: ${compMoney}')
        print(output + "\n")

        guess, userMoney, compMoney = createGuess(turn, prevGuess, userMoney, compMoney, quote)
        if guess.lower() == quote.lower():
            break
        else:
            prevGuess.append(guess)

        if turn == 1:
            if guess in quote.lower():
                print("You get $15 for a correct letter!")
                userMoney += 15
            else:
                print("Incorrect letter!")
                turn = (turn + 1) % 2
        else:
            print("Computer guessed: " + guess)
            if guess in quote.lower():
                print("Computer gets $15 for a correct letter!")
                compMoney += 15
            else:
                print("Incorrect letter!")
                turn = (turn + 1) % 2

        output = createOutput(quote, output, guess)

        input("Type anything to continue")
        print("\033[H\033[J")

    if userMoney > 500 or compMoney > 500:
        game = False

    print(f'\nYou got the quote! It was "{quote}."')
    quotes.remove(quote)
    input("Type anything to continue")
    print("\033[H\033[J")

if userMoney > 500:
    print('''____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| ''')
    print("Congrats! :)")
elif compMoney > 500:
    print('''____    ____  ______    __    __      __        ______        _______. _______ 
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|
                                                                               ''')
    print("Better brush up on your Marvel trivia! :(")
