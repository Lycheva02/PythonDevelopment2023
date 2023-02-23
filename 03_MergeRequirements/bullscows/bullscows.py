import random
import cowsay

def bullscows(guess, secret):
    res = [0, 0]
    for i in range(len(guess)):
        if guess[i] in secret:
            if i >= len(secret):
                res[1] += 1
            elif guess[i] == secret[i]:
                res[0] += 1
            else:
                res[1] += 1
    return tuple(res)

def ask(prompt, valid=None):
    ##res = input(prompt)
    #cow = random.choice(cowsay.list_cows())
    #print(cowsay.cowsay(prompt, cow=cow))
    file = '    __    __\n    ||    ||\n    ||    ||\n  ~~~~~~~~~~~~\n  |  <.>      |\n|*            |\n|             |__________________________      _*\n  | --<                                  |-----\n  |________                              |\n          |                              |\n          |                              |\n          |                              |\n          |                              |\n          --------------------------------\n              U  U               U  U\n'
    print(cowsay.cowsay(prompt, cowfile=file))
    res = input()
    if valid:
        while res not in valid:
            ##res = input(prompt)
            #cow = random.choice(cowsay.list_cows())
            #print(cowsay.cowsay(prompt, cow=cow))
            print(cowsay.cowsay(prompt, cowfile=file))
            res = input()
    return(res)

def inform(format_string, bulls, cows):
    cow = random.choice(cowsay.list_cows())
    print(cowsay.cowsay(format_string.format(bulls, cows), cow=cow))

def gameplay(ask, inform, words):
    num_prompts = 0
    secret = random.choice(words)
    while True:
        guess = ask("Введите слово: ", words).strip()
        num_prompts += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if guess == secret:
            break
    return num_prompts

