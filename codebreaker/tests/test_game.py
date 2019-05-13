from unittest import TestCase, main, skip
from expects import expect, contain

from codebreaker import Game


class Output:
    def __init__(self):
        self._messages = []

    def messages(self):
        return self._messages

    def write(self, message):
        if message != '\n':
            self._messages.append(message)


class TestGame(TestCase):
    def setUp(self):
        self.output = Output()
        self.game = Game(self.output)

    def test_initialization_sends_a_welcome_message(self):
        self.game.start('1234')
        expect(self.output.messages()).to(contain('Welcome to Codebreaker!'))

    def test_start_prompts_for_first_guess(self):
        self.game.start('1234')
        expect(self.output.messages()).to(contain('Enter guess:'))

    def test_guess_with_no_matches(self):
        self.game.start('1234')
        self.game.guess('5555')
        expect(self.output.messages()).to(contain(''))

    def test_guess_with_1_number_match(self):
        self.game.start('1234')
        self.game.guess('2555')
        expect(self.output.messages()).to(contain('-'))

    def test_guess_with_1_exact_match(self):
        self.game.start('1234')
        self.game.guess('1555')
        expect(self.output.messages()).to(contain('+'))

    def test_guess_with_2_number_matches(self):
        self.game.start('1234')
        self.game.guess('2355')
        expect(self.output.messages()).to(contain('--'))

    def test_guess_with_1_number_match_and_1_exact_match_in_that_order(self):
        self.game.start('1234')
        self.game.guess('2535')
        expect(self.output.messages()).to(contain('+-'))

if __name__ == "__main__":
    main()

