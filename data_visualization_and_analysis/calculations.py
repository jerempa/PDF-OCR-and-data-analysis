from data_visualization_and_analysis import values_for_analysis

import statistics

teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']

def main():
    for team in teams:
        df = values_for_analysis.league_tier_throughout_years(team)
        show_average_attendace_to_capacity(df, team)

def show_average_attendace_to_capacity(df, team):
    # for team in teams:
    #     #df = values_for_analysis.league_tier_throughout_years(team)
    #     #print(df)
    #     #print(team)
    premier_league_attendance = []
    championship_attendance = []
    league_one_attendance = []
    #print(df[['League level', 'Average attendance / capacity %']])
    print(f'\n{team}')
    for index, row in df.iterrows():
        if row['Average attendance / capacity %'] > 2.00 and row['Year'] > 1990: #don't take into account covid year without spectators
            if row['League level'] == 'First Tier':
                premier_league_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Second Tier':
                championship_attendance.append(row['Average attendance / capacity %'])
            elif row['League level'] == 'Third Tier':
                league_one_attendance.append(row['Average attendance / capacity %'])
    #print(premier_league_attendance, championship_attendance, league_one_attendance)
    try:
        print(f'Median Premier League: {round(statistics.median(premier_league_attendance), 2)} %'
              f' Median Championship: {round(statistics.median(championship_attendance), 2)} %')
              #f' Median League One: {round(statistics.median(league_one_attendance), 2)} %')
    except statistics.StatisticsError:
        pass
    try:
        print(f'Average Premier League: {round(sum(premier_league_attendance) / len(premier_league_attendance), 2)} %'
              f' Average Championship: {round(sum(championship_attendance) / len(championship_attendance), 2)} %')
              #f' Average League One: {round(sum(league_one_attendance) / len(league_one_attendance), 2)} %')
    except ZeroDivisionError:
        pass

