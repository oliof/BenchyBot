import sqlite3
import sys

#DB Name
conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE SelfPromotion (user_id integer, date date, channel integer, domain text)''')
c.execute('''CREATE TABLE SelfPromotion_whitelist (site text)''')

# Save (commit) the changes
conn.commit()

# close connection 
conn.close()