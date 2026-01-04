Feature: OrangeHRM Login and Dashboard

  # 1
  Scenario: Successful login with valid credentials
    Given user is on OrangeHRM login page
    When user logs in with valid username and password
    Then user should see the dashboard page

  # 2
  Scenario: Invalid login with wrong username
    Given user is on OrangeHRM login page
    When user logs in with invalid username and valid password
    Then user should see login error message

  # 3
  Scenario: Invalid login with wrong password
    Given user is on OrangeHRM login page
    When user logs in with valid username and wrong password
    Then user should see login error message

  # 4
  Scenario: Blank username and password
    Given user is on OrangeHRM login page
    When user logs in with blank username and password
    Then user should see login error message

  # 5
  Scenario: Remember me checkbox
    Given user is on OrangeHRM login page
    When user checks the remember me option and logs in
    Then user should remain logged in after browser refresh

  # 6
  Scenario: Logout functionality
    Given user is logged in successfully
    When user logs out
    Then user should be redirected to login page

  # 7
  Scenario: Dashboard welcome message
    Given user is logged in successfully
    Then user should see the welcome message on dashboard

  # 8
  Scenario: Check dashboard menu links
    Given user is logged in successfully
    Then user should see all main menu links (Admin, PIM, Leave, etc.)

  # 9
  Scenario: Profile page access
    Given user is logged in successfully
    When user navigates to profile page
    Then user should see correct profile info

  # 10
  Scenario: Change password
    Given user is logged in successfully
    When user changes password successfully
    Then user should be able to login with new password
