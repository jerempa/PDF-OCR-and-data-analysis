import os
# from main import main
from file_operations import file_handling
import csv
import json

# balance_sheet_dict = {
#     "Fixed assets": None,
#     "Intangible assets": None,
#     "Tangible assets": None,
#     "Current assets": None,
#     "Stocks": None,
#     "Debtors: due within one year": None,
#     "Debtors: due after more than one year": None,
#     "Cash at bank and in hand": None,
#     "Creditors: amounts falling due within one year": None,
#     "Net current liabilities": None,
#     "Total assets less current liabilities": None,
#     "Creditors: amounts falling due after more than one year": None,
#     "Net liabilities": None,
#     "Capital and reserves": None,
#     "Called up share capital": None,
#     "Share premium account": None,
#     "Unrealised profit reserve": None,
#     "Profit and loss account": None,
#     "Shareholders deficit": None
# }

balance_sheet_keywords = [
    # "fixed assets",
    # "intangible assets",
    # "tangible assets",
    # "investments",
    # "other investments",
    # # "current assets",
    # "stocks",
    # #"stock",
    # "debtors",
    # "debtors: due within one year",
    # "debtors: due after more than one year",
    # "cash at bank and in hand",
    "creditors: amounts falling due within one year",
    "within one year",
    "creditors: amounts falling due after more than one year",
    "more than one year",
    "after more than one year",
    # "net current liabilities",
    # "net current assets",
    # "total assets less current liabilities",
    # "net liabilities",
    # # "capital and reserves",
    # "called up share capital",
    # "capital redemption reserve",
    # "share premium",
    # "retained earnings",
    # "minority interests",
    # "share premium account",
    # "unrealised profit reserve",
    # # "profit and loss account",
    # "shareholders deficit",
    # "total equity",
    # 'shareholders funds',
    # "shareholders' funds",
    # 'net shareholder funds'
]

# pala_keywords = ['turnover', 'revenue', 'cost of sales', 'gross profit', 'gross loss', 'gross profit/loss',
#                  'administrative expenses', 'other operating income', 'profit on ordinary activities before taxation'
#                                                                       'loss on ordinary activities before taxation',
#                  'administrative and operational costs',
#                  'profit/(loss) before taxation',
#                  'operating profit', 'profit before taxation', 'loss before taxation',
#                  'loss on ordinary activities before taxation', 'profit on ordinary activities before taxation',
#                  'operating loss', 'operating profit/loss' 'interest receivable and similar income',
#                  'interest payable and similar expenses', 'interest receivable', 'interest payable',
#                  'loss on ordinary activities before interest', 'profit on ordinary activities before interest',
#                  'tax on profit', 'tax on loss', 'tax on profit/loss', 'tax on loss on ordinary activities',
#                  'tax on profit on ordinary activities',
#                  'profit for the financial period', 'loss for the financial period',
#                  'profit/(loss) for the financial period', 'retained loss for the year', 'retained profit for the year'
#                  'profit for the period', 'loss for the period', 'profit/(loss) for the period',
#                  'profit for the year', 'loss for the year', 'profit/(loss) for the year',
#                  'profit for the financial year', 'loss for the financial year', 'profit/(loss) for the financial year']


years = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']



