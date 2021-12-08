*** Settings ***
Library    textbox.TextBox

*** Test Cases ***

Testing boxes
    ${input_dict}=    Create Dictionary
    ...    userName=test
    ...    userEmail=test@test.com
    ...    currentAddress=address test 3
    ...    permanentAddress=permanet address test 2
    Test Boxes    ${input_dict}    
