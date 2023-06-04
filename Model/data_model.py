import pandas as pd
import sqlite3
import csv
from 'Model/top_players.py' import top_players
import os


# Import features from model
def get_data(load_new=False) -> pd.DataFrame:
    db = "chess_games.db"
    con = sqlite3.connect(db)
    cur = con.cursor()
    if load_new:
        # CREATE TABLE
        create_table = '''CREATE TABLE IF NOT EXISTS game(id,
                        INTEGER,
                        player TEXT,
                        player_name TEXT,
                        url TEXT,
                        white_Accuracy TEXT,
                        black_Accuracy TEXT, 
                        Event TEXT,
                        Site TEXT,
                        Date TEXT,
                        White TEXT,
                        Black TEXT,
                        Result TEXT,
                        BlackElo TEXT,
                        ECO TEXT,
                        ECOurl TEXT,
                        EndDate TEXT,
                        EndTime TEXT,
                        Termination TEXT,
                        TimeControl TEXT,
                        WhiteElo TEXT,
                        pgn TEXT,
                        player_rating TEXT
                    )'''
        cur.execute(create_table)
        # READ GAMES FROM CSV
        file = open('Model/GM_games_dataset.csv',  encoding='utf-8')
        contents = csv.reader(file)
        # INSERT INTO SQL DATABASE
        insert_records = '''INSERT INTO game (id,
                        player,
                        player_name,
                        url,
                        white_Accuracy,
                        black_Accuracy,
                        Event,
                        Site,
                        Date,
                        White,
                        Black,
                        Result,
                        BlackElo,
                        ECO,
                        ECOurl,
                        EndDate,
                        EndTime,
                        Termination,
                        TimeControl,
                        WhiteElo,
                        pgn,
                        player_rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.executemany(insert_records, contents)
        con.commit()
    # SELECT ALL VALUES
    select_all = "SELECT White, Black, TimeControl, pgn FROM game WHERE White in " + top_players + " AND Black in " + top_players
    df = pd.read_sql_query(select_all, con)
    con.commit()
    con.close()
    return df
