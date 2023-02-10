import re
import os
#from main import main
import file_handling

balance_sheet_dict = {
    "Fixed assets": None,
    "Intangible assets": None,
    "Tangible assets": None,
    "Current assets": None,
    "Stocks": None,
    "Debtors: due within one year": None,
    "Debtors: due after more than one year": None,
    "Cash at bank and in hand": None,
    "Creditors: amounts falling due within one year": None,
    "Net current liabilities": None,
    "Total assets less current liabilities": None,
    "Creditors: amounts falling due after more than one year": None,
    "Net liabilities": None,
    "Capital and reserves": None,
    "Called up share capital": None,
    "Share premium account": None,
    "Unrealised profit reserve": None,
    "Profit and loss account": None,
    "Shareholders deficit": None
}





# def main():
#     reg_exp_extraction()

def reg_exp_extraction():
    team_and_files = file_handling.get_filenames('Financial statements in txt')
    #print(team_and_files)
    #print(os.getcwd())
    f = open(f'{os.getcwd()}/Financial statements in txt/Leeds/Leeds 2020-2021.txt', 'r')
    file_reading(f, '2020-2021', 'Leeds')
    # os.chdir(f'{os.getcwd()}/Financial statements in txt')
    # for team, file in team_and_files.items():
    #     os.chdir(f'{os.getcwd()}/{team}')
    #     for files in file:
    #         f = open(files, 'r')
    #         file_reading(f)
        #print(team)
        #print(os.getcwd())

def file_reading(file, season, team):
    this_year = season.split('-')[1]
    last_year = season.split('-')[0]
    file = file.readlines()
    #print(latest_year, former_year)
    keywords = ['turnover', 'revenue', 'cost of sales', 'gross profit', 'administrative expenses', 'other operating income', 'profit/(loss)', 'operating profit']
    data = {}
    for index, line in enumerate(file):
        line = line.strip()
        line = line.lower()
        line = line.split()
        string_with_spaces = " ".join(line[:2])
        string_with_spaces1 = " ".join(line[:3])

        try:
            values = determine_values(line)
            this_year_value = values[0]
            last_year_value = values[1]
            if string_with_spaces in keywords:
                add_to_dict(data, team, this_year, last_year, string_with_spaces, this_year_value, last_year_value)
            elif string_with_spaces1 in keywords:
                add_to_dict(data, team, this_year, last_year, string_with_spaces1, this_year_value, last_year_value)
            elif line[0] in keywords:
                add_to_dict(data, team, this_year, last_year, line[0], this_year_value, last_year_value)
            elif line[2] == this_year[2:] and file[index + 1][1] == '£':
                pass
                #print(file[index], file[index + 1])
                #print(line[index + 1])
                #print(line[2])
        except IndexError:
            pass
        #print(line)
    print(data)
    #file.close()

def determine_values(line):
    this_year_value = line[len(line) - 2]
    last_year_value = line[len(line) - 1]
    this_year_value = this_year_value.replace('(', '').replace(')', '')
    last_year_value = last_year_value.replace('(', '').replace(')', '')

    return this_year_value, last_year_value


def add_to_dict(data, team, this_year, last_year, string_with_spaces, this_year_value, last_year_value):
    if team in data:
        if string_with_spaces not in data[team][this_year]:
            data[team][this_year][string_with_spaces] = this_year_value
            data[team][last_year][string_with_spaces] = last_year_value
    else:
        data[team] = {this_year: {string_with_spaces: this_year_value},
                      last_year: {string_with_spaces: last_year_value}}
    return data

#main()