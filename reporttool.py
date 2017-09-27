#!/usr/bin/env python
# "Database code" for the Udacity Logs Analysis project.

import psycopg2

# Open connection to database
db = psycopg2.connect(dbname="news")

# Create a cursor object
c = db.cursor()

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
c.execute(query1)

# Store first results into a variable, result1
result1 = c.fetchall()

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
c.execute(query2)
result2 = c.fetchall()

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
            round((cast(total_errors.errors as decimal) / cast(total.responses
                   as decimal) * 100),2) as percent_errors
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
c.execute(query3)
result3 = c.fetchall()

# Display the results
print "Top 3 most popular articles:"
print "\n"
for article, view in result1:
    print "\"" + article + "\" - " + str(view) + " views"
print "\n"
print "Most popular Authors:"
print "\n"
for author, view in result2:
    print author + " - " + str(view) + " views"
print "\n"
print "Days where more than 1% of requests led to errors:"
print "\n"
for date, errors in result3:
    print date + " - " + str(errors) + "% errors"
print "\n"

# Close the connection
db.close()
