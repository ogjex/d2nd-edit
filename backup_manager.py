import sys
import shutil
import os
import logger_config
import logging
from datetime import datetime

# Configure logging
logger_config.configure_logging()

class BackupManager (object):

    def __init__(self) -> None:
        pass

    def backup_game_files(self, default_game_file_folder, input_file):
        """
        Function to backup a text file.

        Args:
        - input_file: Path to the input text file.
        """
        try:
            # Create the default_excel folder if it doesn't exist
            
            if not os.path.exists(default_game_file_folder):
                os.makedirs(default_game_file_folder)

            # Get the filename from the input file path
            file_name = os.path.basename(input_file)
            
            # Construct the destination file path in the default_excel folder
            destination_file = os.path.join(default_game_file_folder, file_name)

            # If the destination file doesn't exist, copy the input file to the default_excel folder
            if not os.path.exists(destination_file):
                shutil.copy(input_file, destination_file)
                logging.info(f"File '{file_name}' copied to 'default_excel' folder.")
            else:
                logging.warning(f"File '{file_name}' already exists in 'default_excel' folder.")
        except Exception as e:
            logging.error(f"Error occurred during backup operation for file '{input_file}': {e}")

    def remove_files(self, folder, file_names):
        for file_name in file_names:
            os.remove(os.path.join(folder, file_name))
            if os.path.exists(os.path.join(folder, file_name)):
                logging.info(f"Default values of file '{file_name}' restored to main folder.")    
            else:
                logging.warning(f"File '{file_name}' could not be found in default game file folder.")
        
    def restore_default(self, modded_game_file_folder, *file_names):
        """
        Function to restore default files from 'default modded folder' folder to the main folder.

        Args:
        - *file_names: Variable number of file names to restore. If no file names provided, all default files will be restored.
        """
        try:
            # If no specific file names provided, restore all default files by removing them
            if file_names:
                modded_files = os.listdir(modded_game_file_folder)
                self.remove_files(modded_game_file_folder, file_names)
            else:
            # Restore each specified file from 'default game file' folder by removing each file 
                self.remove_files(modded_game_file_folder, modded_files) 
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
