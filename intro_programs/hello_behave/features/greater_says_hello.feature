Feature: greeter says hello

  In order to start learning unittest and behave
  As a reader of the RSpec book
  I want a greeter to say Hello

  Scenario: greeter says Hello
    Given a greeter
    When I send it the greet message
    Then I should see "Hello Behave!"

