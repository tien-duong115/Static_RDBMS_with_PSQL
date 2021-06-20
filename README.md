## Data Modeling With Postgres SQL

#### Quick Start
After installation of Postgrest SQL, python3 with proper dependencies and initialized postgrest setup:
    - Navigate to project file folder and into Script folder
    - Run the following file within console 
    - python3 (mac) or python.exe (window)`create_tables.sql` to create a postgressql database
    - python3 (mac) or python.exe (window)`etl.py` to input all data into database


### Project OverView

Project goal is to setup a database using postgresSQL to help analytics team perform user's behavioral preferences of the most trendy song. The analytics team data is composes of file compress in JSON format, what they want is an easy access to these JSON files. So we will write a python ETL script to processes and insert output into postgres database.

Data folder:
    -   `song_data` file folder
    -   `log_data` file folder


### Database overview


##### The Sparkifydb database have 5 tables:

##### song_table --> dimensional table --> one to many with fact -->  song_id PR keyUNIQUE
RangeIndex: 71 entries, 0 to 70
Data columns (total 5 columns):

##### artists_table --> dimensional table  --> one to many fact --> artist_id PR keyUNIQUE 
RangeIndex: 71 entries, 0 to 70
Data columns (total 5 columns):


##### users_table --> dimentional table --> one to many with fact --> user_id PR key UNIQUE
RangeIndex: 8056 entries, 0 to 8055
Data columns (total 5 columns):

##### time_table --> deminsional table --> one to many with fact --> start_time PR key UNIQUE
RangeIndex: 6820 entries, 0 to 6819
Data columns (total 7 columns):

##### Songplay_table --> Fact table --> one to many with fact --> songplay_id PR UNIQUE 
RangeIndex: 6820 entries, 0 to 6819
Data columns (total 9 columns):
