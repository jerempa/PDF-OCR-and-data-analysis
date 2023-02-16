import requests
from bs4 import BeautifulSoup
import pandas as pd

#https://www.transfermarkt.com/quickselect/teams/GB2
#https://www.transfermarkt.com/quickselect/teams/GB1
#https://www.transfermarkt.com/quickselect/teams/GB3

base_url = 'https://www.transfermarkt.com'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

def get_request():
    url_bpl = 'https://www.transfermarkt.com/quickselect/teams/GB1'
    url_champ = 'https://www.transfermarkt.com/quickselect/teams/GB2'
    url_l1 = 'https://www.transfermarkt.com/quickselect/teams/GB3'
    url_l2 = 'https://www.transfermarkt.com/quickselect/teams/GB4'

    res = requests.get('https://www.transfermarkt.com/quickselect/competitions/0', headers=headers)
    print(res, res.text, res.headers['Set-Cookie'])
    cookie = res.headers['Set-Cookie'].split(';')[0]
    #print(cookie)
    cookie = cookie.split('=')[1]
    print(cookie)
    headers['cookie'] = cookie
    print(headers)



    response_bpl = requests.get(url_bpl, headers=headers)
    # response_champ = requests.get(url_champ, headers=headers)
    # response_l1 = requests.get(url_l1, headers=headers)
    # response_l2 = requests.get(url_l2, headers=headers)

    parse_league_and_position(response_bpl.json())


    #print(response_bpl.status_code, response_bpl, response_bpl.text)
    # print(response_champ.status_code, response_champ, response_champ.text)
    # print(response_l1.status_code, response_l1, response_l1.text)
    # print(response_l2.status_code, response_l2, response_l2.text)

def parse_league_and_position(res):
    print(type(res), res)
    #print(headers)
    season_list = []
    league_tier_list = []
    win_list = []
    draw_list = []
    lost_list = []
    goals_and_conceded_goals_list = []
    gd_list = []
    rank_list = []
    manager_list = []
    text = 'platzierungen'
    for data in res:
        if data['name'] == 'Brighton & Hove Albion':
            #print(data)
            url = f'{base_url}{data["link"]}'
            #print(url)
            params = url.split('/')
            params[4] = text
            updated_url = '/'.join(params)
            #print(changed_param)
            #print(updated_url)
            test_res = requests.get(updated_url, headers=headers)
            pageSoup = BeautifulSoup(test_res.content, 'html.parser')
            table = pageSoup.find('table', class_='items')
            rows = table.find_all('tr')[1:]
            #seasons = pageSoup.find_all('td', {'class': 'zentriert'})
            for season in rows:
                cols = season.find_all('td')
                #print(cols)
                #season = cols[1].find('td').text  # extract the season from the link text
                data = [td.text for td in cols]
                try:
                    season = data[0]
                    season_list.append(season)

                    league_tier = data[3]
                    league_tier_list.append(league_tier)

                    wins = data[4]
                    win_list.append(wins)

                    draws = data[5]
                    draw_list.append(draws)

                    losses = data[6]
                    lost_list.append(losses)

                    scored_conceded = data[7]
                    goals_and_conceded_goals_list.append(scored_conceded)

                    gd = data[8]
                    gd_list.append(gd)

                    rank = data[10]
                    rank_list.append(rank)

                    manager = data[11]
                    manager_list.append(manager)
                except IndexError:
                    pass
                #print(data)
                #print(cols)
                #level = cols[3].text
                #rank = cols[10].text
                #print(season, level, rank)
            #print(seasons)
    #print(manager_list)
    df = pd.DataFrame({'Season': season_list, 'League': league_tier_list})
    print(df)
    print(season_list, league_tier_list)
    df.head()
        #print(data)