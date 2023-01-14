# project-spanish-dictionary-lsp

## Instructions for Using the Executable Files

### add_glosa_ia_tier.exe

- This executable file is used to add a 'GLOSA_IA' tier to ELAN files in a specified directory.
- To use the executable, double click on it and provide the path to the directory containing the ELAN files and the file extension of the files you want to modify (e.g. 'eaf') when prompted.
- The script will then search for files with the provided file extension in the provided directory and its subfolders and add a 'GLOSA_IA' tier to the files that do not have one.
- The modified files will be saved in the same location as the original files.
- Any errors encountered during the processing of the files will be logged in a log file in the 'logs' directory.

### extract_glosa_ia_tier.exe

- This executable file is used to extract information from ELAN files with a 'GLOSA_IA' tier and write it to an Excel spreadsheet.
- To use the executable, double click on it and provide the path to the directory containing the ELAN files and the output filename when prompted.
- The script will then search for files with a 'GLOSA_IA' tier in the provided directory and its subfolders and extract information from that tier and write it to an Excel spreadsheet with the provided output filename.
- The Excel spreadsheet will be saved in the working directory.
- Any errors encountered during the processing of the files will be logged in a log file in the 'logs' directory.


## Structure

The project has the following structure:
      
    .
    │
    ├── data
    │   ├── ABRIR
    │   │   ├── ABRIR_1.eaf
    │   │   ├── ABRIR_1.mp4
    │	  │   ├── ABRIR_1.pfsx
    │   │   ├── ABRIR_2.eaf
    │   │   ├── ABRIR_2.mp4
    │	  │   ├── ABRIR_2.pfsx
    │	  │   ├── ...
    │   ├── ABURRIDO/
    │   │   ├── ABURRIDO_1.eaf
    │	  │   ├── ...
    │   ├── ACERCARSE/
    │   │   ├── ACERCARSE_1.eaf
    │	  │   ├── ...
    │   ├── ADIVINA/
    │   │   ├── ADIVINA_1.eaf
    │	  │   ├── ...
    │   ├── AHI/
    │   │   ├── AHI_1.eaf
    │	  │   ├── ...
    │   ├── AHORA/
    │   │   ├── AHORA_1.eaf
    │	  │   ├── ...
    │   ├── ALGUNOS/
    │   │   ├── ALGUNOS_1.eaf
    │	  │   ├── ...
    │   ├── ALLA/
    │   │   ├── ALLA_1.eaf
    │	  │   ├── ...
    │
    ├── logs
    │   ├── extraction_logs/
    │   ├── tier_adder/
    │
    ├── convert_glosa_db_to_xlsx.exe
    │
    ├── glosa_ia_tier_adder.exe

                


## Contact Us

- Carlos Vasquez
[![Gmail Badge](https://img.shields.io/badge/Gmail-100000?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jose.zapana@pucp.edu.pe)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jazg97)

- Gissella Bejarano
[![Gmail Badge 2](https://img.shields.io/badge/Gmail-100000?style=for-the-badge&logo=gmail&logoColor=white)](mailto:e.schmitt@dkfz-heidelberg.de)
[![GitHub Badge 2](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ECSchmitt)

