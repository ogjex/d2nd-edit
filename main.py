import shutil
import os
import sys

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

def multiply_columns(input_file, x):
    """
    Function to multiply specified columns by x.

    Args:
    - input_file: Path to the input text file.
    - x: Value to multiply the columns by.
    """
    # Read the contents of the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Modify the specified columns
    modified_lines = []
    for line in lines:
        columns = line.split('\t')
        # Check if the line has enough columns
        if len(columns) >= 3:
            # Multiply the specified columns by x
            for i in range(3):
                columns[i] = str(float(columns[i]) * x)
        modified_lines.append('\t'.join(columns))

    # Write the modified lines back to the file
    with open(input_file, 'w') as f:
        f.writelines(modified_lines)

def main():
    # Check if an input file and multiplication factor are provided
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <multiplication_factor>")
        sys.exit(1)

    # Input text file path
    input_file = sys.argv[1]

    # Multiplication factor
    x = float(sys.argv[2])

    # Backup folder path
    backup_folder = 'backup'

    # Call the backup function
    backup_txt(input_file, backup_folder)

    # Multiply the specified columns by x
    multiply_columns(input_file, x)

if __name__ == "__main__":
    main()