import requests
from bs4 import BeautifulSoup
import pandas as pd

#https://www.transfermarkt.com/quickselect/teams/GB2
#https://www.transfermarkt.com/quickselect/teams/GB1
#https://www.transfermarkt.com/quickselect/teams/GB3

base_url = 'https://www.transfermarkt.com'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

teams = ['Brighton & Hove Albion', 'Leeds United', 'Blackpool FC' 'Huddersfield Town', 'Hull City', 'Queens Park Rangers', 'Ipswich Town']

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

    test = [response_bpl, response_champ, response_l1, response_l2]
    test1 = []

    for res in test:
        teams_dict = parse_league_and_position(res.json())
        test1.append(teams_dict)
    for dic in test1:
        if dic:
            print(create_df_from_dict(dic))


    #print(response_bpl.status_code, response_bpl, response_bpl.text)
    # print(response_champ.status_code, response_champ, response_champ.text)
    # print(response_l1.status_code, response_l1, response_l1.text)
    # print(response_l2.status_code, response_l2, response_l2.text)

def parse_league_and_position(res):
    #print(type(res), res)
    #print(headers)
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
                'Manager': []
            }
            #seasons = pageSoup.find_all('td', {'class': 'zentriert'})
            for season in rows:
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
            teams_dict[team] = team_data
    return teams_dict

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

    return df

    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    #print(df)



# def loop_through_history_data(rows):
#     season_list = []
#     league_tier_list = []
#     win_list = []
#     draw_list = []
#     lost_list = []
#     goals_and_conceded_goals_list = []
#     gd_list = []
#     rank_list = []
#     manager_list = []
#     for season in rows:
#         cols = season.find_all('td')
#         data = [td.text for td in cols]
#         try:
#             season = data[0]
#             season_list.append(season)
#
#             league_tier = data[3]
#             league_tier_list.append(league_tier)
#
#             wins = data[4]
#             win_list.append(wins)
#
#             draws = data[5]
#             draw_list.append(draws)
#
#             losses = data[6]
#             lost_list.append(losses)
#
#             scored_conceded = data[7]
#             goals_and_conceded_goals_list.append(scored_conceded)
#
#             gd = data[8]
#             gd_list.append(gd)
#
#             rank = data[10]
#             rank_list.append(rank)
#
#             manager = data[11]
#             manager_list.append(manager)
#         except IndexError:
#             pass
#
#     return