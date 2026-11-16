Feature: features to test the functionalities

    Background:
        Given I navigate to the "https://wordcounter.net/" url

    Scenario Outline: Validate number of words
        When I type the text "<text>"
        Then the number of words should be "<number>"

        Examples:
          | text | number |
          | lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | 16 |
          |  | 0 |
          | hello | 1 |
          | hello, lumu? | 2 |
          | hello, lumu | 3 |

