import shutil
import os

def backup_txt(input_file, backup_folder):
    """
    Function to backup a text file.

    Args:
    - input_file: Path to the input text file.
    - backup_folder: Path to the folder where the backup will be saved.
    """
    # Create the backup folder if it doesn't exist
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Get the filename from the input file path
    file_name = os.path.basename(input_file)
    
    # Construct the backup file path
    backup_file = os.path.join(backup_folder, f"{file_name}_backup.txt")

    # Copy the input file to the backup location
    shutil.copy(input_file, backup_file)

def main():
    # Input text file path
    input_file = 'levels.txt'

    # Backup folder path
    backup_folder = 'backup'

    # Call the backup function
    backup_txt(input_file, backup_folder)

    # Now you can read the text file, edit the desired column,
    # and save the changes.

if __name__ == "__main__":
    main()