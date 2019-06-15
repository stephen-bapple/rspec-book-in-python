#! /usr/bin/env python
from sys import stdout

from codebreaker import Game

game = Game(stdout)
game.start('1234')

guess = input().strip()

while guess:
    game.guess(guess)
    guess = input().strip()

