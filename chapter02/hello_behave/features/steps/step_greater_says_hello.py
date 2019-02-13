from behave import given, when, then
from expects import expect, equal

from behave_greeter import BehaveGreeter


@given('a greeter')
def step_impl(context):
    context.greeter = BehaveGreeter()

@when('I send it the greet message')
def step_impl(context):
    context.message = context.greeter.greet()

@then('I should see "{message}"')
def step_impl(context, message):
    expect(context.message).to(equal(message))

