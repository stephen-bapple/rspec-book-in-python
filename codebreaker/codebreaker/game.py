class Game:
    def __init__(self, output):
        self._output_file = output

    def start(self):
        print('Welcome to Codebreaker!', file=self._output_file)
        print('Enter guess:', file=self._output_file)

