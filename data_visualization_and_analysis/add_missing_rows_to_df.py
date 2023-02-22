from data_visualization_and_analysis import values_for_analysis

teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City',
         'Queens Park Rangers', 'Ipswich Town']

def main():
    #print("nice")
    for team in teams:
        df = values_for_analysis.league_tier_throughout_years(team)
        if team == 'Brighton & Hove Albion':
            add_rows_brighton(df)
        #print(df)

def add_rows_brighton(df):
    pass