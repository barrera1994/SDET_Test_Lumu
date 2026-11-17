Feature: features to test the functionalities

    Background:
        Given I navigate to the "https://wordcounter.net/" url

    Scenario Outline: Validate number of words
        When I type the text "<text>"
        Then the number of words should be "<number>"

        Examples:
          | text | number |
          | lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | 16 |
          | https://wordcounter.net/        | 1 |
          | hello, lumu?                    | 2 |
          | hello, 😀lumu lumu--attacks     | 4 |
          | lumu--attacks                   | 2 |

    Scenario Outline: Validate number of characters
        When I type the text "<text>"
        Then the number of characters should be "<number>"

        Examples:
          | text | number |
          | lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | 117 |
          | lumu °!"#$%&/()=?   | 17 |
          | lumu /n/n           | 9 |
          | lumu,---😀lumu     | 14 |
