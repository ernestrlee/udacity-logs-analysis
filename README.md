# Udacity Log Analysis Project
## A Python program that uses SQL to gather and display information from a database.

## How to install

1. Start by installing Python 2 to your system.  For the latest version, please visit the [Python website](https://www.python.org/).

2. Install a command line tool such as [Git BASH](https://git-for-windows.github.io/).

3. A virtual machine (VM) must also be installed to run the SQL database server.  For this project, Vagrant and VirtualBox were used.
Files can be found from the links below:
    - https://www.virtualbox.org/wiki/Downloads
    - https://www.vagrantup.com/downloads.html 

4. Configure the the VM using files that can be found in the below link:
    - https://github.com/udacity/fullstack-nanodegree-vm

5. Add the database file, "newsdata.sql".  The link can be found below:
    - https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

    To load the data into your local database, place the file into the vagrant directory.  Use the command:
    ```
    psql -d news -f newsdata.sql
    ```
    This command will use PostgreSQL to connect to the database named "news", run the SQL statements in the file
    "newsdata.sql", and create and populate the tables with data needed for this project.

6. Lastly, download the following file from this Git repository and place it into the same folder as the database file, "news" that was created above:
    - reporttool.py

## How to use the Logs Analysis tool
Follow the below instructions to run the report.
1. Run the command line tool.
2. Start your virtual machine.  If using Vagrant, this is usually done by using the "vagrant up" command followed by "vagrant ssh".
3. Navigate to the directory that contains the "newsdata.sql" database as well as the "reporttool.py" file.
4. Using Python, run the file, "reporttool.py".

The program will run three queries and print out the following information from the database:
1. The top three most popular articles.
2. The most popular authors based on the sum of all articles.
3. The days where more than 1% of requests led to errors.
