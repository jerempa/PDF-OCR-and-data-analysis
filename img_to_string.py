import os
import pytesseract
import file_handling
import correct_seasons

def ocr_result_to_txt(img, current_team):
    #print(os.getcwd(), current_team)
    #print(starting_seasons[current_team], os.getcwd())
    #print(os.path.basename(os.getcwd()))
    # if os.path.basename(os.getcwd()) == 'Financial statements in txt':
    #     try:
    #         os.mkdir(f'{os.getcwd()}/{current_team}')
    #         os.chdir(f'{os.getcwd()}/{current_team}')
    #     except FileExistsError:
    #         pass
    #print(os.getcwd())
    #current_team = file_handling.return_cur_team()
    #print(os.getcwd(), current_team, correct_seasons.return_correct_season())
    correct_season = correct_seasons.return_teams_season(current_team)
    #print(current_team, correct_season)
    if os.path.basename(os.getcwd()) == current_team:
        f = open(f'{current_team} {correct_season}.txt', 'a', encoding='utf-8')
        f.write(pytesseract.image_to_string(img))
        f.close()
    file_handling.create_dir_for_txt(current_team)
    #os.chdir(f'{os.getcwd()}\Financial Statements in txt')