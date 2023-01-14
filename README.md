# Instructions for Using the Executable Files - Management of dataset of ELAN Files

## Adding GLOSA_IA Tier (add_glosa_ia_tier.exe)

- This executable file is used to add a 'GLOSA_IA' tier to ELAN files in a specified directory. (Note: GLOSA_IA could be replaced with any tier name in the source file add_glosa_ia_tier.py
- To use the executable, double click on it and provide the path to the directory containing the ELAN files and the file extension of the files you want to modify (e.g. 'eaf') when prompted.
- The script will then search for files with the provided file extension in the provided directory and its subfolders and add a 'GLOSA_IA' tier to the files that do not have one.
- The modified files will be saved in the same location as the original files.
- Any errors encountered during the processing of the files will be logged in a log file in the 'logs' directory.

### Usage
To use the script, run the file add_glosa_ia_tier.exe and provide the path to the folder containing the ELAN files, and the extension of the ELAN files as input.

**Example**
```
Initializing script glosa_ia_tier_adder.py...

Enther the folder which contains the subfolders of each gloss
FOLDER: 1.VERSIÓN FINAL

Enter the name for the xlsx file
FILENAME: glosas_complete

```
### Output
The script will modify the ELAN files in the provided folder, adding a new 'GLOSA_IA' tier based on the existing 'GLOSA' tier. In case of any errors, they will be logged in the 'logs' folder.

***
## Creating XLSX from ELAN Files (convert_glosa_db_to_xlsx.exe)

- This executable file is used to extract information from ELAN files with a 'GLOSA_IA' tier and write it to an Excel spreadsheet.
- To use the executable, double click on it and provide the path to the directory containing the ELAN files and the output filename when prompted.
- The script will then search for files with a 'GLOSA_IA' tier in the provided directory and its subfolders and extract information from that tier and write it to an Excel spreadsheet with the provided output filename.
- The Excel spreadsheet will be saved in the working directory.
- Any errors encountered during the processing of the files will be logged in a log file in the 'logs' directory.

### Usage
To use the script, run the file convert_glosa_db_to_xlsx.exe and provide the path to the folder containing the ELAN files and the output filename as input.

*Example*
```
Initializing script convert_glosa_db_to_xlsx.py...

Enter the path to the directory containing the files:
FOLDER: 1.VERSIÓN FINAL

Enter the file extension of the files you want to modify (e.g. 'eaf'):
FILE EXTENSION: eaf
```
### Output
The script will create an excel file as the output filename argument in the working directory and log files for each processed file in the 'logs/extraction_logs/' directory. In case of any errors

***
## Structure

The project has the following structure:
      
    .
    │
    ├── data
    │   ├── ABRIR
    │   │   ├── ABRIR_1.eaf
    │   │   ├── ABRIR_1.mp4
    │   │   ├── ABRIR_1.pfsx
    │   │   ├── ...
    │   ├── ABURRIDO/
    │   │   ├── ABURRIDO_1.eaf
    │   │   ├── ...
    │   ├── ACERCARSE/
    │   │   ├── ACERCARSE_1.eaf
    │   │   ├── ...
    │   ├── ...
    │ 
    ├── logs
    │   ├── extraction_logs/
    │   ├── tier_adder/
    │
    ├── convert_glosa_db_to_xlsx.exe
    │
    ├── glosa_ia_tier_adder.exe

                



