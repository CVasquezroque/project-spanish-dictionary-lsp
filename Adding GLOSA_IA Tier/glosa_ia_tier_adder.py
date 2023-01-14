import pympi
import os
import logging
import datetime
import time
def delete_bak(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".bak"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
    return True

def add_glosa_ia_tier(folder_path, file_extension):
    # Input validation
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        raise ValueError("Invalid folder path provided. Please provide a valid path to a directory.")
    if not file_extension.startswith("."):
        file_extension = "." + file_extension

    # Get list of file paths and filenames for files with provided file extension in folder_path subfolders
    list_path_file = [folder_path + folder + '/' + file for folder in os.listdir(folder_path) for file in
                      os.listdir(os.path.join(folder_path, folder)) if
                      os.path.isfile(os.path.join(folder_path, folder, file)) and file.endswith(file_extension)]
    list_file = [file for folder in os.listdir(folder_path) for file in os.listdir(os.path.join(folder_path, folder)) if
                 os.path.isfile(os.path.join(folder_path, folder, file)) and file.endswith(file_extension)]

    # Set up logging
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    subfolder_path = "logs/tier_adder/"
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)


    for n, eaf_file in enumerate(list_path_file):
        aEAFfile = pympi.Elan.Eaf(eaf_file)
        if 'GLOSA_IA' not in aEAFfile.tiers:
            try:
                glosa_annotations = aEAFfile.get_annotation_data_for_tier("GLOSA")
                aEAFfile.add_tier("GLOSA_IA")
                for annotation in glosa_annotations:
                    aEAFfile.add_annotation('GLOSA_IA', annotation[0], annotation[1], annotation[2])
                pympi.Elan.to_eaf(list_path_file[n], aEAFfile)
                print(f'Successfully added GLOSA_IA tier to {list_file[n]}')
            except Exception as e:
                log_file_name = subfolder_path + 'add_glosa_ia_tier_' + time_string + '.log'
                logging.basicConfig(filename=log_file_name, level=logging.ERROR)
                logging.error(f'Error adding GLOSA_IA tier to {list_file[n]}: {e}')
                print(f'Error adding GLOSA_IA tier to {list_file[n]}: {e}')
    delete_bak(folder_path)


if __name__ == '__main__':
    print("\nInitializing script glosa_ia_tier_adder.py...\n")
    time.sleep(3)
    print("\nEnter the path to the directory containing the files:\n")
    folder_path = input("FOLDER: ")
    folder_path = folder_path + '/'
    print("\nEnter the file extension of the files you want to modify (e.g. 'eaf'):\n")
    file_extension = input("FILE EXTENSION: ")
    add_glosa_ia_tier(folder_path, file_extension)
