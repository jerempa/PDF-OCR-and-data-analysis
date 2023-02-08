from datetime import datetime, timedelta
import file_handling

#first_season = str()
starting_seasons = {'Forest Green Rovers': '2010-2011', 'Ipswich Town': '1999-2000'}
first_seasons = {'Forest Green Rovers': '2010-2011', 'Ipswich Town': '1999-2000'}

def get_correct_dates(date_str):
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
        starting_seasons[file_handling.return_cur_team()] = new_date_str
    except KeyError:
        pass
    #print(new_date_str)
    correct_season = new_date_str

    #return new_date_str

def return_first_season():
    try:
        return first_seasons[file_handling.return_cur_team()]
    except KeyError:
        pass

def return_starting_seasons():
    return starting_seasons

def return_teams_season():
    try:
        return starting_seasons[file_handling.return_cur_team()]
    except KeyError:
        pass