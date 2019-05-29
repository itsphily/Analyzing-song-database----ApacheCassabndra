
# Drop and Create the database
drop_database = """ DROP KEYSPACE IF EXISTS PhilHabra"""
create_database = """ CREATE KEYSPACE IF NOT EXISTS PhilHabra 
WITH REPLICATION = {'class' : 'SimpleStrategy' , 'replication_factor' : 1 }
"""


# Drop and Create the music_library table
music_library_drop = """DROP TABLE IF EXISTS music_library"""
music_library_create = """CREATE TABLE IF NOT EXISTS music_library
(year int, artist_name text, album_name text, PRIMARY KEY(year, artist_name))"""
# Insert into music_library
music_library_insert = """ INSERT into music_library (year, artist_name, album_name) 
VALUES(%s, %s, %s)"""

# Drop and Create the artist_library table
artist_library_drop = """DROP TABLE IF EXISTS artist_library"""
artist_library_create = """ CREATE TABLE IF NOT EXISTS artist_library
(artist_name text, year int, album_name text, PRIMARY KEY(artist_name, year))"""
# Insert into artist_library
artist_library_insert = """ INSERT into artist_library (artist_name, year, album_name) 
VALUES(%s, %s, %s)"""

# Drop and Create the album_library table
album_library_drop = """DROP TABLE IF EXISTS album_library"""
album_library_create = """ CREATE TABLE IF NOT EXISTS album_library
( album_name text, artist_name text,  year int,  PRIMARY KEY(album_name, year))"""
# Insert into album_library
album_library_insert = """ INSERT into album_library (album_name, artist_name, year) 
VALUES(%s, %s, %s)"""

# Drop and Create the music_library2 table
music_library2_drop = """DROP TABLE IF EXISTS music_library2"""
music_library2_create = """CREATE TABLE IF NOT EXISTS music_library2
(year int, artist_name text, album_name text, city text,  PRIMARY KEY((year), artist_name, album_name))"""
# Insert into music_library
music_library2_insert = """ INSERT into music_library2(year, artist_name, album_name, city) 
VALUES(%s, %s, %s, %s)"""

# Drop and Create the music_library3 table
music_library3_drop = """DROP TABLE IF EXISTS music_library3"""
music_library3_create = """CREATE TABLE IF NOT EXISTS music_library3
(artist_name text, album_name text, year int, city text,  PRIMARY KEY((artist_name), album_name, year))"""
# Insert into music_library
music_library3_insert = """ INSERT into music_library3(artist_name, album_name, year, city) 
VALUES(%s, %s, %s, %s)"""

#Queries
# Albums in  music library that was released in a given year
album_year = ''' SELECT * FROM music_library WHERE YEAR = %s
'''
# Album in my music library that was created by a given artist
album_artist = ''' SELECT * FROM artist_library WHERE artist_name = %s
'''
#  All the information from the music library about a given album
album_info = 'SELECT * FROM album_library WHERE album_name = %s'

# All the information from music_library2 for albums released in a specific year
album_year2 = 'SELECT * FROM music_library2 WHERE year = %s'

# All the information from music_library2 for albums created by a specific artist
album_year3 = 'SELECT * FROM music_library3 WHERE artist_name = %s'

# Give me the city in which the Album "Let It Be" was released
city_album = "SELECT city FROM music_library3 WHERE album_name = %s AND artist_name = %s"