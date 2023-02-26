import requests
from bs4 import BeautifulSoup

from file_operations import file_handling


links_and_teams = {'Coventry': 'https://find-and-update.company-information.service.gov.uk/company/01788466/filing-history',
                   #'Coventry1': 'https://find-and-update.company-information.service.gov.uk/company/03056875/filing-history',
                   'Bolton': 'https://find-and-update.company-information.service.gov.uk/company/00335699/filing-history',
                   #'Bolton1': 'https://find-and-update.company-information.service.gov.uk/company/11761052/filing-history',
                   #'Shef United': 'https://find-and-update.company-information.service.gov.uk/company/06963761/filing-history',
                   'Shef United': 'https://find-and-update.company-information.service.gov.uk/company/00396956/filing-history',
                   'Bournemouth': 'https://find-and-update.company-information.service.gov.uk/company/02393821/filing-history',
                   'Brentford': 'https://find-and-update.company-information.service.gov.uk/company/03642327/filing-history'}
# links_and_teams = {'Coventry': 'https://find-and-update.company-information.service.gov.uk/company/01788466/filing-history',
#                    'Coventry1': 'https://find-and-update.company-information.service.gov.uk/company/03056875/filing-history',
#                    'Bolton': 'https://find-and-update.company-information.service.gov.uk/company/00335699/filing-history',
#                    'Bolton1': 'https://find-and-update.company-information.service.gov.uk/company/11761052/filing-history',
#                    'Shef United': 'https://find-and-update.company-information.service.gov.uk/company/06963761/filing-history',
#                    'Shef United1': 'https://find-and-update.company-information.service.gov.uk/company/00396956/filing-history',
#                    'Bournemouth': 'https://find-and-update.company-information.service.gov.uk/company/02393821/filing-history',
#                    'Brentford': 'https://find-and-update.company-information.service.gov.uk/company/03642327/filing-history'}
# links_and_teams = {'Charlton': 'https://find-and-update.company-information.service.gov.uk/company/01788466/filing-history',
# 'Blackburn': 'https://find-and-update.company-information.service.gov.uk/company/00053482/filing-history', 'Sunderland': 'https://find-and-update.company-information.service.gov.uk/company/00049116/filing-history',
#                    'Wolves': 'https://find-and-update.company-information.service.gov.uk/company/01989823/filing-history',
#                    'Swansea': 'https://find-and-update.company-information.service.gov.uk/company/00123414/filing-history',
#                    'Norwich': 'https://find-and-update.company-information.service.gov.uk/company/00154044/filing-history'}



def fetch_cookie(url):
    res = requests.get(url)
    set_cookie = res.headers['Set-Cookie']
    set_cookie = set_cookie.split(';')
    sid = set_cookie[1].split(',')
    # ch_cookie_consent = 'ch_cookie_consent=eyJ1c2VySGFzQWxsb3dlZENvb2tpZXMiOiJubyIsImNvb2tpZXNBbGxvd2VkIjpbXX0='
    cookie = f'{set_cookie[0]}fh%3Daccounts;{sid[1]}' #fetching cookie, needed for filtering results on the page

    return cookie

def download_financial_statements():
    for team, url in links_and_teams.items():
        cookie = fetch_cookie(url)
        headers = {'cookie': cookie}
        res = requests.get(url, headers=headers)
        pageSoup = BeautifulSoup(res.content, 'html.parser')
        pdfs = pageSoup.find_all('a')
        for link in pdfs:
            try:
                pdf_url = link['href']
                if pdf_url[len(pdf_url) - 10:] == 'download=0':
                    try:
                        link_text = link.find_previous('td', {'class': 'nowrap'}).text.strip().split('\n')
                        year = link_text[2][-4:]
                        former_part_season = str(int(year) - 1)
                        season = f'{former_part_season}-{year}'
                        parsed_url = url.split('/c')
                        download_url = f'{parsed_url[0]}{pdf_url}'
                        response = requests.get(download_url)
                        file_handling.save_pdfs(response.content, team, season)
                        if year == '2000':
                            break
                    except AttributeError:
                        pass
            except KeyError:
                pass
