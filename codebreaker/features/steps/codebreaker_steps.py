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
    context.game.start('1234')

@then('I should see "{message}"')
def step_impl(context, message):
    expect(context.output.messages()).to(contain(message))

@given('the secret code is "{secret}"')
def step_impl(context, secret):
    context.output = Output()
    context.game = Game(context.output)
    context.game.start(secret)

@when('I guess "{guess}"')
def step_impl(context, guess):
    context.game.guess(guess)

@then('the mark should be "{mark}"')
def step_impl(context, mark):
    expect(context.output.messages()).to(contain(mark))

