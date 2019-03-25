from setuptools import find_packages, setup
from setuptools.command.test import test


class Tester(test):

    def run_tests(self):
        from xmlrunner import XMLTestRunner
        tests = TestLoader().discover('tests', pattern='test_*.py')
        runner = XMLTestRunner(output='reports')
        result = runner.run(tests)
        exit(0 if result.wasSuccessful() else 1)


setup(
    name='codebreaker',
    author='Stephen Bapple',
    author_email='stephen.bapple@gmail.com',
    description='Python version of the Codebreaker program for the RSpec book.',
    url='https://github.com/stephen-bapple/rspec-book-in-python/codebreaker/',
    packages=find_packages(),
    install_requires=[
        'expects>=0.9.0',  # Needed for unit tests.
        'behave>=1.2.6',  # Needed for features.
        'wheel>=0.33.1',  # Needed to install this package.
    ]
)

