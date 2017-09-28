#!/usr/bin/env python
# "Database code" for the Udacity Logs Analysis project.

import psycopg2


# This function establishes a database connection.  Use quotes around the
# name of the database when invoking connectDB.  Example, connectDB("news").
def connectDB(databasename):
    try:
        # Open connection to database
        db = psycopg2.connect("dbname={}".format(databasename))
        # Create a cursor object
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error connecting to database")


# This function prints out the results, using the title of the report, the
# results obtained from the SQL query, an optional delimiter to surround
# the first results (such as quotes), and an end tag used to describe the
# data value (such as "views" or "% errors").
def printResult(title, result, delimiter, endtag):
    print title
    print "\n"
    for a, b in result:
        if delimiter == '"':
            dlmtr = '\"'
        elif delimiter == "'":
            dlmtr = "\'"
        else:
            dlmtr = delimiter
        print dlmtr + str(a) + dlmtr + " - " + str(b) + endtag
    print "\n"


def runReport():
    # Connect to the "news" database
    db, cursor = connectDB("news")

    # Setup the first sql query to find the 3 most popular articles.
    # Show the title of the articles from the articles table.
    # Show a count of all the views based on the path from the log table,
    # grouped by the title of the article.
    # Join the articles table and the log table using slug and path as a
    # condition since they are related.
    # Concat '%' to the beginning of slug, since the beginning path name
    # may differ.
    # Order the table so that it displays by number of highest views first.
    # Show only the top 3 results.
    query1 = """select articles.title, count(*) as views
                from articles, log
                where log.path like concat('%', articles.slug)
                group by articles.title
                order by views desc
                limit 3;"""

    # Run SQL command with cursor object
    cursor.execute(query1)

    # Store first results into a variable, result1
    result1 = cursor.fetchall()

    # Setup the second sql query to find the most popular authors based on
    # most page views from all articles.
    # Show the name column from the authors table.
    # Show a count of all the views based on the path from the log table,
    # grouped by the name of the author.
    # Join the articles table, log table, and the authors table
    # using id from author with author from articles, and slug from articles
    # with path from log.
    # Concat '%' to the beginning of slug, since the beginning path name may
    # differ.
    # Group the results by authors.
    # Order the table so that it displays by number of highest views first.
    query2 = """select authors.name, count(*) as views
                from authors, articles, log
                where authors.id = articles.author
                and log.path like concat('%', articles.slug)
                group by authors.name
                order by views desc;"""
    cursor.execute(query2)
    result2 = cursor.fetchall()

    # Setup the third sql query to find the days where more than 1% of requests
    # led to errors.
    # Show by date from the log table by casting the time stamp as date.
    # Show the percentage of errors by dividing the total errors by the
    # total responses.
    # Perform a self join where the first table is a count of all the responses
    # and the second table is a count of all the errors.
    # Group by date to view the number of requests/responses by date for each
    # table.
    # Use the date as the key for comparison.
    # Show only results where the number of errors is 1% or more.
    # Results are rounded to two decimal places.
    query3 = """select to_char(total.time, 'Month DD, YYYY') as date,
                round((cast(total_errors.errors as decimal) /
                       cast(total.responses as decimal) * 100),2)
                       as percent_errors
                from (select cast(time as date), count(*) as responses
                      from log
                      group by cast(time as date))
                      as total,
                     (select cast(time as date), count(*) as errors
                      from log
                      where status != ('200 OK')
                      group by cast(time as date))
                      as total_errors
                where total.time = total_errors.time
                and round((cast(total_errors.errors as decimal) /
                           cast(total.responses as decimal) * 100),2) >= 1"""
    cursor.execute(query3)
    result3 = cursor.fetchall()

    # Display the results
    printResult("Top 3 most popular articles:", result1, "\"", " views")
    printResult("Most popular Authors:", result2, "", " views")
    printResult("Days where more than 1% of requests led to errors:",
                result3, "", "% errors")

    # Close the connection
    db.close()


runReport()
