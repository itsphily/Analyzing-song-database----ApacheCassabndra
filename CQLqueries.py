
# Drop and Create the database
drop_database = """ DROP KEYSPACE IF EXISTS udacity"""
create_database = """ CREATE KEYSPACE IF NOT EXISTS udacity 
WITH REPLICATION = {'class' : 'SimpleStrategy' , 'replication_factor' : 1 }
"""


# Drop and Create the music_library_table
music_library_drop = """DROP TABLE IF EXISTS music_library"""
music_library_create = """CREATE TABLE IF NOT EXISTS music_library
(year int, artist_name text, album_name text, PRIMARY KEY(year, artist_name))"""
# Insert into music_library
music_library_insert = """ INSERT into music_library (year, artist_name, album_name) VALUES(%s, %s, %s)"""


# Drop and Create the artist_library_table
artist_library_drop = """DROP TABLE IF EXISTS artist_library"""
artist_library_create = """ CREATE TABLE IF NOT EXISTS artist_library
(artist_name text, year int, album_name text, PRIMARY KEY(artist_name, year))"""
# Insert into artist_library
artist_library_insert = """ INSERT into artist_library (artist_name, year, album_name) VALUES(%s, %s, %s)"""


# Drop and Create the album_library_table
album_library_drop = """DROP TABLE IF EXISTS album_library"""
album_library_create = """ CREATE TABLE IF NOT EXISTS album_library
( album_name text, artist_name text,  year int,  PRIMARY KEY(album_name, year))"""
# Insert into album_library
album_library_insert = """ INSERT into album_library (album_name, artist_name, year) VALUES(%s, %s, %s)"""


#Queries
# Albums in  music library that was released in a given year
album_year = ''' SELECT * FROM music_library WHERE YEAR = %s
'''
# Album in my music library that was created by a given artist
album_artist = ''' SELECT * FROM artist_library WHERE artist_name = %s
'''
#  All the information from the music library about a given album
album_info = 'SELECT * FROM album_library WHERE album_name = %s'
