from unittest import TestCase, main
from expects import expect, equal

from unit_test_greeter import UnitTestGreeter


class TestGreeter(TestCase):

    def test_greeter_says_hello(self):
        greeter = UnitTestGreeter()
        greeting = greeter.greet()
        expect(greeting).to(equal('Hello UnitTest!'))


if __name__ == '__main__':
    main()

