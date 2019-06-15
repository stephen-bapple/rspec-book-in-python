from functools import reduce


class Marker:
    def __init__(self, secret, guess):
        self.secret, self.guess = secret, guess

    def exact_match_count(self):
        return reduce(
            lambda matches, index:
                matches + (1 if self.exact_match(index) else 0),
           range(0, 4), 0)

    def number_match_count(self):
        return reduce(
            lambda matches, index:
                matches + (1 if self.number_match(index) else 0),
            range(0, 4), 0)

    def exact_match(self, index):
        return self.guess[index] == self.secret[index]

    def number_match(self, index):
        return self.guess[index] in self.secret and not self.exact_match(index)

