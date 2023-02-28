import pandas as pd
from file_operations import file_handling

# stadium_capacities = {'Brentford FC': [17250, 2, 12763], 'Brighton & Hove Albion': [31800, 12, 8850], 'Leeds United': 37890,
#                       'Leicester City': [32273, 21, 22000], 'Nottingham Forest': 30445, 'Southampton FC': [32384, 22, 15200],
#                       'Wolverhampton Wanderers': 32050, 'Blackburn Rovers': 31367, 'Blackpool FC': 16220, 'Huddersfield Town': 24500, 'Hull City': 25586,
#                       'Norwich City': 27244, 'Queens Park Rangers': 18360, 'Wigan Athletic': 25133,
#                       'Bolton Wanderers': 28723, 'Charlton Athletic': 26875,
#                       'Derby County': 33597, 'Ipswich Town': 29673, 'Portsmouth FC': 20688}

#stadium_capacities = {'Wolverhampton Wanderers': [31750, 32050, 32050, 32050, 32050, 31700, 30852, 31700, 31700, 31700, 31700, 27670, 29195, 29195, 29303, 29303, 29303, 29303, 29303, 29303, 28500, 28500, 28500, 28500], 'Brighton & Hove Albion': [31800, 31800, 30750, 30750, 30666, 30666, 30750, 30750, 30750, 30750, 28583, 22374, 8850, 8850, 8850, 8850, 8850, 8850, 8850, 8850, 8850, 8850, 8850, 8850], 'Leeds United': [37608, 37792, 37792, 37890, 37890, 37890, 37890, 37890, 37890, 37890, 37890, 37890, 40242, 40242, 40242, 40242, 40242, 40242, 40242, 40242, 40242, 40242, 40242, 40242], 'Leicester City': [32262, 32312, 32261, 32243, 32273, 32273, 32500, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 32312, 22000, 22000, 22000], 'Nottingham Forest': [30445, 30445, 30445, 30445, 30445, 30445, 24357, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576, 30576], 'Brentford FC': [17250, 17250, 17250, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300, 12300], 'Hull City': [25400, 25400, 25586, 25400, 25400, 25404, 25404, 25404, 25400, 25400, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404, 25404], 'Blackpool FC': [17338, 17338, 17338, 17338, 17338, 17338, 16750, 16750, 16750, 16750, 16750, 16750, 16220, 16220, 9700, 9700, 9700, 9700, 9400, 9400, 9400, 9400, 8000, 8000], 'Norwich City': [27244, 27244, 27244, 27244, 27244, 27220, 27244, 27010, 27010, 27244, 27224, 27183, 27183, 26018, 26018, 26018, 26018, 26018, 26018, 24500, 22500, 22500, 22000, 22000], 'Wigan Athletic': [25138, 25133, 25133, 25133, 25133, 25133, 25133, 25138, 25138, 25138, 25133, 25133, 25133, 25138, 25138, 25138, 25138, 25138, 25138, 25138, 25138, 25138, 25138, 25138], 'Queens Park Rangers': [18439, 18439, 18439, 18439, 18439, 18439, 18360, 18000, 18000, 18000, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439, 18439], 'Blackburn Rovers': [31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31154, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367, 31367], 'Derby County': [33600, 33600, 33600, 33600, 33600, 33600, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597, 33597], 'Portsmouth FC': [20620, 19669, 19669, 19669, 21100, 21100, 21100, 20688, 20688, 20688, 20688, 20688, 20688, 20688, 20224, 20688, 20220, 20220, 20220, 20220, 20220, 20220, 20220, 20220], 'Charlton Athletic': [27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111, 27111], 'Ipswich Town': [30311, 30311, 30311, 30311, 30300, 30300, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30311, 30300, 30300, 27300], 'Bolton Wanderers': [28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723, 28723], 'Southampton': [32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 32384, 15200, 15200]}


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
    stadium_capacities_dict = file_handling.return_stadium_capacities()
    percentages = []
    for team, capacity in stadium_capacities_dict.items():
        if team == team_name:
            for index, attendance in enumerate(avg_attendance_list):
                if not attendance:
                    percentages.append(None)
                    continue
                attendance = int(attendance.replace(',', ''))
                percentage = attendance / capacity[index] * 100
                percentages.append(round(percentage, 2))
                # if isinstance(capacity, list) and index >= capacity[1]:
                #     percentage = attendance/capacity[2] * 100
                # elif isinstance(capacity, list):
                #     percentage = attendance / capacity[0] * 100
                # else:
                #     percentage = attendance / capacity * 100
                # percentages.append(round(percentage, 2))

   # print(team_name, percentages)
    #
    return percentages