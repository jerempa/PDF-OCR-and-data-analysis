import os
from PIL import Image
import json
import csv
import pandas as pd
import numpy as np

import correct_seasons
from error_handling import errors

teams = ["Blackpool FC", "Bolton", "Brentford", "Brighton", "Huddersfield", "Leeds", "Swansea", "Wolves"]
years = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']


def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dire = os.path.join(folder, directory)
        if os.path.isdir(dire):
            if directory in teams:
                for filename in os.listdir(dire):
                    file = os.path.join(dire, filename)
                    if os.path.isfile(file):
                        files.append(filename)
                team_and_files[directory] = files
    #print(team_and_files)
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


# def return_cur_team():
#     return current_team

def create_img_dicts():
    image_dict = dict()
    for team in os.listdir('../Financial statements jpg'):
        path = os.path.join(os.getcwd(), f'Financial statements jpg/{team}')
        if os.path.isdir(path):
            seasons_list = []
            for season in os.listdir(f'Financial statements jpg/{team}'):
                season_images = []
                for img in os.listdir(f'Financial statements jpg/{team}/{season}'):
                    #print(img, season)
                    image = Image.open(f'Financial statements jpg/{team}/{season}/{img}')
                    season_images.append(image)
                seasons_list.append(season_images)
            image_dict[team] = seasons_list # loop through the dir with img-files and create a dict of them
    #print(image_dict)
    return image_dict

def create_dir_for_txt(current_team):
    try:
        if os.path.basename(os.getcwd()) == current_team:
            pass
        elif os.path.basename(os.getcwd()) in correct_seasons.return_starting_seasons():
            os.chdir('../..')
        elif os.path.basename(os.getcwd()) == 'Financial statements in csv':
            try:
                os.mkdir(f'{os.getcwd()}/{current_team}')
                os.chdir(f'{os.getcwd()}/{current_team}')
            except FileExistsError:
                os.chdir(f'{os.getcwd()}/{current_team}')
        else:
            os.mkdir(f'{os.getcwd()}/Financial statements in csv')
            os.chdir(f'{os.getcwd()}/Financial statements in csv')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}/Financial statements in csv') #changing and making directories, depending on where the user is
# def get_filenames(folder):
#     team_and_files = dict()
#     for directory in os.listdir(folder):
#         files = []
#         dir = os.path.join(folder, directory)
#         if os.path.isdir(dir):
#             current_team = directory
#             files = get_team_files(dir, current_team)
#             team_and_files[current_team] = files
#     return team_and_files
#
# def get_team_files(team_folder, team_name):
#     files = []
#     for filename in os.listdir(team_folder):
#         file = os.path.join(team_folder, filename)
#         if os.path.isfile(file):
#             files.append(filename)
#     return files

def create_dir_for_images(image_arr, team, f_statement_season):
    # if os.path.basename(os.getcwd()) == team:
    #     os.chdir('..')
    #     if os.path.basename(os.getcwd()) == 'Financial statements in csv':
    #         os.chdir('..')
    try:
        os.mkdir(f'{os.getcwd()}\Financial statements jpg')
        os.chdir(f'{os.getcwd()}\Financial statements jpg')
        create_dir_for_teams(image_arr, team, f_statement_season)
        os.chdir('../..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Financial statements jpg')
        create_dir_for_teams(image_arr, team, f_statement_season)
        os.chdir('../..') #create financial statements jpg dir and ch to it

def create_dir_for_teams(image_arr, team, f_statement_season):
    # if os.path.basename(os.getcwd()) == team:
    #     os.chdir('..')
    #     if os.path.basename(os.getcwd()) == 'Financial statements in csv':
    #         os.chdir('..')
    try:
        os.mkdir(f'{os.getcwd()}\{team}')
        os.chdir(f'{os.getcwd()}\{team}')
        save_images(image_arr, team, f_statement_season)
        os.chdir('../..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\{team}')
        save_images(image_arr, team, f_statement_season)
        os.chdir('../..') #create team dir inside financial statement jpg and ch to it

def save_images(image_arr, team, f_statement_season):
    try:
        os.mkdir(f'{os.getcwd()}/{f_statement_season}')
        os.chdir(f'{os.getcwd()}/{f_statement_season}')
        try:
            for index, img in enumerate(image_arr):
                img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('../..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}/{f_statement_season}')
        try:
            for index, img in enumerate(image_arr):
                img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('../..') #create img files inside correct dir

def create_dir_for_processed_images(image, team, f_statement_season):
    if os.path.basename(os.getcwd()) == team:
        os.chdir('../..')
        if os.path.basename(os.getcwd()) == 'Financial statements in csv':
            os.chdir('../..')
    try:
        os.mkdir(f'{os.getcwd()}\Processed images')
        os.chdir(f'{os.getcwd()}\Processed images')
        save_processed_images(image, team, f_statement_season)
        os.chdir('../..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Processed images')
        save_processed_images(image, team, f_statement_season)
        os.chdir('../..') #create a directory for processed images

