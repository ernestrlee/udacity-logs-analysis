# Udacity Log Analysis Project
# A Python program that uses SQL to gather and display information from a database.

## How to install

Start by installing Python 2 to your system.  For the latest version, please visit the [Python website](https://www.python.org/).
Next, install a command line tool such as [Git BASH](https://git-for-windows.github.io/).

A virtual machine (VM) is also needed to run the SQL database server.  For this project, Vagrant and VirtualBox were used.
Files can be found from the links below:
- https://www.virtualbox.org/wiki/Downloads
- https://www.vagrantup.com/downloads.html 

The VM is configured using files that can be found in the below link:
- https://github.com/udacity/fullstack-nanodegree-vm

The database file used for the project can be found here:
- https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Lastly, download the following file and place it into the same folder as the database file:
- reporttool.py

## How to use the Logs Analysis tool

1. Run the command line tool.
2. Start your virtual machine.  If using Vagrant, this is usually done by using the "vagrant up" command followed by "vagrant ssh".
3. Navigate to the directory that contains the "newsdata.sql" database as well as the "reporttool.py" file.
4. Using Python, run the file, "reporttool.py".

The program will run three queries and print out the following information from the database:
1. The top three most popular articles.
2. The most popular authors based on the sum of all articles.
3. The days where more than 1% of requests led to errors.
