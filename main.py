import sys
from backup_restore import backup_txt, restore_default
from edit_columns import multiply_columns

def main(input_file, multiplication_factor, restore_files=None):
    # Backup input file if provided
    if input_file:
        backup_txt(input_file)

    # Multiply specified columns in a text file
    if input_file and multiplication_factor:
        multiply_columns(input_file, multiplication_factor)

    # Restore specific files if requested
    if restore_files:
        restore_default(*restore_files)

if __name__ == "__main__":
    pass  # Placeholder for direct execution
