import os

def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dir = os.path.join(folder, directory)
        if os.path.isdir(dir):
            #global current_team
            #current_team = directory
            #if directory != 'Forest Green Rovers':
            for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file):
                    files.append(filename)
            team_and_files[directory] = files
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


# def return_cur_team():
#     return current_team

def create_dir_for_txt(current_team):
    #print(os.path.basename(os.getcwd()), os.getcwd())
    #print(starting_seasons[current_team], os.getcwd())
    #print(return_cur_team(), os.getcwd())
    try:
        if os.path.basename(os.getcwd()) == current_team:
            pass
        elif os.path.basename(os.getcwd()) == 'Financial statements in txt':
            try:
                os.mkdir(f'{os.getcwd()}/{current_team}')
                os.chdir(f'{os.getcwd()}/{current_team}')
            except FileExistsError:
                os.chdir(f'{os.getcwd()}/{current_team}')
        else:
            os.mkdir(f'{os.getcwd()}/Financial statements in txt')
            os.chdir(f'{os.getcwd()}/Financial statements in txt')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}/Financial statements in txt') #changing and making directories, depending on where the user is
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

def create_dir_for_images(image, team, f_statement_season):
    if os.path.basename(os.getcwd()) == team:
        os.chdir('..')
        if os.path.basename(os.getcwd()) == 'Financial statements in txt':
            os.chdir('..')
    try:
        os.mkdir(f'{os.getcwd()}\Processed images')
        os.chdir(f'{os.getcwd()}\Processed images')
        save_files(image, team, f_statement_season)
        os.chdir('..')
    except FileExistsError:
        os.chdir(f'{os.getcwd()}\Processed images')
        save_files(image, team, f_statement_season)
        os.chdir('..')

def save_files(image, team, f_statement_season):
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