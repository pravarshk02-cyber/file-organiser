# file-organiser
Helps in organizing files effectively and saves a lot of time

A Python-based file organization utility that automatically sorts files in a selected directory into category-based folders according to their file extensions.

## Overview

The **File Organizer** helps maintain a clean and structured directory by identifying files based on their extensions and moving them into appropriate folders.

The program uses Python's built-in `os` and `shutil` modules and creates category folders only when matching files are found.

## Features

- Accepts a directory path from the user.
- Verifies that the specified directory exists.
- Automatically identifies files by their extensions.
- Organizes files into the following categories:
  - Images
  - Docs
  - Videos
  - Audio
  - Code
  - Executables
  - Archives
- Creates category folders automatically when required.
- Leaves existing folders untouched.
- Handles duplicate filenames by generating unique filenames.
- Skips directories and processes files only.
- Displays the folders created and files moved during execution.

## Supported File Types

### Images
`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg`, `.tiff`, `.ico`

### Documents
`.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.csv`, `.ppt`, `.pptx`, `.odt`, `.ods`, `.odp`

### Videos
`.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.mpeg`, `.mpg`, `.3gp`

### Audio
`.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma`, `.m4a`, `.opus`

### Code
`.py`, `.c`, `.cpp`, `.h`, `.java`, `.js`, `.ts`, `.html`, `.css`, `.php`, `.rb`, `.go`, `.rs`, `.swift`, `.kt`, `.kts`, `.sql`, `.r`, `.dart`, `.sh`, `.bat`, `.ps1`

### Executables
`.exe`, `.msi`, `.apk`, `.app`, `.com`, `.scr`

### Archives
`.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`

## Requirements

- Python 3.x
- No external Python packages are required.

The project uses the standard Python modules:

os
shutil
