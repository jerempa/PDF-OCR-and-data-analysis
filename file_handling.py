import os

def get_filenames(folder):
    team_and_files = dict()
    for directory in os.listdir(folder):
        files = []
        dir = os.path.join(folder, directory)
        if os.path.isdir(dir):
            global current_team
            current_team = directory
            for filename in os.listdir(dir):
                file = os.path.join(dir, filename)
                if os.path.isfile(file):
                    files.append(filename)
            team_and_files[directory] = files
    return team_and_files, current_team #loop through dir that has team sub-dirs, add their files to a dict

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