#model.py
import csv

FOOTBALL_FILE_NAME = 'umfootball.csv'

fb_games = []

def init_ftball(csv_file_name=FOOTBALL_FILE_NAME):
    with open(csv_file_name) as f:
        reader=csv.reader(f)
        next(reader)
        next(reader)
        global fb_games
        fb_games = []
        for r in reader:
            r[1] = int(r[1])
            r[3] = int(r[3])
            r[6] = float(r[6])
            fb_games.append(r)


def get_ftball_seasons(sortby='year', sortorder='desc'):
    global bf_games

    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 6
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(fb_games, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
