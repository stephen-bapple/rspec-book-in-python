from expects import expect, contain

from codebreaker import Game


class Output:
    def __init__(self):
        self._messages = []

    def messages(self):
        return self._messages

    def write(self, message):
        self._messages.append(message)


@given('I am not yet playing')
def step_impl(context):
    pass

@when('I start a new game')
def step_impl(context):
    context.output = Output()
    context.game = Game(context.output)
    context.game.start()

@then('I should see "{message}"')
def step_impl(context, message):
    expect(context.output.messages()).to(contain(message))

