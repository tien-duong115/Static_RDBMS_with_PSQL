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
    Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       71 non-null     object
 1   1       71 non-null     object
 2   2       71 non-null     object
 3   3       71 non-null     int64 
 4   4       71 non-null     int64 
dtypes: int64(2), object(3)
 
##### artists_table --> dimensional table  --> one to many fact --> artist_id PR keyUNIQUE 
RangeIndex: 69 entries, 0 to 68
Data columns (total 5 columns):
    Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       69 non-null     object
 1   1       69 non-null     object
 2   2       69 non-null     object
 3   3       69 non-null     object
 4   4       69 non-null     object
dtypes: object(5)

##### users_table --> dimentional table --> one to many with fact --> user_id PR key UNIQUE

RangeIndex: 97 entries, 0 to 96
Data columns (total 5 columns):
    Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       97 non-null     int64 
 1   1       97 non-null     object
 2   2       97 non-null     object
 3   3       97 non-null     object
 4   4       97 non-null     object
dtypes: int64(1), object(4)

##### time_table --> deminsional table --> one to many with fact --> start_time PR key UNIQUE
RangeIndex: 6803 entries, 0 to 6802
Data columns (total 7 columns):
    Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   0       6803 non-null   datetime64[ns]
 1   1       6803 non-null   int64         
 2   2       6803 non-null   int64         
 3   3       6803 non-null   int64         
 4   4       6803 non-null   int64         
 5   5       6803 non-null   int64         
 6   6       6803 non-null   int64         
dtypes: datetime64[ns](1), int64(6)

##### Songplay_table --> Fact table --> one to many with fact --> songplay_id PR UNIQUE 
RangeIndex: 6820 entries, 0 to 6819
Data columns (total 9 columns):
    Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   0       6820 non-null   int64         
 1   1       6820 non-null   datetime64[ns]
 2   2       6820 non-null   object        
 3   3       6820 non-null   object        
 4   4       6820 non-null   object        
 5   5       6820 non-null   object        
 6   6       6820 non-null   int64         
 7   7       6820 non-null   object        
 8   8       6820 non-null   object        
dtypes: datetime64[ns](1), int64(2), object(6)

## Repo File Overview
`create_table.py` --> Creating tables script with defined functions in Drop, Create or Insert new table and values into Postgres db

`etl.py` --> Script consist of functions that interates through file PATH folder and process the JSON files, then read the data file and inserted it into postgres db using `sql_queries.py` file

`sql_queries.py` --> script contained pre-defined queries that helps in the DROP, CREATE, INSERT, and UPDATE the connected postgres db

`test.ipynb` --> Use to test postgres database in checking governing data within each table