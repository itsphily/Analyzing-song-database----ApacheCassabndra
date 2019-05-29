
# Description
Create and connect to an apache cassandra database using a python driver.
Create tables based on specific queries, and query those tables.

Make use of PRIMARY KEY to partition the data

# How to run
Start an cassandra cluster (got to your apache cassandra directory and in your command line start apache cassandra)
Once started find the local host address and replace it in the section: Connects to Apache Cassandra in the Apache Cassandra Demo#1.py file.


# Dependencies
Need to have Apache Cassandra installed


# Queries
1. Give me every album in my music library that was released in a given year
2. Give me every album in my music library that was created by a given artist
3. All the information in my music library given an album name
4. Give me every album in my music library that was released in a given year (Using a composite key)
5. Give me every album in my music library that was released by a specific artist (Using a composite key)
6. Give me the city in which the Album "Let It Be" was released

# Tables

*******************************
- __Name: music_library__
- Year
- Artist Name
- Album Name
- Primary KEY (Year, Artist Name)
*******************************
*******************************
- __Name: artist_library__
- Artist Name
- Year
- Album Name
- Primary KEY (Artist Name,Year)
*******************************
*******************************
__Name: album_library__
- Album Name
- Artist Name
- Year
- Primary KEY (Artist Name,Year)
*******************************
*******************************
- __Name: music_library2__
- Year
- Artist Name
- Album Name
- City
- Primary KEY (Year, Artist Name, Album Name)
*******************************
*******************************
- __Name: music_library3__
- Artist Name
- Album Name
- Year
- City
- Primary KEY (Artist Name, Album Name, Year)
*******************************
