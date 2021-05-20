Feature: RAM alive
  As a viewer(of rick and morty),
  I want to know who is still alive in the series
  So that I can predict who might die next

  Scenario Outline: RAM char-alive
    When the RAM API is queried with "<character>"
    Then the response status code is 200
    And the response shows status of "<status>"

    Examples: char-alive
      | character                 | status     |
      | Rick Sanchez              | "Alive"    |
      | Morty Smith               | "Alive"    |
