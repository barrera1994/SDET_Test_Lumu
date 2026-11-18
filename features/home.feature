Feature: features to test the functionalities

    Background:
        Given I navigate to the "https://wordcounter.net/" url

    @punto1
    Scenario Outline: Validate number of words
        When I type the text "<text>"
        Then the number of words should be "<number>"

        Examples:
          | text                                                                                                                  | number |
          | lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | 16     |
          | lumu julian123 @julian-barrera 12345,3                                                                                | 4      |
          | hello, lumu?                                                                                                          | 2      |
          |                                                                                                                       | 0      |
          | lumu--attacks                                                                                                         | 2      |
          | 😀lumu                                                                                                                | 1      |
          | hello, 😀lumu lumu--attacks                                                                                           | 4      |

    @punto2
    Scenario Outline: Validate number of characters
        When I type the text "<text>"
        Then the number of characters should be "<number>"

        Examples:
          | text                                                                                                                  | number |
          | lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | 117    |
          | lumu °!"#$%&/()=?                                                                                                     | 17     |
          | lumu /n/n                                                                                                             | 9      |
          | lumu,---😀lumu                                                                                                        | 14     |
          |                                                                                                                       | 0     |

    @punto3
    Scenario Outline: validate top 3 Keyword Density
        When I type the text "<text>"
        Then the 3 most frequently repeated words are:
            | word_top     | number     |
            | <word_top1>  | <number1>  |
            | <word_top2>  | <number2>  |
            | <word_top3>  | <number3>  |

        Examples:
          | text                                                                                                        | word_top1 | number1 | word_top2   | number2 | word_top3 | number3 |
          | lumu lumu lumu illuminates illuminates attacks and adversaries lumu illuminates all attacks and adversaries | lumu      | 4       | illuminates | 3       | attacks   | 2       |
          | lumu where where attacks and adversaries lumu and where all lumu                                            | lumu      | 3       | where       | 3       | and       | 2       |
          | julian julian julianjulian  julian julian hola hola lumu mu lumu                                            | julian    | 3       | hola        | 2       | lumu      | 1       |
          | lumu lumu lumu                                                                                              | lumu      | 3       |             |         |           |         |