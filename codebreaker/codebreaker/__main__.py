#! /usr/bin/env python
import random
from sys import stdout

from codebreaker import Game


def generate_secret_code():
    options = list('123456')
    return ''.join(random.choice(options) for _ in range(4))

secret_code = generate_secret_code()

game = Game(stdout)
game.start(secret_code)

guess = input().strip()

while guess:
    game.guess(guess)
    guess = input().strip()

print(f'The secret code was: <{secret_code}>')

