Legacy Code Repository in RDBMS


# Overview

This is a tool to upload the Legacy mainframe off-line code into Relational Database Management System for faster analysis and documentation purpose.
The script is written in Python and the database used here is MySQL. 
So the pre-requisites are the python and MySQL installed.

# Implementation

The below steps need to be followed for loading the components in a structured manner.
Provide the folder location against the "path=" variable given in the script.
The folder should contain all the Codes segregated based on the type.
For example, A folder named COBOL should contain all the COBOL code, JCL containing all the JCLs etc.
Once the Code is segregated into different folders, give these folder locations as input to the "path=" for each run.
The Database Table has got 6 columns namely Language type (COBOL,PL1 etc) , File Name, Content of each file, Line Number (Line number of each Filename), Content Type and the Created TimeStamp.
Once all the components are loaded, which will take a few minutes, user will be able to Query the Table to get various results for Analysis and Documentation.
RegEx queries can be used for maximizing the Analysis results.
For example, user can write a query to get the copybook names used in the programs and can be joined against the List of copybook names loaded to find the missing components.
The Content Type Column can be used to further categorize the kind of statements, like Move, Conditional, Loop, Comments etc.
Right now it is not populated using the script and SQL statements are used to give value to the Content Type column, after loading the Database Table.

# Conclusion

Millions of lines of code can be loaded into the table in a few minutes and analysis can be completed in a couple of hours.
It may take several days to complete the same work, if done manually.

