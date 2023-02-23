import random

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
    res = input(prompt)
    if valid:
        while res not in valid:
            res = input(prompt)
    return(res)

def inform(format_string, bulls, cows):
    print(format_string.format(bulls, cows))

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

