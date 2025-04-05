import pandas
from util.teams_class import Teams
import pandas as pd


def init(file):
    df = pd.read_csv(file)
    # print(df.to_string())
    teams = Teams(division=1)
    for index, row in df.iterrows():
        poke_list = []
        coach = None
        pos = 0
        for name, item in row.items():
            if pos == 0:
                coach = item
            else:
                poke_list.append(item)
            pos += 1

        teams.add_coach(coach=coach, poke_list=poke_list)

    return teams
