import pandas as pd
from file_operations import file_handling

stadium_capacities = {'Brentford FC': [17250, 2, 12763], 'Brighton & Hove Albion': [31800, 12, 8850], 'Leeds United': 37890,
                      'Leicester City': [32273, 21, 22000], 'Nottingham Forest': 30445, 'Southampton FC': [32384, 22, 15200],
                      'Wolverhampton Wanderers': 32050, 'Blackburn Rovers': 31367, 'Blackpool FC': 16220, 'Huddersfield Town': 24500, 'Hull City': 25586,
                      'Norwich City': 27244, 'Queens Park Rangers': 18360, 'Wigan Athletic': 25133,
                      'Bolton Wanderers': 28723, 'Charlton Athletic': 26875,
                      'Derby County': 33597, 'Ipswich Town': 29673, 'Portsmouth FC': 20688}

#'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers'
#'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic'
# 'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC'

#Hull from 2002
#Hull before that 15,160
#Brighton from 2011
#Brighton before that 8,850



def print_df():
    league_level_dicts = file_handling.return_scraped_data_dict()

    # attendances = file_handling.return_scraped_data_dict_attendances()
    # #print(attendances)
    # for team, attendance in attendances.items():
    #     return_attendance_percentage(team, attendance)


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
        try:
            team_df = pd.DataFrame(data)
            team_df['Team'] = team
            team_df = team_df[['Team'] + list(data.keys())]
            team_data.append(team_df)
        except ValueError:
            pass
    #print(team_data)
    # try:
    df = pd.concat(team_data).reset_index(drop=True)

    # except ValueError:
    #     pass
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)


    return df

# def create_bpl_df(teams_dict):
#     #print(team_list)
#     team_data = []
#     for team, data in teams_dict.items():
#         team_df = pd.DataFrame(data)
#         team_df['Team'] = team
#         team_df = team_df[['Team'] + list(data.keys())]
#         team_data.append(team_df)
#     #print(team_data)
#     # try:
#     df = pd.concat(team_data).reset_index(drop=True)
#
#     # except ValueError:
#     #     pass
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.width', 1000)
#
#
#     return df

def return_attendance_percentage(team_name, avg_attendance_list):
    percentages = []
    for team, capacity in stadium_capacities.items():
        if team == team_name:
            for index, attendance in enumerate(avg_attendance_list):
                if not attendance:
                    percentages.append(None)
                    continue
                attendance = int(attendance.replace(',', ''))
                if isinstance(capacity, list) and index >= capacity[1]:
                    percentage = attendance/capacity[2] * 100
                elif isinstance(capacity, list):
                    percentage = attendance / capacity[0] * 100
                else:
                    percentage = attendance / capacity * 100
                percentages.append(round(percentage, 2))

    #print(team_name, percentages)

    return percentages