def main():
    team_and_files = file_handling.get_filenames('Financial statements in csv')
    data = file_reading(team_and_files)
    #print(data)
    # with open("financial_statement_values.txt", "w") as f:
    #     data_str = json.dumps(data)
    #     #print(data_str)
    #     f.write(data_str)
    #print(data)
    jee = {}

    for team, info in data.items():
        idx = 0
        temp_dict = {}
        year_list = []
        header = None
        value_list = []
        for string, value in info.items():
            #header = None
            #print(team, string, value)
            for name, number in value.items():
                #print(team, string, years[idx])
                #print(year_list)
                #print(string, name, number, year_list)
                header = name
                #print(name, number)
                if string not in year_list:
                    if int(string) != int(years[idx]):
                        value_list.append(None)
                        while int(string) != int(years[idx]):
                            idx += 1
                            if int(string) == int(years[idx]):
                                number = number.replace('(', '-').replace(')', '')
                                value_list.append(number)
                                break
                            value_list.append(None)
                    else:
                        number = number.replace('(', '-').replace(')', '')
                        value_list.append(number)
                    idx += 1
                    year_list.append(string)
                #print(header, team, value_list)
                # try:
                #     jee[team][header] = value_list
                # except KeyError:
                #     pass
                #     jee[team] = {header: value_list}
                temp_dict[header] = value_list
                # except KeyError:
                #     temp_dict[team] = {header: value_list}
                #print(team, string, name, number)

    #temp_dict[team][header] = value_list
        #print(header, team)
        # try:
        #     jee[team][header] = value_list
        # except KeyError:
        #     pass
        #     jee[team] = {header: value_list}
        #rint(jee)
        jee[team] = temp_dict

    #print(json.dumps(jee))

    result = {}
    for team, years1 in data.items():
        team_dict = {}
        for year in range(1999, 2022):
            year_dict = years1.get(year, {})
            for value_name, value in year_dict.items():
                if value_name not in team_dict:
                    team_dict[value_name] = [None] * (2022 - 1999)
                team_dict[value_name][year - 1999] = value
        result[team] = team_dict

    #print(json.dumps(result))

    for team, data in result.items():
        print(team, json.dumps(data))
        print("\n")
    # for team, data in jee.items():
    #     print(json.dumps(data))
    # for team, lst in jee.items():
    #     print(team, len(lst), len(years))
    # for year, year_data in data.items():
    #     #print("Year:", year)
    #     for key, value in year_data.items():
    #         #pass
    #         #print(key)
    #         print(year, key, ":", value)
    #         #print(key, ":", value)


def file_reading(team_and_files):
    data = {}
    done_teams = []
    for team, team_directory in team_and_files.items():
        if os.path.basename(os.getcwd()) in done_teams:
            os.chdir('../..')
        os.chdir(f'{os.getcwd()}/Financial statements in csv/{team}')
        for csv_file in team_directory:
            years = csv_file[len(team):len(csv_file) - 4]
            this_year = years.split('-')[1]
            last_year = years.split('-')[0]
            process_csv_file(data, team, this_year, last_year, csv_file, new_keywords)
            done_teams.append(team)
    return data #loop through files and call another function


def process_csv_file(data, team, this_year, last_year, csv_file, keywords):
    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter=",")
        try:
            for index, row in enumerate(reader):
                for i in range(1, len(row) + 1):
                    keyword = " ".join(row[:i]).lower()
                    try:
                        values = determine_values(row)
                        this_year_value = values[0]
                        last_year_value = values[1]
                        if keyword in keywords:
                            #print(team, keyword, this_year, this_year_value, last_year, last_year_value)
                            # try:
                            #     this_year_value = int(this_year_value)
                            #     last_year_value =
                            add_to_dict(data, team, int(this_year), int(last_year), keyword, this_year_value, last_year_value)
                    except IndexError:
                        pass
        except UnicodeError:
            pass #process the csv files and add correct values to a dict


def determine_values(line):
    this_year_value = line[len(line) - 2]
    last_year_value = line[len(line) - 1]

    #this_year_value = this_year_value.replace('(', '').replace(')', '')
    #last_year_value = last_year_value.replace('(', '').replace(')', '')

    this_year_value = this_year_value.replace('"', '')
    last_year_value = last_year_value.replace('"', '')

    # this_year_value = this_year_value.replace(',', '')
    # last_year_value = last_year_value.replace(',', '')
    #
    #
    # try:
    #     this_year_value = int(this_year_value)
    #     last_year_value = int(last_year_value)
    #
    #
    #     #return True
    # except ValueError:
    #     pass

    return this_year_value, last_year_value #process the given input, remove unnecessary characters


def add_to_dict(data, team, this_year, last_year, keyword, this_year_value, last_year_value):
    if team in data:
        if this_year not in data[team]:
            data[team][last_year] = {}
            data[team][this_year] = {}
        #print(keyword)
        if keyword not in data[team][this_year] and keyword not in data[team][last_year]:
            data[team][last_year][keyword] = last_year_value
            data[team][this_year][keyword] = this_year_value
        if ',' in this_year_value:
            data[team][this_year][keyword] = this_year_value
        if ',' in last_year_value:
            data[team][last_year][keyword] = last_year_value
        # if keyword == 'turnover':
        #     if ',' in this_year_value:
        #         data[team][this_year][keyword] = this_year_value
        #     if ',' in last_year_value:
        #         data[team][last_year][keyword] = last_year_value #checking if the turnover value has been found from the profit and loss account
    else:
        data[team] = {last_year: {keyword: last_year_value},
                      this_year: {keyword: this_year_value}}
    return data #add the given data to a nested dict

# main()
