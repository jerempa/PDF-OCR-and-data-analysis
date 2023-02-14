import re
import os
# from main import main
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
    # "fixed assets",
    "intangible assets",
    "tangible assets",
    "investments",
    "other investments",
    # "current assets",
    "stocks",
    "debtors",
    "debtors: due within one year",
    "debtors: due after more than one year",
    "cash at bank and in hand",
    "creditors: amounts falling due within one year",
    "net current liabilities",
    "net current assets",
    "total assets less current liabilities",
    "creditors: amounts falling due after more than one year",
    "net liabilities",
    # "capital and reserves",
    "called up share capital",
    "capital redemption reserve",
    "share premium",
    "retained earnings",
    "minority interests",
    "share premium account",
    "unrealised profit reserve",
    # "profit and loss account",
    "shareholders deficit",
    "total equity",
    'shareholders funds'
]

pala_keywords = ['turnover', 'revenue', 'cost of sales', 'gross profit', 'gross loss', 'gross profit/loss',
                 'administrative expenses', 'other operating income', 'profit on ordinary activities before taxation'
                                                                      'loss on ordinary activities before taxation',
                 'profit/(loss) before taxation',
                 'operating profit', 'profit before taxation', 'loss before taxation',
                 'loss on ordinary activities before taxation', 'profit on ordinary activities before taxation',
                 'operating loss', 'operating profit/loss' 'interest receivable and similar income',
                 'interest payable and similar expenses', 'interest receivable', 'interest payable',
                 'loss on ordinary activities before interest', 'profit on ordinary activities before interest',
                 'tax on profit', 'tax on loss', 'tax on profit/loss', 'tax on loss on ordinary activities',
                 'tax on profit on ordinary activities',
                 'profit for the financial period', 'loss for the financial period',
                 'profit/(loss) for the financial period', 'retained loss for the year', 'retained profit for the year'
                 'profit for the period', 'loss for the period', 'profit/(loss) for the period',
                 'profit for the year', 'loss for the year', 'profit/(loss) for the year',
                 'profit for the financial year', 'loss for the financial year', 'profit/(loss) for the financial year']


def main():
    team_and_files = file_handling.get_filenames('Financial statements in csv')
    data = file_reading(team_and_files)
    # print(data['Brighton'])
    data = data['Brighton']
    # for year, year_data in data.items():
    #     #print("Year:", year)
    #     for key, value in year_data.items():
    #         #pass
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
            process_csv_file(data, team, this_year, last_year, csv_file, pala_keywords + balance_sheet_keywords)
            done_teams.append(team)
    print(data)
    return data


def process_csv_file(data, team, this_year, last_year, csv_file, keywords):
    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            for i in range(1, len(row) + 1):
                keyword = " ".join(row[:i]).lower()
                try:
                    values = determine_values(row)
                    this_year_value = values[0]
                    last_year_value = values[1]
                    if keyword in keywords:
                        # try:
                        #     this_year_value = int(this_year_value)
                        #     last_year_value =
                        add_to_dict(data, team, int(this_year), int(last_year), keyword, this_year_value, last_year_value)
                except IndexError:
                    pass


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
    #print(this_year, last_year, string_with_spaces, this_year_value, last_year_value)
    # this_year = int(this_year)
    # last_year = int(last_year)
    if team in data:
        #print(data[team])
        #print(this_year, this_year in data[team], last_year, last_year in data[team])
        if this_year not in data[team]:
            # data[team][last_year] = {string_with_spaces: last_year_value}
            # data[team][this_year] = {string_with_spaces: this_year_value}
            data[team][last_year] = {}
            data[team][this_year] = {}
        # data[team][last_year][string_with_spaces] = last_year_value
        # data[team][this_year][string_with_spaces] = this_year_value
        # elif this_year not in data[team] and last_year in data[team]:
        #     data[team][last_year][string_with_spaces] = last_year_value
        #print(data[team])
        #print(type(this_year))
        if string_with_spaces not in data[team][this_year] and string_with_spaces not in data[team][last_year]:
            data[team][last_year][string_with_spaces] = last_year_value
            data[team][this_year][string_with_spaces] = this_year_value
    else:
        data[team] = {last_year: {string_with_spaces: last_year_value},
                      this_year: {string_with_spaces: this_year_value}}
    return data

# main()
