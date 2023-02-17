import os
import correct_seasons
from PIL import Image
import json

def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dire = os.path.join(folder, directory)
        if os.path.isdir(dire):
            for filename in os.listdir(dire):
                file = os.path.join(dire, filename)
                if os.path.isfile(file):
                    files.append(filename)
            team_and_files[directory] = files
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

def write_scraped_data_to_file(data):
    with open('scraped_data.txt', 'w') as f:
        json.dump(data, f) #write the scraping output to a file to avoid making unnecessary requests

def return_scraped_data_dict():
    teams_dict = None
    try:
        with open('scraped_data.txt', 'r') as f:
            data = f.read()
            teams_dict = json.loads(data)
    except IOError:
        pass

    return teams_dict #return the values for making the df