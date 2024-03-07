import sys
import shutil
import os
import logger_config
import logging
from datetime import datetime

# Configure logging
logger_config.configure_logging()

class BackupManager (object):
    backup_game_file_folder = 'excel_backup_folder'
    modded_game_file_folder = 'modded_excel_files'

    def __init__(self) -> None:
        pass

    def backup_game_files(self, default_game_file_path):
        """
        Function to backup a text file. The logic is that we need a local copy from the current mod's excel folder 
        because we need to overwrite the mod folder's files with our own modded files. 

        Args:
        - input_file: Path to the input text file.
        """
        try:
            # Create the backup game file folder if it doesn't exist
            if not os.path.exists(self.backup_game_file_folder):
                os.makedirs(self.backup_game_file_folder)

            # Get the filename from the input file path
            default_file_name = os.path.basename(default_game_file_path)
            # Construct the destination file path in the default game file folder
            destination_file_path = os.path.join(self.backup_game_file_folder, default_file_name)

            # If the destination file doesn't exist, copy the input file to the default game file folder
            if not os.path.exists(destination_file_path):
                shutil.copy(default_game_file_path, destination_file_path)
                logging.info(f"File '{default_file_name}' copied to '{self.backup_game_file_folder}' folder.")
            else:
                logging.warning(f"File '{default_file_name}' already exists in '{self.backup_game_file_folder}' folder.")
        except Exception as e:
            logging.error(f"Error occurred during backup operation for file '{default_game_file_path}': {e}")

    def restore_files(self, destination_folder, file_names):
        for file_name in file_names:
            # copy all files from backup to the game file folder first
            shutil.copy(os.path.join(self.backup_game_file_folder, file_name), destination_folder)
            # then we remove the modded files to ensure that all values are restored.
            os.remove(os.path.join(self.modded_game_file_folder, file_name), destination_folder)
            if not os.path.exists(os.path.join(self.modded_game_file_folder, file_name)):
                logging.info(f"Default values of file '{file_name}' restored to main folder.")    
            else:
                logging.warning(f"File '{file_name}' could not be found in default game file folder.")
        
    def restore_default(self, default_game_file_folder, *file_names):
        """
        Function to restore default files from 'default modded folder' folder to the main folder.

        Args:
        - *file_names: Variable number of file names to restore. If no file names provided, all default files will be restored.
        """
        try:
            # If modded game folder does not exist, create it.
            if not os.path.exists(self.modded_game_file_folder):
                os.makedirs(self.modded_game_file_folder)
                logging.info(f"No modded game file folder detected. Folder '{self.modded_game_file_folder}' created in '{os.path.abspath(self.modded_game_file_folder)}'.")    

            # If no specific file names provided, restore all default files by overwriting the files in game file folder based on all the filenames in the backup folder
            if not file_names:
                modded_files = os.listdir(self.modded_game_file_folder)
                self.restore_files(default_game_file_folder, modded_files)
            
            if file_names:
                self.restore_files(default_game_file_folder, file_names)
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
