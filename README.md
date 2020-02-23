# worklessSQL_trash_generator
Save some of your precious time.

### About
Idea for this project was born on lesson called 'Databases administration'. After half year of creating databases in which we were mindlessly putting rows that weren't even needed to learn proper SQL syntax or database structures, I decided that I have enough and made a simple python script. It creates 'INSERT' SQL query based on informations provided by user.
Script is simple and easy to understand, feel free to add your own modules ^-^

## Setup
Just in case you didn't noticed - it's a python script, so you need Python interpreter in order to run *.py files.
### Download
Clone or Download >> `Download ZIP`
### Preperations
Export it to your desktop or whatever and navigate with your terminal/cmd. <br />
Open `config.py` with your favourite text editor and you're ready to go.

## Usage

-- After opening `config.py` --<br/>
In `values` provide functions or values you wish to generate. <br />
In `columns` specify names of following columns in your databse. <br />
In `database_name` - it's obvious. <br />
In `table_name` - same story. <br />
In `number_of_rows` - how many rows of garb- ...content will be printed <br/>

Then `py execute.py` and collect your reward.

### Files
  `dataHandler.py` - store elements to draw from and manage `.txt` dependencies <br/>
  `func.py` - main module providing functions generating output <br/>
  `script_config.py` - main configuration file for user specified data <br/>
  `execute.py` - start script <br/>
  
### Functions
Module keyword `func` [exp. `func.rand_number(9)`]. <br/>
All dependencies are stored in , you guessed it, folder `dependencies` aka names, surnames, nationalities etc. <br/>
Put into `.txt` files anything you want as long as it make sense ^-^ <br/>

<li> rand_name() - print random name from the list </li>
<li> rand_surname() - same story </li>
<li> rand_city() - same story </li>
<li> rand_nationality() - same story </li>
<li> rand_country() - same story </li>
<li> rand_currency() - this one takes data from array</li>
<li> rand_productName() - same here  </li>
<li> rand_email() - generates random email with rand_string() and domain from list </li>
<li> rand_age() - gives random number from 16 to 110</li>
<li> rand_number(number_of_digits) - generates number as long as [number_of_digits] </li>
<li> rand_string(number_of_chars) - same story, but mixes number and letters - you can provide your own</li>
<li> rand_postCode() - generates post code as string `00-000` with numbers </li>
    
## Other info
Script recognizes is value is number or string, so monitor what type of data your column accepts.
If you want to set number element as string use str() function [exp. `str(func.rand_number(9))` - for phone number ]

After your code is generated - put it simply to your DBMS, or just use phpmyadmin.

### Contact
If you wish to give me feedback, inform about mistakes or simply scold me go ahead and messenge me ^-^
