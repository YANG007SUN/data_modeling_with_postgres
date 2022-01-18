# **Data Modeling with Postgresql**

## Background
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Repo Purpose
Using python to create an ETL pipelines on multiple `json` files. The ETL pipelines transfer those files into 5 tables (one fact table and 4 dimension tables) in postgres.

## Instructions
1. `create_tables.py` drops and creates tables. **You run this file to reset your tables before each time you run your ETL scripts.**
2. `etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
3. `etl.py` reads and processes files from song_data and log_data and loads them into tables. You can fill this out based on your work in the ETL notebook.
4. `sql_queries.py` contains all your sql queries, and is imported into the last three files above.
5. `config.py` contains the `user name` and `password` for your local or clound postgres. Please make sure update the `user` and `password` before running.



