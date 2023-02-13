import re
import os
#from main import main
import file_handling
import csv

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
    #"fixed assets",
    "intangible assets",
    "tangible assets",
    #"current assets",
    "stocks",
    "debtors: due within one year",
    "debtors: due after more than one year",
    "cash at bank and in hand",
    "creditors: amounts falling due within one year",
    "net current liabilities",
    "total assets less current liabilities",
    "creditors: amounts falling due after more than one year",
    "net liabilities",
    #"capital and reserves",
    "called up share capital",
    "share premium account",
    "unrealised profit reserve",
    "profit and loss account",
    "shareholders deficit"
]

pala_keywords = ['turnover', 'revenue', 'cost of sales', 'gross profit', 'gross loss', 'gross profit/loss',
                 'administrative expenses', 'other operating income', 'profit/(loss) before taxation',
                 'operating profit', 'profit before taxation', 'loss before taxation',
                 'operating loss', 'operating profit/loss' 'interest receivable and similar income',
                 'interest payable and similar expenses', 'tax on profit', 'tax on loss', 'tax on profit/loss'
                 'profit for the financial period', 'loss for the financial period', 'profit/(loss) for the financial period']





# def main():
#     reg_exp_extraction()

def reg_exp_extraction():
    team_and_files = file_handling.get_filenames('Financial statements in csv')
    #print(team_and_files)
    #print(os.getcwd())
    file = return_csv_file()
    # for team, files in team_and_files.items():
    #     print(team)
    #f = open(f'{os.getcwd()}/Financial statements in csv/Leeds/Leeds 2020-2021.csv', 'r')
    #print(team_and_files)
    #file_reading(f'{os.getcwd()}/Financial statements in csv/Leeds/Leeds 2020-2021.csv', '2020-2021', 'Leeds', team_and_files)
    file_reading(team_and_files)
    # os.chdir(f'{os.getcwd()}/Financial statements in csv')
    # for team, file in team_and_files.items():
    #     os.chdir(f'{os.getcwd()}/{team}')
    #     for files in file:
    #         f = open(files, 'r')
    #         file_reading(f)
        #print(team)
        #print(os.getcwd())

def file_reading(team_and_files):
    # this_year = season.split('-')[1]
    # last_year = season.split('-')[0]
    #file = file.readlines()
    #print(latest_year, former_year)
    data = {}
    for team, team_directory in team_and_files.items():
        #print(team)
        os.chdir(f'{os.getcwd()}/Financial statements in csv/{team}')
        for csv_file in team_directory:
            #print(os.getcwd())
            years = csv_file[len(team):len(csv_file)-4]
            this_year = years.split('-')[1]
            last_year = years.split('-')[0]
            with open(csv_file, "r") as file:
                print("nice")
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    for i in range(1, len(row) + 1):
                        keyword = " ".join(row[:i]).lower()
                        try:
                            values = determine_values(row)
                            this_year_value = values[0]
                            last_year_value = values[1]
                            if keyword in pala_keywords:
                                add_to_dict(data, team, this_year, last_year, keyword, this_year_value, last_year_value)
                            elif keyword in balance_sheet_keywords:
                                add_to_dict(data, team, this_year, last_year, keyword, this_year_value, last_year_value)
                        except IndexError:
                            pass
    print(data)
    #file.close()

def determine_values(line):
    this_year_value = line[len(line) - 2]
    last_year_value = line[len(line) - 1]

    this_year_value = this_year_value.replace('(', '').replace(')', '')
    last_year_value = last_year_value.replace('(', '').replace(')', '')

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

    return this_year_value, last_year_value



def add_to_dict(data, team, this_year, last_year, string_with_spaces, this_year_value, last_year_value):
    if team in data:
        if this_year not in data[team]:
            data[team][this_year] = {}
            data[team][last_year] = {}
        if string_with_spaces not in data[team][this_year]:
            data[team][this_year][string_with_spaces] = this_year_value
            data[team][last_year][string_with_spaces] = last_year_value
        # except KeyError:
        #     data[team][this_year] = this_year_value
        #     data[team][last_year] = last_year_value
    else:
        data[team] = {this_year: {string_with_spaces: this_year_value},
                      last_year: {string_with_spaces: last_year_value}}
    return data

def return_csv_file():
    team_and_files = file_handling.get_filenames('Financial statements in csv')
    print(team_and_files)

#main()