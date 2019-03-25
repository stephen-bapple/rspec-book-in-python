class Game:
    def __init__(self, output):
        self.output = output

    def start(self):
        self.output.print('Welcome to Codebreaker!')
        self.output.print('Enter guess:')

