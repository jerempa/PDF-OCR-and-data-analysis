import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


base_url = 'https://www.worldfootball.net'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

teams = ['Brentford FC', 'Brighton & Hove Albion', 'Leeds United', 'Leicester City', 'Nottingham Forest', 'Southampton FC', 'Wolverhampton Wanderers',
         'Blackburn Rovers', 'Blackpool FC', 'Huddersfield Town', 'Hull City', 'Norwich City', 'Queens Park Rangers', 'Wigan Athletic',
         'Bolton Wanderers', 'Charlton Athletic', 'Derby County', 'Ipswich Town', 'Portsmouth FC']

all_seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13',
               '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']

# all_seasons_full = ['2022/2023', '2021/2022', '2020/2021', '2019/2020', '2018/2019', '2017/2018', '2016/2017', '2015/2016',
#                     '2014/2015', '2013/2014', '2012/2013', '2011/2012', '2010/2011', '2009/2010', '2008/2009', '2007/2008',
#                     '2006/2007', '2005/2006', '2004/2005', '2003/2004', '2002/2003', '2001/2002', '2000/2001', '1999/2000']

all_seasons_full = ['2022/23', '2021/22', '2020/21', '2019/20', '2018/19', '2017/18', '2016/17', '2015/16',
                    '2014/15', '2013/14', '2012/13', '2011/12', '2010/11', '2009/10', '2008/09', '2007/08',
                    '2006/07', '2005/06', '2004/05', '2003/04', '2002/03', '2001/02', '2000/01', '1999/00']

stadium_names = [{'Wolverhampton Wanderers': 'Molineux Stadium', 'Wolverhampton Wanderers?': 'Molineux',
                  'Brighton & Hove Albion': 'Amex Stadium', 'Brighton & Hove Albion?': 'Falmer Stadium',
                  'Leeds United': 'Elland Road', 'Southampton': "Saint Mary's", 'Southampton?': 'The Dell',
                  'Leicester City': 'King Power Stadium',
                  'Leicester City?': 'Filbert Street', 'Nottingham Forest': 'City Ground',
                  'Brentford FC': 'Brentford Community Stadium', 'Brentford FC?': 'Griffin Park'},
                 {'Hull City': 'MKM Stadium', 'Hull City?': 'KC Stadium', 'Hull City!': 'KCOM Stadium',
                  'Huddersfield Town': 'John Smith’s Stadium',
                  'Blackpool FC': 'Bloomfield Road', 'Norwich City': 'Carrow Road', 'Wigan Athletic': 'DW Stadium',
                  'Wigan Athletic?': 'JJB Stadium',
                  'Queens Park Rangers': 'Loftus Road', 'Blackburn Rovers': 'Ewood Park'},
                 {'Derby County': 'Pride Park Stadium', 'Portsmouth FC': 'Fratton Park',
                  'Bolton Wanderers': 'University of Bolton Stadium', 'Bolton Wanderers?': 'Reebok Stadium',
                  'Bolton Wanderers!': 'Macron Stadium', 'Charlton Athletic': 'The Valley',
                  'Ipswich Town': 'Portman Road'}
                 ]

def main():
    url_bpl = 'https://www.worldfootball.net/competition/eng-premier-league/'
    url_champ = 'https://www.worldfootball.net/competition/eng-championship/'
    url_l1 = 'https://www.worldfootball.net/competition/eng-league-one/'
    url_l2 = 'https://www.worldfootball.net/competition/eng-league-two/'

    # response_bpl = requests.get(url_bpl, headers=headers)
    # response_champ = requests.get(url_champ, headers=headers)
    # response_l1 = requests.get(url_l1, headers=headers)
    # response_l2 = requests.get(url_l2, headers=headers)
    #
    # responses = [response_bpl, response_champ, response_l1, response_l2]

    # for res in responses:
    #     stadium_name_dicts = parse_stadium_name(res.content)
    #     stadium_names.append(stadium_name_dicts)


    #create_urls_for_fetching_capacities(stadium_names)



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

def create_urls_for_fetching_capacities(data):
    #url = f'{base_url}/venues'
    url = f'https://en.wikipedia.org/wiki/'
    #league_to_url = ['/eng-premier-league', '/eng-championship', '/eng-league-one', '/eng-league-two']
    league_to_url = ['_Premier_League', 'EFL_Championship', 'EFL_League_One', 'EFL_League_Two']
    #league_to_url = ['/eng-premier-league']
    capacity_dict = {}
    for season in all_seasons_full:
        temporary_url = url
        #temporary_url += league
        #print(temporary_url)
        for league in league_to_url:
            season = season.replace('/', '-')
            temp_url = temporary_url
            temp_url += f'{season}_{league}'
            #print(temp_url)
            res = requests.get(temp_url, headers=headers)
            soup = BeautifulSoup(res.content, 'html.parser')
            for values in data:
                for team, stadium in values.items():
                    team = team.replace('?', '').replace('!', '')
                    #stadium_td = soup.find_all('td', {'class': ['hell', 'dunkel']})
                    # stadium_td = soup.find_all('td')
                    # for index, row in enumerate(stadium_td):
                    #     if row.get_text().lower() == stadium.lower():
                    #         print(stadium, row[index + 2].get_text())
                    stadium_td = soup.find_all('td')
                    for index, row in enumerate(stadium_td):
                        if row.get_text().strip().lower() == stadium.lower():
                            capacity = stadium_td[index + 1].get_text().strip()
                            try:
                                if team in capacity_dict:
                                    capacity_dict[team][season] = capacity
                                else:
                                    capacity_dict[team] = {season: capacity}
                            except KeyError:
                                pass
                        #stadium_soup = BeautifulSoup(str(row), 'html.parser')
                    #stadium_soup = BeautifulSoup(str(stadium_td[i]), 'html.parser')
                    #td_tags = stadium_soup.find_all('td', {'class': ['hell', 'dunkel']})
                    # try:
                    #     if td_tags[-1].get_text().strip() == stadium:
                    #         capacity = stadium_td[index + 4].get_text().strip()
                    #         if team in capacity_dict:
                    #             capacity_dict[team][season] = capacity
                    #         else:
                    #             capacity_dict[team] = {season: capacity}
                    #         #print(team, stadium, stadium_td[index + 4].get_text().strip(), season)
                    #         #print(td_tags)
                    # except IndexError:
                    #     pass
    print(capacity_dict)