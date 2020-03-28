# Created by oleg3 at 3/18/2020
Feature: Auto-suggestion
  # Enter feature description here

  Scenario Outline: Verify that Auto-suggestion works
    Examples:
    |keyword    |expected_result   |
    |Hammer     | Hammer           |
    |Pliers     | Pliers           |
    |Pry bar    | Pry bar          |
    |Lawn Mower | Lawn Mower       |

    Given Open Homedepot page
    When Input <keyword> in search field
    And Click on search button and wait a couple of seconds
    Then Verify "<expected_result>" is shown.
    #Then Count them

  Scenario: User is taken to the search results page
    Given Open Homedepot page
    When Input dry vacuum in search field
    And Click on search button and wait a couple of seconds
    Then Verify "dry vacuum" is shown.

  Scenario: Verify that Registration flow works as expected
    Given Open Homedepot page
    When Click account button
    And Click 'register' button
    And Fill email field with oleg31950@gmail.com
    And Fill password field with <12345th78>
    And Fill zip code field with 98661
    And Fill Phone field with 5038050714
    And Click submit
    Then Expected registration will be complete successfully https://www.homedepot.com/










