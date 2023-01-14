# Adding a Copy of an existing Tier in ELAN files

## Description
This script is used to add a copy of an existing tier to ELAN files (in this case GLOSA is copied into GLOSA_IA tier). It first searches the provided data path and its subfolders for ELAN files, then it checks if the files contain a 'GLOSA_IA' tier and if not, it creates a new tier named 'GLOSA_IA' and adds the annotations from the GLOSA tier to the new one.

## Features
- Adds a GLOSA_IA tier to ELAN files
- Handles misspellings of the GLOSA_IA tier name
- Creates a log file for each processed file

## Requirements
- pympi-ling>=1.70.2
- python>=3.7

## Inputs
- `folder_path`: path to the directory containing the ELAN files
- `file_extension`: file extension of the files you want to modify (e.g. 'eaf')

## Outputs
- modified ELAN files in the folder provided
- log files for each processed file in the 'logs/' directory

## Usage
```python
folder_path = 'data/'
file_extension = 'eaf'
add_glosa_ia_tier(folder_path, file_extension)
```
## Note
- Any errors encountered during the processing of the files will be logged in the log file created for that file. Make sure to check the log files in case of any issues.
- This script assumes that the folder structure provided has the following format, where each folder represents a word and contains the corresponding ELAN files:
    .
    │
    ├── data
    │   ├── WORD-1/
    │   │   ├── WORD-1_1.eaf
    │   │   ├── WORD-1_1.mp4
    │   │   ├── WORD-1_1.pfsx
    │   │   ├── ...
    │   ├── WORD-2/
    │   │   ├── WORD-2_1.eaf
    │   │   ├── ...
    │   ├── WORD-3/
    │   │   ├── WORD-3_1.eaf
    │   │   ├── ...
    │   ├── ...
    ├── glosa_ia_tier_adder.py
