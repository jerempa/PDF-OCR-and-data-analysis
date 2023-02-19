import pandas as pd
from file_operations import file_handling

stadium_capacities = {'Brighton & Hove Albion': '31,800', 'Leeds': '37,890', 'Blackpool FC': '16,220', 'Huddersfield Town': '24,500', 'Hull City': '25,586',
                      'Queens Park Rangers': '18,360', 'Ipswich Town': '29,673'}


def print_df():
    league_level_dicts = file_handling.return_scraped_data_dict()


    # return league_level_dicts
    # teams_dict
    # create_df_from_dict()

    # return league_level_dicts
    for league_level in league_level_dicts:
        if league_level:
            print(create_df_from_dict(league_level))

def create_df_from_dict(teams_dict):
    team_data = []
    for team, data in teams_dict.items():
        team_df = pd.DataFrame(data)
        team_df['Team'] = team
        team_df = team_df[['Team'] + list(data.keys())]
        team_data.append(team_df)
    #print(team_data)
    # try:
    df = pd.concat(team_data).reset_index(drop=True)

    # except ValueError:
    #     pass
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)


    return df