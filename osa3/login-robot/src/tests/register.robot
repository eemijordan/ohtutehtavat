*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jari  jarii123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short


Register With Enough Long But Invalid Username And Valid Password
   Input Credentials  kalle!  kamu123
   Output Should Contain  Invalid Username


Register With Valid Username And Too Short Password
   Input Credentials  jari  jari1
   Output Should Contain  Too Short Password


Register With Valid Username And Long Enough Password Containing Only Letters
   Input Credentials  jari  jarikatti
   Output Should Contain  Password Containing Only Letters



*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
