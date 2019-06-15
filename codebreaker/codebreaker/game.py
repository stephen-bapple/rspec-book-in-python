class Game:
    def __init__(self, output):
        self._output_file = output
        self.secret = None

    def start(self, secret):
        self.secret = secret
        self.print('Welcome to Codebreaker!')
        self.print('Enter guess:')

    def guess(self, guess):
        self.print('+'*self.exact_match_count(guess)
                   + '-'*self.number_match_count(guess))

    def exact_match_count(self, guess):
        exact_match_count = 0

        for index in range(len(guess)):
            if self.exact_match(guess, index):
                exact_match_count += 1
        return exact_match_count

    def number_match_count(self, guess):
        number_match_count = 0

        for index in range(len(guess)):
            if self.number_match(guess, index):
                number_match_count += 1

        return number_match_count

    def exact_match(self, guess, index):
        return guess[index] == self.secret[index]

    def number_match(self, guess, index):
        return (guess[index] in self.secret and not
                self.exact_match(guess, index))

    def print(self, output):
        print(output, file=self._output_file)

