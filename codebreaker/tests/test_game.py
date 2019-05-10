from unittest import TestCase, main, skip
from expects import expect, contain

from codebreaker import Game


class Output:
    def __init__(self):
        self._messages = []

    def messages(self):
        return self._messages

    def write(self, message):
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


if __name__ == "__main__":
    main()

