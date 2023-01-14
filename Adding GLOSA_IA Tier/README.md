# glosa_ia_tier_adder

## Description
This script is used to add a GLOSA_IA tier to ELAN files. It first searches the provided data path and its subfolders for ELAN files, then it checks if the files contain a 'GLOSA_IA' tier and if not, it creates a new tier named 'GLOSA_IA' and adds the annotations from the GLOSA tier to the new one.

## Features
- Adds a GLOSA_IA tier to ELAN files
- Handles misspellings of the GLOSA_IA tier name
- Creates a log file for each processed file

## Requirements
- pympi==1.2.3
- python==3.7

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
