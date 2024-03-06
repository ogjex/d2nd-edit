import os
import shutil
import logging
import logger_config  # Import the logging configuration module

# Configure logging
logger_config.configure_logging()

class FileEditor:
    def __init__(self) -> None:
        pass

    def multiply_columns(default_game_file_folder, input_file, x, column_indices, destination_folder=None):
        """
        Function to multiply specified columns by x.

        Args:
        - input_file: Path to the input text file.
        - x: Value to multiply the columns by.
        - column_indices: List of column indices to modify.
        - destination_folder: Optional. Path to the destination folder to save the modified file.
        If not provided, the file will be saved to "modded_files" in the same folder as the program.
        """
        try:
            # Construct the path to the default file in "default_excel" folder
            default_file = os.path.join(default_game_file_folder, os.path.basename(input_file))

            # Read the contents of the default file
            with open(default_file, 'r') as f:
                default_lines = f.readlines()

            # Modify the specified columns
            modified_lines = []
            for idx, line in enumerate(default_lines):
                # Skip the header row
                if idx == 0:
                    modified_lines.append(line)
                    continue

                columns = line.split('\t')
                # Check if the line has enough columns
                if len(columns) >= max(column_indices) + 1:
                    # Multiply the specified columns by x and convert to integer
                    for col_idx in column_indices:
                        try:
                            columns[col_idx] = str(int(float(columns[col_idx]) * x))
                        except ValueError:
                            # Log a warning if the column value cannot be converted to float
                            logging.warning(f"Unable to convert column value to float at line {idx + 1}, column index {col_idx}. Skipping multiplication.")
                modified_lines.append('\t'.join(columns))

            # Determine the destination folder
            if destination_folder is None:
                destination_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modded_files")
            os.makedirs(destination_folder, exist_ok=True)

            # Construct the path to the destination file
            destination_file = os.path.join(destination_folder, os.path.basename(default_file))

            # Write the modified lines to the destination file
            with open(destination_file, 'w') as f:
                f.writelines(modified_lines)

            logging.info(f"Columns at indices {column_indices} multiplied by {x} in file '{input_file}'.")
            logging.info(f"Modified file saved to '{destination_file}'.")
        except Exception as e:
            logging.error(f"Error occurred during column multiplication operation for file '{input_file}': {e}")