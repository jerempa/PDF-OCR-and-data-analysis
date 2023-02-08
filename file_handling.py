import os

def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dir = os.path.join(folder, directory)
        if os.path.isdir(dir):
            global current_team
            current_team = directory
            if directory != 'Forest Green Rovers':
                for filename in os.listdir(dir):
                    file = os.path.join(dir, filename)
                    if os.path.isfile(file):
                        files.append(filename)
                team_and_files[directory] = files
    return team_and_files #loop through dir that has team sub-dirs, add their files to a dict


def return_cur_team():
    return current_team

def create_dir_for_txt():
    #print(os.path.basename(os.getcwd()), os.getcwd())
    #print(starting_seasons[current_team], os.getcwd())
    #print(return_cur_team(), os.getcwd())
    try:
        if os.path.basename(os.getcwd()) == return_cur_team():
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