def save_processed_images(image, team, f_statement_season):
    try:
        os.mkdir(f'{os.getcwd()}\{team}')
        os.chdir(f'{os.getcwd()}\{team}')
        try:
            image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('../..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\{team}')
        try:
            image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('../..')
    #save processed images inside correct directory

def save_pdfs(pdf, team, season):
    filename = f'Season {season} {team}'
    save_path = f'{os.getcwd()}/Financial statements/{team}'
    full_path = f'{save_path}/{filename}'
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    #print(full_path)
    #print(pdf, team, season)
    with open(f'{full_path}.pdf', 'wb') as f:
        f.write(pdf)

def calculations_to_csv(filename, type_of_data, data):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        #print(count_rows)
        if file.tell() == 0 or (count_csv_rows(filename) % 28 == 0):
            writer.writerow([type_of_data])

        writer.writerow(data)

def count_csv_rows(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        count = sum(1 for row in reader)
    return count

def write_scraped_data_to_file(data):
    with open('scraped_data4.txt', 'w') as f:
        json.dump(data, f) #write the scraping output to a file to avoid making unnecessary requests

def return_scraped_data_dict(filename):
    teams_dict = None
    try:
        with open(filename, 'r') as f:
            data = f.read()
            teams_dict = json.loads(data)
    except IOError:
        pass

    return teams_dict #return the values for making the df


def return_stadium_capacities():
    teams_dict = None
    try:
        with open('stadium_capacities1.txt', 'r') as f:
            data = f.read()
            data = data.replace("'", "\"")
            try:
                teams_dict = json.loads(data)
            except json.decoder.JSONDecodeError as e:
                print(data)
                print("JSON syntax error: ", e)
    except IOError:
        pass

    capacity_dict = {}

    for key, value in teams_dict.items():
        capacity_list = list()
        for season, capacity in value.items():
            capacity = int(capacity.replace(",", ""))
            capacity_list.append(capacity)
        capacity_dict[key] = capacity_list

    return capacity_dict

def return_transfermarkt_values_from_csv(team, data_header):
    with open("team_data4.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        cur_header = str() #keeping up with what data is read atm
        prem_median = float()
        champ_median = float()
        l1_median = float()
        l2_median = float()
        for row in reader:
            if len(row) == 1:
                cur_header = row[0]
            if row[0] == team and data_header in cur_header:
                prem_median = errors.file_reading_value_errors(row[1])
                champ_median = errors.file_reading_value_errors(row[3])
                l1_median = errors.file_reading_value_errors(row[5])
                l2_median = errors.file_reading_value_errors(row[7])
                return [l2_median, l1_median, champ_median, prem_median]
            #print(row, cur_header)
        #print(reader)

def read_financial_statement_values():
    teams_dict = None
    with open("financial_statement_values.txt", "r") as f:
        data = f.read()
        teams_dict = json.loads(data)
    df = pd.DataFrame.from_dict(teams_dict)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    #print(df['Blackburn'])
    #print(team_df['1999'])
    #testi = team_df['1999']
    #print(team_df)
    # for col in team_df.columns:
    #     year, key = col.split('_')
    #     print(f"{year}: {key}")
    teams = ['Blackburn' , 'Blackpool FC', 'Bolton', 'Brentford', 'Brighton', 'Charlton', 'Coventry',
             'Huddersfield', 'Hull', 'Ipswich Town', 'Leeds', 'QPR', 'Shef United', 'Sunderland', 'Swansea', 'Wolves']
    example_dict = {}
    result = {}
    for team in teams:
        team_df = df[team]
        keys = []
        for i in years:
            temp_df = team_df[i]
            #print(temp_df)
            team_dict = {}
            temp_list = []
            cur_len = 0
            try:
                for key, value in temp_df.items():
                    #print(i, key, value)
                    #print(i, len(temp_df), temp_df)
                    if len(temp_df) > cur_len:
                        if key not in keys:
                            keys.append(key)
                    # print(key, value)
                    temp_list.append({key: value})
            except AttributeError:
                pass
            team_dict[i] = temp_list
            #print(team_dict)
            if team in example_dict:
                example_dict[team][i] = temp_list
            else:
                example_dict[team] = team_dict
       # print(keys)
        #print(len(example_dict), len(teams))
        if len(example_dict) == len(teams):
            #print(example_dict)
            for team, year_data in example_dict.items():
                team_data = {}
                for key in keys:
                    values = []
                    for year, year_values in year_data.items():
                        value_found = False
                        for i in year_values:
                            for avain, arvo in i.items():
                                if avain == key:
                                    values.append(arvo)
                                    value_found = True
                                    break
                            if value_found:
                                break
                        else:
                            values.append(np.nan)
                    team_data[key] = values
                result[team] = team_data
    print(result)
    with open("financial statement data.txt", "w") as f:
        data = json.dumps(result)
        f.write(data)
