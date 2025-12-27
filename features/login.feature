Feature: OrangeHRM Login

  Scenario: Successful login with valid credentials
    Given user is on OrangeHRM login page
    When user logs in with valid username and password
    Then user should see the dashboard page
