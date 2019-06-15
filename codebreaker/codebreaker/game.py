from codebreaker.marker import Marker


class Game:
    def __init__(self, output):
        self._output_file = output
        self.secret = None

    def start(self, secret):
        self.secret = secret
        self.print('Welcome to Codebreaker!')
        self.print('Enter guess:')

    def guess(self, guess):
        marker = Marker(self.secret, guess)
        self.print('+'*marker.exact_match_count()
                   + '-'*marker.number_match_count())

    def print(self, output):
        print(output, file=self._output_file)

