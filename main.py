import random
from hangman_art import logo, hangman_pic


print(logo)
word = ['aerobics', 'archery', 'badminton', 'badminton', 'baseball', 'biking']
word_choose = random.choice(word)

guessed_world = []
for _ in range(len(word_choose)):
    guessed_world += "_"

hangman_life = 6

while hangman_life != 0:
    if '_' not in guessed_world:
        break
    user_letter = input("Give me a letter: ").lower()
    if user_letter in word_choose:
        print(f"You already guessed {user_letter}")
        for letter in range(len(word_choose)):
            if user_letter == word_choose[letter]:
                guessed_world[letter] = word_choose[letter]

    print(f"{''.join(guessed_world)}")
    if user_letter not in word_choose:
        print(hangman_pic[-hangman_life])
        hangman_life -= 1

if hangman_life == 0:
    print(f"\n\nTry again the world you need to guess in this game is: {word_choose}")
else:
    print("\n\nCongratulation you win this game!")