wisielec = """
           ______________
           |            |
           |            0
           |           /|\\
           |           /\\
      _____|_____
""".splitlines()

no_of_tries = 5
fail_counter = -1
i = 0
word = "Patryk".upper()
user_word = []
used_letters = []
for _ in word:
    user_word.append("_")
run = True
while run:
    user_letter = input("Podaj literę: ").upper()
    used_letters.append(user_letter)
    index = -1
    letter_hit = False
    for letter in word:
        index += 1
        if letter == user_letter:
            user_word[index] = word[index]
            letter_hit = True

    if not letter_hit:
        fail_counter += 1
        i += 1
        x = 0
        for number in range(0, i, 1):
            print(wisielec[7 - i + x])
            x += 1
        if fail_counter == no_of_tries:
            print("Gra skończona")
            break
    else:
        print("Trafiłeś litery : ")
        print(user_word)

    if list(word) == user_word:
        print("Gratulacje, odgadnąłeś hasło !")
        break
