*** Settings ***
# # is used to comment single line.
# Settings sections include the library which are we using in our test case.
# Library may be built-in and user defined.
# Some of the built-in library are 1. Collections 2. DateTime 3. BuiltIn 4. OperatingSystem, etc
# user-defined library: some_file_name.py, etc.
# Define metadata for test case.
# Example is shown below

# below importing Built-In/predefined Library.
Library   Collections
Library   BuiltIn
Library   DateTime

#Below is the user defined library.
#Library   Calculator.py
#Library   /home/test/robot_framework/calculator.py





*** Variables ***
# In this section, you will put all the variable like scalar variable (normal variable),
# List variable, dictionary variable and enviroment variable.
# Variable in robot framework are case-insensitive, and also spaces and underscored are ignored.
# Scalar Variable example is shown below


${Var1}   Good Morning
${var1}   Hii
${Var 1}  Tech-Bloggers
${var 1}  Hii
${Var_1}  Users
${Var 2}  Users

# Creating empty variable.
${var2}   ${EMPTY}
${sum}     0
# Creating boolean type variable with value true and false.
${boolean_variable_1}   ${TRUE}
${boolean_variable_2}   ${FALSE}


# Below examples shows list variable example
@{List}    10   20   30   40

# Below examples shows dictionary variable
&{dict}    name=Ram    age=19    course=BE    branch=CSE

# Creating empty list
@{List_2}    @{EMPTY}
@{List_3}    @{EMPTY}
#Creating empty dictionary
&{dict_1}    &{EMPTY}

   





*** Keywords ***
# In this section, you have to define your own keywords(user-defined keywords).
# below is the example of creating own keyword.

Create_Chart
	FOR   ${J}   IN RANGE   3
		${x-axis}   Create List   ${J}
		${y-axis}   Create List    ${List}[${J}]
		Append to list   ${List_2}   ${x-axis}
		Append to list   ${List_3}   ${y-axis}
    END
	LOG   ${List_2}
	LOG   ${List_3}
	




*** Test Cases ***
# In this block, you have to write your test case.
Basic Test Case  #Test case name
	
	FOR   ${I}   IN RANGE   3
		${sum} =  Evaluate   ${sum}+${List}[${I}]
	END
	LOG   ${sum}
# How to run keyword.
	run keyword		Create_Chart
	LOG   ${Var1}   
	LOG   ${var1}   
	LOG   ${Var 1}  
	LOG   ${var 1}  
	LOG   ${Var_1}
	LOG   ${Var 2}
	LOG   ${List}
	LOG   ${dict}
	Log   ${List_2}
	Log   ${dict_1}
	Log   ${boolean_variable_1}
	Log   ${boolean_variable_2}