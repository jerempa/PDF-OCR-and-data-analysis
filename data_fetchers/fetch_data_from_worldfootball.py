import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = 'https://www.worldfootball.net'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']

all_seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13',
               '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']

def get_request():
    url_bpl = 'https://www.worldfootball.net/competition/eng-premier-league/'
    url_champ = 'https://www.worldfootball.net/competition/eng-championship/'
    url_l1 = 'https://www.worldfootball.net/competition/eng-league-one/'
    url_l2 = 'https://www.worldfootball.net/competition/eng-league-two/'

    response_bpl = requests.get(url_bpl, headers=headers)
    response_champ = requests.get(url_champ, headers=headers)
    response_l1 = requests.get(url_l1, headers=headers)
    response_l2 = requests.get(url_l2, headers=headers)

    responses = [response_bpl, response_champ, response_l1, response_l2]

    stadium_names = []

    for res in responses:
        stadium_name_dicts = parse_stadium_name(res.content)
        stadium_names.append(stadium_name_dicts)

    for value in stadium_names:
        print(value)


def parse_stadium_name(res):
    team_and_stadium = {}

    soup = BeautifulSoup(res, 'html.parser')
    a_tag = soup.find_all('a')
    for data in a_tag:
        try:
            team_name = data['title']
            if team_name in teams:
                url = f'{base_url}{data["href"]}'

                res_team = requests.get(url, headers=headers)
                teamsoup = BeautifulSoup(res_team.content, 'html.parser')
                tag = teamsoup.find_all('a')
                #
                for row in tag:
                    try:
                        if 'venues' in row['href']:
                            if team_name not in team_and_stadium:
                                team_and_stadium[team_name] = row['title']
                    except KeyError:
                        pass
        except KeyError:
            pass

    return team_and_stadium