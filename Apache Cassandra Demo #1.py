

from cassandra.cluster import Cluster
from CQLqueries import *

# Connects to Apache Cassandra
local_host_address = '127.0.0.1'
cluster = Cluster([local_host_address])
session = cluster.connect()

# Resets and Creates a database
session.execute(drop_database)
session.execute(create_database)

# Connect to the keyspace(database)
session.set_keyspace('udacity')

# Resets and Creates a table music_library
session.execute(music_library_drop)
session.execute(music_library_create)

# Resets and Creates a table artist_library
session.execute(artist_library_drop)
session.execute(artist_library_create)

# Resets and Creates a table album_library
session.execute(album_library_drop)
session.execute(album_library_create)

# Create store the information I want to insert in the tables in a list
year_released = [1965, 1965, 1970, 1966, 1970]
artists = ['The Beatles', 'The Who', 'The Beatles', 'The Monkees', 'The Carpenters']
albums = ['Rubber Soul', 'My Generation', 'Let It Be', 'The Monkees', 'Close To You']

# Insert values into music_library
for i in range(len(year_released)):
    session.execute(music_library_insert, (year_released[i], artists[i], albums[i]))
    session.execute(artist_library_insert, (artists[i], year_released[i], albums[i]))
    session.execute(album_library_insert, (albums[i], artists[i], year_released[i]))

#Testing our queries

#1. Give me every album in my music library that was released in a given year
print('*'*40)
print('All the albums created by The Beatles')
rows = session.execute(album_artist, ['The Beatles'])
for row in rows:
    print(row.artist_name, row.year, row.album_name)
print('*' * 40, '\n')

#2. Give me every album in my album library that was created by a given artist
print('*'*40)
print('All the albums created in 1970')
rows = session.execute(album_year, [1970])
for row in rows:
    print(row.year, row.artist_name, row.album_name)
print('*'*40, '\n')

#3. All the information from the music library about a given album
print('*'*40)
print('All the information about "Close to you"')
rows = session.execute(album_info, ['Close To You'])
for row in rows:
    print(row.album_name, row.artist_name, row.year,)
print('*' * 40)


# Close the session and cluster connection
session.shutdown()
cluster.shutdown()
