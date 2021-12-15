*** Settings ***
Library    textbox.TextBox

*** Test Cases ***

Testing boxes
    ${input_dict}=    Create Dictionary
    ...    Full Name=test
    ...    Email=test@test.com
    ...    Current Address=address test 3
    ...    Permanent Address=permanet address test 2
    Navigate To    https://demoqa.com/text-box 
    Input Data    ${input_dict}
    Verify Output    ${input_dict}
    Close Driver
    
