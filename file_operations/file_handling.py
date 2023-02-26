import os
from PIL import Image
import json
import csv

import correct_seasons

teams = ['Coventry']

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
    print(team_and_files)
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
        if file.tell() == 0 or (count_csv_rows(filename) % 20 == 0):
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

def return_scraped_data_dict():
    teams_dict = None
    try:
        with open('scraped_data4.txt', 'r') as f:
            data = f.read()
            teams_dict = json.loads(data)
    except IOError:
        pass

    return teams_dict #return the values for making the df