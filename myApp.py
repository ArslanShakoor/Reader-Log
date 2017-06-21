#!/usr/bin/env python

import psycopg2

# establish the datavse connection
try:
    conn = psycopg2.connect("dbname=news")
    
except:
    print "I am unable to connect to the database"

# get the cursor
cur = conn.cursor()

# query no 1 to get the most popular articles by view  
cur.execute("""
 select title ,count(*) as num 
 from articles
 join log 
 on articles.slug=substring(path from 10)
 group by title
 order by num desc
 limit 3
 """) 
rows = cur.fetchall()

print "\n1. What are the most popular three articles of all time?\n"
for row in rows:
    print "   ", row[0], "----", row[1], "views"

# query no 2 to get most popular authors by views
cur.execute("""
 select distinct name, sum(num) as total
 from(select distinct authors.name, substring(log.path from 10),
 count(*) as num 
 from log 
 right join articles 
 on articles.slug=substring(path from 10)
 right join authors on authors.id=articles.author
 group by log.path, authors.name 
 order by num desc) as foo 
 group by name 
 order by total desc
""")

rows = cur.fetchall()

print "\n\n2. Who are the most popular article authors of all time?\n"
for row in rows:
    print "   ", row[0], "----", row[1], "views"

# query no 3 to get more than 1% of request leads to error
cur.execute("""
 select tb1.day, (tb2.sum/tb1.sum * 100) as percentage
 from (select distinct day,sum(num) 
 from(SELECT distinct  status,count(*) as num,(time::date) as day
 from log group by status, (time::date) 
 order by (time::date) desc)as foo 
 group by day order by day) as tb1 
 JOIN (select distinct status,sum(num),day 
 from(SELECT distinct  status,count(*) as num,(time::date) as day 
 from log group by status,(time::date) 
 order by (time::date) desc)as foo 
 where status='404 NOT FOUND' 
 group by status,day order by day) AS tb2 
 on tb1.day = tb2.day 
 where (tb2.sum/tb1.sum * 100) > 1 
 order by (tb2.sum/tb1.sum * 100) desc
 """)    

rows = cur.fetchall()

print "\n\n3. On which days did more than 1% of requests lead to errors? \n"
for row in rows:
    print "   ", row[0], " ", "%.2f" % row[1], "%"
 
# close the communication with database 
cur.close()
conn.close()  