import sqlite3
import sys

#DB Name
conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Requests (message_id integer, owner_id integer)''')

# Save (commit) the changes
conn.commit()

# close connection 
conn.close()