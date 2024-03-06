import sys
import shutil
import os
import logger_config
import logging
from datetime import datetime

# Configure logging
logger_config.configure_logging()

class BackupManager (object):

    default_excel_folder = 'default_excel'

    def __init__(self) -> None:
        pass

    def backup_txt(self, input_file):
        """
        Function to backup a text file.

        Args:
        - input_file: Path to the input text file.
        """
        try:
            # Create the default_excel folder if it doesn't exist
            
            if not os.path.exists(BackupManager.default_excel_folder):
                os.makedirs(BackupManager.default_excel_folder)

            # Get the filename from the input file path
            file_name = os.path.basename(input_file)
            
            # Construct the destination file path in the default_excel folder
            destination_file = os.path.join(BackupManager.default_excel_folder, file_name)

            # If the destination file doesn't exist, copy the input file to the default_excel folder
            if not os.path.exists(destination_file):
                shutil.copy(input_file, destination_file)
                logging.info(f"File '{file_name}' copied to 'default_excel' folder.")
            else:
                logging.warning(f"File '{file_name}' already exists in 'default_excel' folder.")
        except Exception as e:
            logging.error(f"Error occurred during backup operation for file '{input_file}': {e}")

    def restore_default(self, *file_names):
        """
        Function to restore default files from 'default_excel' folder to the main folder.

        Args:
        - *file_names: Variable number of file names to restore. If no file names provided, all default files will be restored.
        """
        try:
            # List all files in the 'default_excel' folder
            default_files = os.listdir(BackupManager.default_excel_folder)

            # If no specific file names provided, restore all default files
            if not file_names:
                file_names = default_files

            # Restore each specified file from 'default_excel' folder to main folder
            for file_name in file_names:
                # Construct source and destination file paths
                source_file = os.path.join(BackupManager.default_excel_folder, file_name)
                destination_file = file_name

                # Check if source file exists and destination file doesn't exist
                if os.path.exists(source_file):
                    shutil.copy(source_file, destination_file)
                    logging.info(f"File '{file_name}' restored to main folder.")
                else:
                    logging.warning(f"File '{file_name}' could not be found in 'default_excel' folder.")
        except Exception as e:
            logging.error(f"Error occurred during restore operation: {e}")

    def backup_folder(self, src_folder, backup_folder):
        """
        Function to backup the contents of a folder to a destination folder.

        Args:
        - src_folder: Path to the source folder.
        - dest_folder: Path to the destination folder.
        """
        try:
            # Get the current date in YYYYMMDD format
            current_date = datetime.now().strftime('%Y%m%d')

            src_abs_path = os.path.abspath(src_folder)

            backup_abs_path = os.path.abspath(backup_folder)

            suffix = ""
            while True:
                dest_folder_with_suffix = f"{backup_folder}_{current_date}{suffix}"
                # save backup destination path        
                dest_folder_path = os.path.join(backup_abs_path, dest_folder_with_suffix)

                if not os.path.exists(dest_folder_path):
                    os.makedirs(dest_folder_path)
                    break
                # Increment the suffix if the folder already exists
                suffix = f"_{int(suffix.split('_')[-1]) + 1 if suffix else 1}"
            
            # Copy all contents of the source folder to the new destination folder
            for item in os.listdir(src_abs_path):
                item_path = os.path.join(src_abs_path, item)
                if os.path.isdir(item_path):
                    shutil.copytree(item_path, os.path.join(dest_folder_path, item))
                else:
                    shutil.copy(item_path, dest_folder_path)
            
            logging.info(f"Folder '{src_folder}' backed up to '{dest_folder_with_suffix}'.")
        except Exception as e:
            logging.error(f"Error occurred during folder backup operation: {e}")
