import requests
from bs4 import BeautifulSoup
import pandas as pd

from file_operations import file_handling

#https://www.transfermarkt.com/quickselect/teams/GB2
#https://www.transfermarkt.com/quickselect/teams/GB1
#https://www.transfermarkt.com/quickselect/teams/GB3

base_url = 'https://www.transfermarkt.com'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']

all_seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13',
               '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']

def get_request():
    url_bpl = 'https://www.transfermarkt.com/quickselect/teams/GB1'
    url_champ = 'https://www.transfermarkt.com/quickselect/teams/GB2'
    url_l1 = 'https://www.transfermarkt.com/quickselect/teams/GB3'
    url_l2 = 'https://www.transfermarkt.com/quickselect/teams/GB4'

    #res = requests.get('https://www.transfermarkt.com/quickselect/competitions/0', headers=headers)
    #print(res, res.text, res.headers['Set-Cookie'])
    #cookie = res.headers['Set-Cookie'].split(';')[0]
    #print(cookie)
    #cookie = cookie.split('=')[1]
    #print(cookie)
    #headers['cookie'] = cookie
    #print(headers)



    response_bpl = requests.get(url_bpl, headers=headers)
    response_champ = requests.get(url_champ, headers=headers)
    response_l1 = requests.get(url_l1, headers=headers)
    response_l2 = requests.get(url_l2, headers=headers)

    urls = [response_bpl, response_champ, response_l1, response_l2]
    # league_level_dicts = []
    # #teams_dict = parse_league_and_position(response_champ.json())
    #
    # for res in urls:
    #     teams_dict = parse_league_and_position(res.json())
    #     league_level_dicts.append(teams_dict)
    #
    # return league_level_dicts

    league_level_dicts = file_handling.return_scraped_data_dict()


    #return league_level_dicts
    # teams_dict
    # create_df_from_dict()

    #return league_level_dicts
    for league_level in league_level_dicts:
        if league_level:
            print(create_df_from_dict(league_level))


    #print(response_bpl.status_code, response_bpl, response_bpl.text)
    # print(response_champ.status_code, response_champ, response_champ.text)
    # print(response_l1.status_code, response_l1, response_l1.text)
    # print(response_l2.status_code, response_l2, response_l2.text)

def parse_league_and_position(res):
    text = 'platzierungen'
    teams_dict = {}
    for data in res:
        team = None
        if data['name'] in teams:
            team = data['name']
            url = f'{base_url}{data["link"]}'
            params = url.split('/')
            params[4] = text
            updated_url = '/'.join(params)
            test_res = requests.get(updated_url, headers=headers)
            pageSoup = BeautifulSoup(test_res.content, 'html.parser')
            table = pageSoup.find('table', class_='items')
            rows = table.find_all('tr')[1:]
            team_data = {
                'Season': [],
                'League': [],
                'League level': [],
                'Wins': [],
                'Draws': [],
                'Losses': [],
                'Goals': [],
                'Goal difference': [],
                'Rank': [],
                'Manager': [],
            }
            #seasons = pageSoup.find_all('td', {'class': 'zentriert'})
            attendance_info = parse_attendance(team, data['link'])
            total_spectators = attendance_info[0]
            avg_attendance = attendance_info[1]

            transfer_values = parse_transfer_values(data['link'])
            arrivals = transfer_values[0]
            departures = transfer_values[1]

            for index, season in enumerate(rows):
                cols = season.find_all('td')
                data = [td.text for td in cols]
                season = data[0]
                try:
                    team_data['Season'].append(data[0])
                    team_data['League'].append(data[2])
                    team_data['League level'].append(data[3])
                    team_data['Wins'].append(data[4])
                    team_data['Draws'].append(data[5])
                    team_data['Losses'].append(data[6])
                    team_data['Goals'].append(data[7])
                    team_data['Goal difference'].append(data[8])
                    team_data['Rank'].append(data[10])
                    team_data['Manager'].append(data[11])
                except IndexError:
                    pass
                if season[0] == '9' or season[0] == '8':
                    break
            if len(team_data['Season']) != len(all_seasons):
                team_data = add_missing_seasons(team_data)

            team_data['Total spectators'] = total_spectators
            team_data['Average attendance'] = avg_attendance

            team_data['Arrivals'] = arrivals
            team_data['Departures'] = departures

            teams_dict[team] = team_data
    return teams_dict

def parse_attendance(team, link):
    url = f'{base_url}{link}'
    params = url.split('/')
    params[4] = 'besucherzahlenentwicklung'
    updated_url = '/'.join(params)

    test_res = requests.get(updated_url, headers=headers)
    pageSoup = BeautifulSoup(test_res.content, 'html.parser')
    table = pageSoup.find('table', class_='items')
    rows = table.find_all('tr')[1:]

    total_spec = []
    avg_attendance = []

    for index, row in enumerate(rows):
        cols = row.find_all('td')
        data = [td.text for td in cols]
        season = data[0]
        #print(data, link)
        if season in all_seasons and season == all_seasons[index]:
            total_spec.append(data[len(data) - 2])
            avg_attendance.append(data[-1])
        try:
            if season != all_seasons[index]:
                total_spec.append(None)
                avg_attendance.append(None)
        except IndexError:
            pass
        if (data[0][0:2] == '99' or data[0][0] == '9' or data[0][0] == '8') and len(avg_attendance) == len(all_seasons):
            break
    return total_spec, avg_attendance

def parse_transfer_values(link):
    url = f'{base_url}{link}'
    params = url.split('/')
    params[4] = 'alletransfers'
    updated_url = '/'.join(params)

    test_res = requests.get(updated_url, headers=headers)
    pageSoup = BeautifulSoup(test_res.content, 'html.parser')
    transfers = pageSoup.find_all('td', class_=['redtext rechts hauptlink', 'greentext rechts hauptlink'])
    arrivals = []
    departures = []
    data = [td.text for td in transfers]

    for index, transfer_sum in enumerate(data):
        if (len(arrivals) == len(all_seasons)) and len(arrivals) == len(departures):
            break
        if index % 2 == 0:
            arrivals.append(transfer_sum)
        else:
            departures.append(transfer_sum)
    return arrivals, departures

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


    #print(df)

def add_missing_seasons(data):
    new_dict = {}
    for key in data:
        new_dict[key] = []

    for season in all_seasons:
        if season not in data['Season']:
            new_dict['Season'].append(season)
            for key in data:
                if key != 'Season':
                    new_dict[key].append(None)
        else:
            index = data['Season'].index(season)
            for key in data:
                new_dict[key].append(data[key][index])

    return new_dict

