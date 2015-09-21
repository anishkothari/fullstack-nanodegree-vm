###Project 2 of Udacity's Full-Stack Nanodegree

This project runs on a Vagrant VM (virtual machine). The goal of this project is to create a basic implementation of a Swiss-style tournament in a PostgreSQL database. There is a pre-written test suite, so the student must use Python and SQL that make the tests pass.

###Instructions
Clone this project locally and navigate to the `vagrant/` directory.  
From there run the `vagrant up` and `vagrant ssh` commands in sequence.  
Then navigate to the `vagrant/tournament/` directory.  
Run the following command to set up the database `psql -f tournament.sql`.  
To run the test suite run `python tournament_test.py`.  

###Outcomes
Through the course of the [Introduction to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) course and this project, I learned the basic functionalities of Vagrant and PostgreSQL. I tested queries on the command-line using 'psql' and then wrote them as queries in Python. 

I learned the basics of using views and joins. I had trouble initially with the standings view - https://discussions.udacity.com/t/failing-test-for-reportmatch/31810 - with the two left joins, specifically.

I tried to consolidate the `singleInsert()` and `multipleInsert()` as they are identical except for the number of arguments passed in to them. However, I couldn't implement this properly and left them as separate methods in the end.

