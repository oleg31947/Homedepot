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
    # And Count them. Step

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
    And Fill password field with 12345th78
    And Fill zip code field with 98661
    And Fill Phone field with 5038050714
    And Verify my mobile number, click
    And Click submit
    Then Expected registration will be complete successfully https://www.homedepot.com/

  Scenario: Verify that Sign-In with existing account works
    Given Open Homedepot page
    When Click account button
    And Check button Sign out
    And Click 'register' button
    And Fill email field with oleg31950@gmail.com
    And Fill password field with 12345th78
    And Fill zip code field with 98661
    And Fill Phone field with 5038050714
    And Verify my mobile number, click
    And Click submit
    Then Expected login will be complete successfully https://www.homedepot.com/customer/auth/v1/signin

  Scenario: Shopping cart - empty state
    Given Open Homedepot page
    When Click 'cart' button
    Then Expected cart page will have the title: Cart 0 items


  Scenario: User is able to add an item to the Shopping Cart
    Given Open Homedepot page
    When Insert circular saw in search field
    And Insert shovel saw in search field
    And 1 product added to shopping cart
    Then Expect 1 Item Added to Cart
    #Then Close all pop-ups


  Scenario: User is able to add multiple items to the Shopping Cart
  Given Open Homedepot page
  When Insert circular saw in search field
  And 1 product added to shopping cart
  And Return to product search page
  And Insert drill in search field
  And 1 product added to shopping cart
  And Return to product search page
  And Click cart button
  Then Expected cart page will have the title: Cart 2 items
#  Then Close all pop-ups

  Scenario: Shopping cart - Change quantity
  Given Open Homedepot page
  When Insert circular saw in search field
  And 1 product added to shopping cart
  And Return to product search page
  And Click cart button
  And Change quantity from 1 to 2
  Then Try expect items in cart will be 2

  Scenario: User is able to write a review
  Given Open Homedepot page
  When Insert hammer in search field
  And On search results page choose stars and click
  And Click 'write review' button
  Then Expected product has Write A Review button




