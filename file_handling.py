import os
import correct_seasons

def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dire = os.path.join(folder, directory)
        if directory == 'Hull' or directory == 'Huddersfield':
            if os.path.isdir(dire):
                for filename in os.listdir(dire):
                    file = os.path.join(dire, filename)
                    if os.path.isfile(file):
                        files.append(filename)
                team_and_files[directory] = files
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


# def return_cur_team():
#     return current_team

def create_dir_for_txt(current_team):
    try:
        if os.path.basename(os.getcwd()) == current_team:
            pass
        elif os.path.basename(os.getcwd()) in correct_seasons.return_starting_seasons():
            os.chdir('..')
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
    if os.path.basename(os.getcwd()) == team:
        os.chdir('..')
        if os.path.basename(os.getcwd()) == 'Financial statements in csv':
            os.chdir('..')
    #print(os.getcwd())
    #print('jee', image_arr)
    try:
        os.mkdir(f'{os.getcwd()}\Financial statements jpg')
        os.chdir(f'{os.getcwd()}\Financial statements jpg')
        create_dir_for_teams(image_arr, team, f_statement_season)
        #save_images(image_arr, team, f_statement_season)
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Financial statements jpg')
        create_dir_for_teams(image_arr, team, f_statement_season)
        #save_images(image_arr, team, f_statement_season)
        os.chdir('..')

def create_dir_for_teams(image_arr, team, f_statement_season):
    if os.path.basename(os.getcwd()) == team:
        os.chdir('..')
        if os.path.basename(os.getcwd()) == 'Financial statements in csv':
            os.chdir('..')
    #print(os.getcwd())
    #print('jee', image_arr)
    try:
        os.mkdir(f'{os.getcwd()}\{team}')
        os.chdir(f'{os.getcwd()}\{team}')
        save_images(image_arr, team, f_statement_season)
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\{team}')
        save_images(image_arr, team, f_statement_season)
        os.chdir('..')

def save_images(image_arr, team, f_statement_season):
    #print("jee", f_statement_season)
    try:
        os.mkdir(f'{os.getcwd()}/{f_statement_season}')
        os.chdir(f'{os.getcwd()}/{f_statement_season}')
        # try:
        #     os.mkdir(f'{os.getcwd()}/{f_statement_season}')
        #     os.chdir(f'{os.getcwd()}/{f_statement_season}')
        try:
            for index, img in enumerate(image_arr):
                img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        except OSError:
            pass
        # except FileExistsError:
        #     os.chdir(f'{os.getcwd()}/{team}/{f_statement_season}')
        #     try:
        #         for index, img in enumerate(image_arr):
        #             img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        #     except OSError:
        #         pass
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}/{f_statement_season}')
        # try:
        #     os.mkdir(f'{os.getcwd()}/{f_statement_season}')
        #     os.chdir(f'{os.getcwd()}/{f_statement_season}')
        try:
            for index, img in enumerate(image_arr):
                img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        except OSError:
            pass
        # except FileExistsError:
        #     os.chdir(f'{os.getcwd()}/{team}/{f_statement_season}')
        #     try:
        #         for index, img in enumerate(image_arr):
        #             img.save(f'{team} financial statement {f_statement_season} page {index + 1}.jpg', 'JPEG')
        #     except OSError:
        #         pass
        os.chdir('..')
    #get_correct_dates(team, f_statement_season)

def create_dir_for_processed_images(image, team, f_statement_season):
    if os.path.basename(os.getcwd()) == team:
        os.chdir('..')
        if os.path.basename(os.getcwd()) == 'Financial statements in csv':
            os.chdir('..')
    try:
        os.mkdir(f'{os.getcwd()}\Processed images')
        os.chdir(f'{os.getcwd()}\Processed images')
        save_processed_images(image, team, f_statement_season)
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Processed images')
        save_processed_images(image, team, f_statement_season)
        os.chdir('..')

def save_processed_images(image, team, f_statement_season):
    try:
        os.mkdir(f'{os.getcwd()}\{team}')
        os.chdir(f'{os.getcwd()}\{team}')
        try:
            image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\{team}')
        try:
            image.save(f'{team} financial statement {f_statement_season}.jpg', 'JPEG')
        except OSError:
            pass
        os.chdir('..')
    #get_correct_dates(team, f_statement_season)