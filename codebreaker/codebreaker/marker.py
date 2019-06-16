from collections import Counter
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
        return self.total_match_count() - self.exact_match_count()

    def total_match_count(self):
        return len(
            list((Counter(self.guess) & Counter(self.secret)).elements())
        )

    def exact_match(self, index):
        return self.guess[index] == self.secret[index]

