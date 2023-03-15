from datetime import datetime, timedelta
#import file_handling

#first_season = str()
starting_seasons = {'Forest Green Rovers': '2010-2011', 'Ipswich Town': '1999-2000',
                    'Blackpool FC': '1999-2000', 'QPR': '2002-2003', 'Hull': '2001-2002', 'Leeds': '2000-2001', 'Huddersfield': '1999-2000', 'Brighton': '1999-2000',
                    'Blackburn': '1999-2000', 'Charlton': '1999-2000', 'Sunderland': '1999-2000', 'Swansea': '1999-2000', 'Wolves': '1999-2000',
                    'Bolton': '1999-2000', 'Brentford': '1999-2000', 'Shef United': '1999-2000', 'Coventry': '1999-2000',
                    "Leicester": '2002-2003', "Bournemouth": "1999-2000", "Norwich": "1999-2000", "Nottingham": "1999-2000", "Portsmouth": "2012-2013",
                    "Southampton": "1999-2000", "Wigan": "1999-2000"}
#first_seasons = {'Forest Green Rovers': '2010-2011', 'Ipswich Town': '1999-2000'}

def get_correct_dates(date_str, current_team):
    #global first_season
    start_year, end_year = [int(x) for x in date_str.split("-")]
    #start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    # print(date_str, return_teams_starting_season())
    # if date_str == return_teams_starting_season():
    #     first_season = date_str

    new_start_date = end_date
    new_end_date = end_date + timedelta(days=365)

    new_date_str = new_start_date.strftime("%Y") + "-" + new_end_date.strftime("%Y")
    try:
        starting_seasons[current_team] = new_date_str
    except KeyError:
        pass
    #print(new_date_str)
    correct_season = new_date_str

    #return new_date_str

# def return_first_season():
#     try:
#         return first_seasons[file_handling.return_cur_team()]
#     except KeyError:
#         pass

def return_starting_seasons():
    return starting_seasons

def return_teams_season(current_team):
    try:
        return starting_seasons[current_team]
    except KeyError:
        pass