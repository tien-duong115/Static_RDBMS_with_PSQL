import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ Process single file in JSON format and 
    insert into song and artist table 

    * cur --> psql connection variable
    * filepath --> file path to be processed

    OutPut:
    * song_data insert into song table
    * artist_data insert into artists table

    """
    # open song file
    df = pd.DataFrame(pd.read_json(filepath,
                                        lines=True,
                                        orient='columns'))

    
    # insert song record
    song_data = (   df.values[0][6],
                    df.values[0][7],
                    df.values[0][1],
                    df.values[0][9],
                    df.values[0][8])
    cur.execute(song_table_insert, song_data)    
    # insert artist record
    artist_data = ( df.values[0][1],
                    df.values[0][5],
                    df.values[0][4],
                    df.values[0][2],
                    df.values[0][3])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """ Process a single file in JSON format, filtered and converted
    ts column into datatime data type then insert into time_df and user table  

    * cur --> psql connection variable 
    
    * filepath --> file path to be processed

    Output:
    * Insert into time_df table with different time granularity
    * Insert into user_table with user data information
    * Insert into songplay table with matching result from songselect query generated in sql_queries.py

     """

    # open log file
    df = pd.DataFrame(pd.read_json(filepath,
                                        lines=True,
                                        orient='columns'))
    old_df = df
    # filter by NextSong action
    df = df[df['page'] == 'NextSong' ]


    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit ='ms')
    
    # insert time data records
    time_data =     time_data = list(zip(   t.dt.strftime('%Y-%m-%d %I:%M:%S'),
                            t.dt.hour,
                            t.dt.day,
                            t.dt.week,
                            t.dt.month,
                            t.dt.year,
                            t.dt.weekday))
    column_labels = (       'start_time',
                            'hour',
                            'day',
                            'week',
                            'month',
                            'year',
                            'weekday')
  
    time_df = pd.DataFrame( time_data,
                            columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = old_df.get(['userId', 'firstName', 'lastName', 'gender', 'level'])

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert , list(row))

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        start_time = pd.to_datetime(
                    row.ts,
                    unit='ms').strftime(
                    '%Y-%m-%d %I:%M:%S')
        songplay_data = (start_time,
                    row.userId,
                    row.level,
                    str(songid),
                    str(artistid),
                    row.sessionId,
                    row.location,
                    row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    """ Walk through input file path directory

    * cur -->  cursor, connection variable to db
    * conn -->  connection parameter to connect 
    * filepath --> filepath directory to walk through
    * func --> function to be call to enumerate the datafile

    OutPut:
    Within terminal console, printout the file processed
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over  and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname= user= password=")
    cur = conn.cursor()

    process_data(cur, conn, filepath='your file path goes here', func=process_song_file)
    process_data(cur, conn, filepath='your file path goes here', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()