import pympi
import os
import xlsxwriter
import datetime
from fuzzywuzzy.fuzz import token_set_ratio
import time

def log(glosa,LOG_STR):
    subfolder_path = "logs/extraction_logs/"
    # get the current time
    now = datetime.datetime.now()

    # format the time string for use in the file name
    time_string = now.strftime("%Y-%m-%d_%H-%M-%S")

    # create the file name
    file_name = subfolder_path + "/log_" + glosa +"_" + time_string + ".txt"

    # open the file for writing
    with open(file_name, "w") as log_file:
        log_file.write(LOG_STR)


def extraction(path,output):
    # create the subfolder path
    subfolder_path = "logs/extraction_logs/"

    # create the subfolder if it does not exist
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    # raise value errors if path not exist or is not a directory
    if not os.path.exists(path):
        raise ValueError("The provided path does not exist.")
    if not os.path.isdir(path):
        raise ValueError("The provided path is not a directory.")
    # Get list of file paths and filenames for .eaf files in DATA_PATH subfolders
    list_path_file = [path + folder + '/' + file for folder in os.listdir(path) for file in
                      os.listdir(os.path.join(path, folder)) if
                      os.path.isfile(os.path.join(path, folder, file)) and file[-3:] == 'eaf']
    list_file = [file for folder in os.listdir(path) for file in os.listdir(os.path.join(path, folder)) if
                 os.path.isfile(os.path.join(path, folder, file)) and file[-3:] == 'eaf']

    # Create a new Excel file
    workbook = xlsxwriter.Workbook(output+'.xlsx') ### Añadir que puedan darle el nombre del archivo
    worksheet = workbook.add_worksheet()

    # Create a format object
    bold_header_format = workbook.add_format({'bold': True, 'font_size': 14})

    # Write header row
    worksheet.write(0, 0, "ELAN File Name", bold_header_format)
    worksheet.write(0, 1, "GLOSA_IA Tier Info", bold_header_format)
    worksheet.write(0, 2, "Location", bold_header_format)
    # Set column widths
    worksheet.set_column(0, 0, 27)  # Column A
    worksheet.set_column(1, 1, 165)  # Column B
    worksheet.set_column(2, 2, 20)  # Column C
    # Iterate through .eaf file paths
    for n, eaf_file in enumerate(list_path_file):
        # Open .eaf file
        aEAFfile = pympi.Elan.Eaf(eaf_file)
        log_err = ""
        # Check if 'GLOSA_IA' tier is present in .eaf file
        if 'GLOSA_IA' in aEAFfile.tiers:
            dict_gloss = aEAFfile.tiers['GLOSA_IA']
        else:
            tiers = aEAFfile.tiers.keys()


            similar_tiers = [tier for tier in tiers if tier != 'GLOSA' and token_set_ratio(tier, "GLOSA_IA") > token_set_ratio("GLOSA","GLOSA_IA")]
            if len(similar_tiers)>0:
                print(list_path_file[n], ' has tier GLOSA_IA misspelled, their tiers are:', str(list(tiers)))
                log_err = log_err + list_path_file[n] + ' has tier GLOSA_IA misspelled, their tiers are:' + str(list(tiers)) + '\n'
                for tier in similar_tiers:
                    aEAFfile.rename_tier(tier, "GLOSA_IA")
            else:
                log_err = log_err + list_path_file[n]+' has not tier named GLOSA_IA, their tiers are:' + str(list(tiers)) + '\n'
                dict_gloss == 'NA'
            log(str(list_file[n][:-4]),log_err)
        # Create string to write to Excel file
        string_csv = ''
        for key in dict_gloss[0]:
            if dict_gloss == 'NA':
                gloss = 'NA'
            else:
                gloss = dict_gloss[0][key][2]  # get the ANNOTATION_VALUE which is the text or sentence annotation
            print(gloss)

            string_csv = string_csv + gloss + ' '
        l = len(list_file[n])

        worksheet.write(n + 1, 0, list_file[n])
        worksheet.write(n + 1, 1, string_csv)
        worksheet.write(n + 1, 2, list_path_file[n][:-l])

        # Close the Excel file
    workbook.close()

if __name__ == "__main__":
    print("\nInitializing script convert_glosa_db_to_xlsx.py...\n")
    time.sleep(3)
    # Constants for file paths
    print("\nEnter the folder which contains the subfolders of each gloss\n")
    DATA_PATH = input("FOLDER: ")
    DATA_PATH = DATA_PATH + '/'
    print("\nEnter the name for the xlsx file\n")
    OUT_PATH = input("FILENAME: ")
    extraction(path=DATA_PATH,output=OUT_PATH)