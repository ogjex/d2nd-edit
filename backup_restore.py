import shutil
import os
import logger_config
import logging

# Configure logging
logger_config.configure_logging()

def backup_txt(input_file):
    """
    Function to backup a text file.

    Args:
    - input_file: Path to the input text file.
    """
    try:
        # Create the default_excel folder if it doesn't exist
        default_excel_folder = 'default_excel'
        if not os.path.exists(default_excel_folder):
            os.makedirs(default_excel_folder)

        # Get the filename from the input file path
        file_name = os.path.basename(input_file)
        
        # Construct the destination file path in the default_excel folder
        destination_file = os.path.join(default_excel_folder, file_name)

        # If the destination file doesn't exist, copy the input file to the default_excel folder
        if not os.path.exists(destination_file):
            shutil.copy(input_file, destination_file)
            logging.info(f"File '{file_name}' copied to 'default_excel' folder.")
        else:
            logging.warning(f"File '{file_name}' already exists in 'default_excel' folder.")
    except Exception as e:
        logging.error(f"Error occurred during backup operation for file '{input_file}': {e}")

def restore_default(*file_names):
    """
    Function to restore default files from 'default_excel' folder to the main folder.

    Args:
    - *file_names: Variable number of file names to restore. If no file names provided, all default files will be restored.
    """
    try:
        # List all files in the 'default_excel' folder
        default_excel_folder = 'default_excel'
        default_files = os.listdir(default_excel_folder)

        # If no specific file names provided, restore all default files
        if not file_names:
            file_names = default_files

        # Restore each specified file from 'default_excel' folder to main folder
        for file_name in file_names:
            # Construct source and destination file paths
            source_file = os.path.join(default_excel_folder, file_name)
            destination_file = file_name

            # Check if source file exists and destination file doesn't exist
            if os.path.exists(source_file):
                shutil.copy(source_file, destination_file)
                logging.info(f"File '{file_name}' restored to main folder.")
            else:
                logging.warning(f"File '{file_name}' could not be found in 'default_excel' folder.")
    except Exception as e:
        logging.error(f"Error occurred during restore operation: {e}")

# Example usage
if __name__ == "__main__":
    # Example backup
    backup_txt('example.txt')

    # Example restore
    restore_default('file1.txt', 'file2.txt')
