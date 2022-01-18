# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id INT,\
                                      start_time TIMESTAMP,\
                                      user_id INT,\
                                      level VARCHAR,\
                                      song_id INT,\
                                      artist_id INT,\
                                      session_id INT,\
                                      location VARCHAR,\
                                      user_agent VARCHAR);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id INT,\
                                 first_name VARCHAR,\
                                 last_name VARCHAR,\
                                 gender VARCHAR,\
                                 level VARCHAR);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR,\
                                 title VARCHAR,\
                                 artist_id VARCHAR,\
                                 year INT,\
                                 duration FLOAT);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (artist_id VARCHAR,\
                                 name VARCHAR,\
                                 location VARCHAR,\
                                 latitude FLOAT,\
                                 longitude FLOAT);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP,\
                                 hour INT,\
                                 day INT,\
                                 week INT,\
                                 month INT,\
                                 year INT,\
                                 weekday INT);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title,artist_id,year,duration) \
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artist (artist_id,name,location,latitude,longitude) \
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]