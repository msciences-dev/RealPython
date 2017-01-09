# INSERT Command


# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  c.execute("INSERT INTO population VALUES('Chicago 3', \
    'IL', 4400000)")
  c.execute("INSERT INTO population VALUES('Boston 3', \
    'MA', 800000)")