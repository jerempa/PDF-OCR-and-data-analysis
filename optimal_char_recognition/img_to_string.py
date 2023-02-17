import os
import pytesseract
from file_operations import file_handling
import correct_seasons
import csv

def ocr_result_to_txt(img, current_team):
    correct_season = correct_seasons.return_teams_season(current_team)
    if os.path.basename(os.getcwd()) == current_team:
        print(current_team, correct_season)
        f = open(f'{current_team} {correct_season}.txt', 'a', encoding='utf-8')
        f.write(pytesseract.image_to_string(img))
        f.close()
    file_handling.create_dir_for_txt(current_team)

def ocr_result_to_csv(sorted_data, current_team):
    correct_season = correct_seasons.return_teams_season(current_team)
    if os.path.basename(os.getcwd()) == current_team:
        with open(f'{current_team} {correct_season}.csv', "a", encoding="windows-1252") as file:
            print(current_team, correct_season)
            writer = csv.writer(file)
            current_top = -1
            current_left = -1
            row = []
            tolerance = 12
            for text, left, top in sorted_data:
                if str(text) == "nan":
                    continue
                if current_top == -1 or abs(top - current_top) > tolerance:
                    if row:
                        row = sorted(row, key=lambda x: x[1])
                        writer.writerow([x[0] for x in row])
                    row = []
                    current_top = top
                row.append((text, left))
            if row:
                row = sorted(row, key=lambda x: x[1])
                writer.writerow([x[0] for x in row])
    file_handling.create_dir_for_txt(current_team)