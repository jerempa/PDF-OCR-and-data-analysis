import requests

#https://www.transfermarkt.com/quickselect/teams/GB2
#https://www.transfermarkt.com/quickselect/teams/GB1
#https://www.transfermarkt.com/quickselect/teams/GB3

def get_request():
    url_bpl = 'https://www.transfermarkt.com/quickselect/teams/GB1'
    url_champ = 'https://www.transfermarkt.com/quickselect/teams/GB2'
    url_l1 = 'https://www.transfermarkt.com/quickselect/teams/GB3'
    url_l2 = 'https://www.transfermarkt.com/quickselect/teams/GB4'
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    response_bpl = requests.get(url_bpl, headers=headers)
    response_champ = requests.get(url_champ, headers=headers)
    response_l1 = requests.get(url_l1, headers=headers)
    response_l2 = requests.get(url_l2, headers=headers)


    print(response_bpl.status_code, response_bpl, response_bpl.text)
    print(response_champ.status_code, response_champ, response_champ.text)
    print(response_l1.status_code, response_l1, response_l1.text)
    print(response_l2.status_code, response_l2, response_l2.text)