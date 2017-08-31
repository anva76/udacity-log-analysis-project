#!/usr/bin/env python3
import psycopg2


# A function that lists most popular articles
def print_most_popular_articles():
    # connect to the database
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    # prepare an SQL query to fetch the needed data
    q = """
         select articles.title, count (log.id) as num
          from articles, log
          where articles.slug = split_part(log.path,'/',3)
           and log.path like '%article%'
           and log.status = '200 OK'
          group by articles.title
          order by num desc
          limit 3;
    """

    # execute the SQL query
    cur.execute(q)
    items = cur.fetchall()

    # print the results
    print ("\n1. Top three most popular articles:")
    for item in items:
        print ("  '{0}' - {1} views".format(item[0], item[1]))

    conn.close()


# A function that lists most popular authors
def print_most_popular_authors():

    # connect to the database
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    # prepare an SQL query to fetch the needed data
    q = """
        select authors.name, count (log.id) as num
        from authors, articles, log
        where authors.id = articles.author
         and articles.slug = split_part(log.path,'/',3)
         and log.path like '%article%'
         and log.status = '200 OK'
        group by authors.name
        order by num desc;
    """

    # execute the SQL query
    cur.execute(q)
    items = cur.fetchall()

    # print the results
    print ("\n2. Top most popular authors:")
    for item in items:
        print ("  {0} - {1} views".format(item[0], item[1]))

    conn.close()


# A function that displays days with high error rates
def print_faulty_days():

    # connect to the database
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    # prepare an SQL query to fetch the needed data
    q = """
      select * from (
       select events.date,
       round (100*events.faults::numeric/totals.total_views::numeric,2) as p
       from (select time::date as date, count(*) as faults
            from log where status != '200 OK' group by date) as events,
            (select time::date as date, count(*) as total_views
            from log group by date) as totals
       where events.date = totals.date) as q1
      where p > 1.0 order by p desc;
    """

    # execute the SQL query
    cur.execute(q)
    items = cur.fetchall()

    # print the results
    print ("\n3. Days when more than 1% of requests led to errors:")
    for item in items:
        print ("  {0} - {1}%".format(item[0], item[1]))

    conn.close()


def main():
    print_most_popular_articles()
    print_most_popular_authors()
    print_faulty_days()
    return 0

main()
