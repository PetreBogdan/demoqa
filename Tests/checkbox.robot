*** Settings ***
Library    checkbox.CheckBox


*** Test Cases ***

Check TestBoxes and verify them
    ${input_dict}=    Create Dictionary
    ...    Home=unchecked
    ...    Desktop=unchecked
    ...    Notes=checked
    ...    Commands=unchecked
    ...    Documents=checked
    ...    WorkSpace=unchecked
    ...    React=unchecked
    ...    Angular=checked
    ...    Veu=checked
    ...    Office=unchecked
    ...    Public=unchecked
    ...    Private=unchecked
    ...    Classified=unchecked
    ...    General=unchecked
    ...    Downloads=unchecked
    ...    Word File.doc=checked
    ...    Excel File.doc= unchecked 
    
    Navigate To    https://demoqa.com/checkbox
    Expand All
    Complete Checkboxes    ${input_dict}
    Verify Checked Boxes    ${input_dict}
    Close Driver