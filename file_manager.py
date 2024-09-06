import os
import shutil

def clean_directory(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Dictionary to map file types to their folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.php'],
        'Others': []  # Files with extensions not in the above categories
    }

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_ext = os.path.splitext(file_name)[1].lower()

        # Find the corresponding folder for the file extension
        destination_folder = None
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                destination_folder = folder_name
                break

        # If the file extension does not match any category, move to "Others"
        if not destination_folder:
            destination_folder = 'Others'

        # Create the destination folder if it does not exist
        destination_path = os.path.join(directory, destination_folder)
        os.makedirs(destination_path, exist_ok=True)

        # Move the file to the destination folder
        shutil.move(file_path, os.path.join(destination_path, file_name))

    print(f"Directory '{directory}' has been cleaned and organized.")

# Example usage
directory_to_clean = "C:\\Users\\Abdullah\\Downloads"
clean_directory(directory_to_clean)
