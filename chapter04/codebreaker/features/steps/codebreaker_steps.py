from codebreaker import Game

@given('I am not yet playing')
def step_impl(context):
    pass

@when('I start a new game')
def step_impl(context):
    context.new_game = Game().start()

