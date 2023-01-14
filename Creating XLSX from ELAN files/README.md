# Extract GLOSA_IA Tier Info and Write to Excel

This script is used to extract information from ELAN files and write it to an Excel spreadsheet. It first searches the provided data path and its subfolders for ELAN files, then it checks if the files contain a 'GLOSA_IA' tier and if not, it checks for a similar name using fuzzywuzzy library and if it finds a similar name it renames it to GLOSA_IA, if the file contains a 'GLOSA_IA' tier, it extracts the information from that tier and writes it to an Excel spreadsheet.

## Features
- Extracts information from ELAN files
- Writes extracted information to an Excel spreadsheet
- Handles misspellings of the GLOSA_IA tier name
- Creates a log file for each processed file

## Requirements
- pympi
- xlsxwriter
- fuzzywuzzy
- datetime

## Usage
To use the script, provide the path to the directory containing the ELAN files, an the output filename as arguments to the `extraction()` function. The script will create an excel file as the output filename argument in the working directory and log files for each processed file in the 'logs/extraction_logs/' directory. 

## Example
```python
path = 'data/'
output_path = 'output.xlsx'
extraction(path)
´´´
## Note
Any errors encountered during the processing of the files will be logged in the log file created for that file. Make sure to check the log files in case of any issues.