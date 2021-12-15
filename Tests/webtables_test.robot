*** Settings ***
Library    webtables.WebTables



*** Test Cases ***
Adding a member
    ${input_dict}=    Create Dictionary
    ...    First Name=Test
    ...    Last Name=TestTest
    ...    Email=testTest@test.com
    ...    Age=23
    ...    Salary=2800
    ...    Department=IT
    Navigate To    https://demoqa.com/webtables
    Click Add
    Complete Form    ${input_dict}
    Verify The Table    ${input_dict}
    Close Driver