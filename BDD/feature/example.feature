Feature: login
As a user I want to be able to log in to the application
  So that I can access my account and perform actions

Scenario:Successful login with valid credentials
 Given  I am on the login page
 When I enter the username "adminhr"
 And  I enter the password "123#@!QWEewq"
 And  I click the login button
 Then I should be redirected to the dashboard page











