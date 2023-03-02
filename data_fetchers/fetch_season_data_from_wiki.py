import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re


base_url = 'https://en.wikipedia.org/wiki/'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

teams = ['Brentford F.C.', 'Brighton & Hove Albion F.C.', 'Leeds United F.C.', 'Leicester City F.C.', 'Nottingham Forest F.C.', 'Southampton F.C.', 'Wolverhampton Wanderers F.C.',
         'Blackburn Rovers F.C.', 'Blackpool F.C.', 'Huddersfield Town A.F.C.', 'Hull City A.F.C.', 'Norwich City F.C.', 'Queens Park Rangers F.C.', 'Wigan Athletic F.C.',
         'Bolton Wanderers F.C.', 'Charlton Athletic F.C.', 'Derby County F.C.', 'Ipswich Town F.C.', 'Portsmouth F.C.']

all_seasons = ['22/23', '21/22', '20/21', '19/20', '18/19', '17/18', '16/17', '15/16', '14/15', '13/14', '12/13',
               '11/12', '10/11', '09/10', '08/09', '07/08', '06/07', '05/06', '04/05', '03/04', '02/03', '01/02', '00/01', '99/00']

all_seasons_full = ['2022/2023', '2021/2022', '2020/2021', '2019/2020', '2018/2019', '2017/2018', '2016/2017', '2015/2016',
                    '2014/2015', '2013/2014', '2012/2013', '2011/2012', '2010/2011', '2009/2010', '2008/2009', '2007/2008',
                    '2006/2007', '2005/2006', '2004/2005', '2003/2004', '2002/2003', '2001/2002', '2000/2001', '1999/2000']

all_seasons_full2 = ['2022/23', '2021/22', '2020/21', '2019/20', '2018/19', '2017/18', '2016/17', '2015/16',
                    '2014/15', '2013/14', '2012/13', '2011/12', '2010/11', '2009/10', '2008/09', '2007/08',
                    '2006/07', '2005/06', '2004/05', '2003/04', '2002/03', '2001/02', '2000/01', '1999/00']

def get_request():

    info_list = []

    for team in teams:
        team = team.replace(' ', '_')
        url = f'{base_url}List_of_{team}_seasons'
        res = requests.get(url, headers=headers)
        team_info = parse_league_position(res.content, team.replace('_', ' '))
        info_list.append(team_info)

    ranks = {}

    for i in info_list:
        for key, value in i.items():
            rank_list = []
            for season, rank in value.items():
                rank_list.append(str(rank))
            rank_list.reverse()
            ranks[key] = rank_list #the information fetched isn't 100 %, however, manually checked before adding to df
    #print(json.dumps(ranks))

def parse_league_position(res, team):
    team_and_rank = {}
    soup = BeautifulSoup(res, 'html.parser')
    tr_tag = soup.find_all('tr')
    #td_tag = tr_tag.find_all('td')
    for data in tr_tag:
        try:
            season = data.find('a').text.strip().replace('–', '/')
            if season in all_seasons_full or season in all_seasons_full2:
                cols = data.find_all('td')
                #print(team, len(cols), cols)
                try:
                    value = cols[8].text.strip()
                    if len(cols) == 14 or len(cols) == 12:
                        value = cols[7].text.strip()
                    elif len(cols) == 17 or len(cols) == 16:
                        value = cols[9].text.strip()
                    elif len(cols) == 18:
                        value = cols[7].text.strip()
                    reg_exp_pattern = r"\d+"

                    value = int(re.findall(reg_exp_pattern, value)[0])
                    if value > 24:
                        value = cols[8].text.strip()
                        value = int(re.findall(reg_exp_pattern, value)[0])
                    # if len(value) == 3:
                    #     value = int(value[0])
                    # elif len(value) == 4:
                    #     value = int(value[:2])
                    # elif len(value) == 5:
                    #     value = int(value[:1])
                    # elif len(value) == 6:
                    #     value = int(value[:1])
                    # elif len(value) == 7:
                    #     value = int(value[0])
                    # elif len(value) == 8:
                    #     value = int(value[:2])
                    if team in team_and_rank:
                        team_and_rank[team][season] = value
                    else:
                        team_and_rank[team] = {season: value}
                    #print(season, value)
                except IndexError:
                    pass
            #print(season, cols)
        except AttributeError:
            pass

    return team_and_rank
