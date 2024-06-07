# EasyFileX Tool

![EasyFileX Logo](logo.png)

EasyFileX is a command-line tool designed to simplify file management tasks. Whether you need to list files, count them, find specific text, or perform various file operations, EasyFileX has got you covered!

## Features

- **List Files**: Display a list of files.
- **List Files From Folders**: Display files from folders.
- **List Files with Specific Extension**: List files with a specified extension.
- **List All Files and Folders**: Display a list of all files and folders.
- **Count Files and Folders**: Count the number of files or folders.
- **Copy File(s) to All Folder**: Copy file(s) in all folders.
- **Make Random File**: Generate random files.
- **Make Random Folder**: Generate random folders.
- **Make Custom File**: Create custom files.
- **Make Custom Folder**: Create custom folders.
- **List Files with Sizes**: Display files along with their sizes.
- **Find Text in Existing Files**: Search for text in existing files.
- **Remove Files with Specified Extension**: Delete files with the specified extension.
- **Remove Empty Files from Folders**: Clean up empty files from folders.
- **Remove Empty Folders from Directory**: Clean up empty folders from the directory.

## Usage

```bash
efx -l                     # List files
efx -lF                    # List files from folders
efx -lfx .txt              # List files with the specified extension (.txt)
efx -al                    # List all files and folders
efx -cf                    # Count files
efx -cF                    # Count folders
efx -cfF                   # Count all files and folders
efx -cfaF                  # Copy file in all folder
efx -mf 20,.txt            # Make random file
efx -mF 20                 # Make random folder
efx -mcf file.txt          # Make custom File
efx -mcF folder.txt        # Make custom Folder
efx -fsize                 # List files with sizes
efx -ft "search text"      # Find text in existing files
efx -rx .log               # Remove files with the specified extension (.log)
efx -rmef                  # Remove empty files from folders
efx -rmeF                  # Remove empty folder from dir
efx -d /path/to/dir        # Specify the directory path

```

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/Cyber-Programer/Easy-File-X.git
    ```

2. Navigate to the EasyFileX directory:
    
    ```bash
    cd Easy-File-X
    ```

3. Setup the tool:

    ```bash
    python setup.py
    ```

4. Run file using terminal:
    
    ```bash
    efx -h
    ```


## License

This project is licensed under the MIT License - see the LICENSE file for details.