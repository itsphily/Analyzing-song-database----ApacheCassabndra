

from cassandra.cluster import Cluster
from CQLqueries import *

# Connects to Apache Cassandra
cluster = Cluster(['127.0.0.1'])
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
"""    
session.execute(music_library_insert, (1965, 'The Beatles', 'Rubber Soul'))
session.execute(music_library_insert, (1965, 'The Who', 'My Generation'))
session.execute(music_library_insert, (1970, 'The Beatles', 'Let It Be'))
session.execute(music_library_insert, (1966, 'The Monkees', 'The Monkee'))
session.execute(music_library_insert, (1970, 'The Carpenters', 'Close To You'))

# Insert values into artist_library
session.execute(artist_library_insert, ('The Beatles', 1965,  'Rubber Soul'))
session.execute(artist_library_insert, ('The Who', 1965,  'My Generation'))
session.execute(artist_library_insert, ( 'The Beatles', 1970, 'Let It Be'))
session.execute(artist_library_insert, ('The Monkees', 1966, 'The Monkee'))
session.execute(artist_library_insert, ('The Carpenters', 1970, 'Close To You'))

#Insert values into album_library
session.execute(album_library_insert, ('Rubber Soul', 'The Beatles', 1965))
session.execute(album_library_insert, ('My Generation', 'The Who', 1965))
session.execute(album_library_insert, ('Let It Be', 'The Beatles', 1970))
session.execute(album_library_insert, ('The Monkee', 'The Monkees', 1966))
session.execute(album_library_insert, ('Close To You', 'The Carpenters', 1970))
"""

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
