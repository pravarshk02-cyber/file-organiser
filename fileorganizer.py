import os
import shutil

# Take directory input from the user
directory = input("Enter the directory path: ").strip()

# Check whether the directory exists
if not os.path.isdir(directory):
    print("Directory does not exist!")
    exit()

# File extensions for each category
file_types = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
        ".svg", ".tiff", ".ico"
    ],

    "Docs": [
        ".pdf", ".doc", ".docx", ".txt",
        ".xls", ".xlsx", ".csv",
        ".ppt", ".pptx",
        ".odt", ".ods", ".odp"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".wma", ".m4a", ".opus"
    ],

    "Code": [
        ".py", ".c", ".cpp", ".h", ".java",
        ".js", ".ts", ".html", ".css",
        ".php", ".rb", ".go", ".rs",
        ".swift", ".kt", ".kts",
        ".sql", ".r", ".dart",
        ".sh", ".bat", ".ps1"
    ],

    "Executables": [
        ".exe", ".msi", ".apk", ".app",
        ".com", ".scr"
    ],

    "Archives": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz", ".bz2"
    ]
}

# Go through all items in the directory
for file in os.listdir(directory):

    file_path = os.path.join(directory, file)

    # Skip folders
    if not os.path.isfile(file_path):
        continue

    # Get the file extension
    extension = os.path.splitext(file)[1].lower()

    # Check which category the file belongs to
    for folder, extensions in file_types.items():

        if extension in extensions:

            # Create folder only if needed
            folder_path = os.path.join(directory, folder)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print("Created folder:", folder)

            # Destination path
            destination = os.path.join(folder_path, file)

            # Handle duplicate filenames
            if os.path.exists(destination):
                name, ext = os.path.splitext(file)
                counter = 1

                while os.path.exists(destination):
                    new_file = f"{name}_{counter}{ext}"
                    destination = os.path.join(folder_path, new_file)
                    counter += 1

            # Move the file
            shutil.move(file_path, destination)

            print("Moved:", file, "->", folder)

            break

print("\nFiles organized successfully!")