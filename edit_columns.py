import logging
import logger_config  # Import the logging configuration module

# Configure logging
logger_config.configure_logging()

def multiply_columns(input_file, x):
    """
    Function to multiply specified columns by x.

    Args:
    - input_file: Path to the input text file.
    - x: Value to multiply the columns by.
    """
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Modify the specified columns ('MonDen', 'MonDen(N)', and 'MonDen(H)')
        modified_lines = []
        for idx, line in enumerate(lines):
            # Skip the header row
            if idx == 0:
                modified_lines.append(line)
                continue

            columns = line.split('\t')
            # Check if the line has enough columns
            if len(columns) >= 65:  # Assuming 'MonDen', 'MonDen(N)', and 'MonDen(H)' are columns 63, 64, and 65
                # Multiply the specified columns by x and convert to integer
                for col_idx in [63, 64, 65]:
                    try:
                        columns[col_idx] = str(int(float(columns[col_idx]) * x))
                    except ValueError:
                        # Log a warning if the column value cannot be converted to float
                        logging.warning(f"Unable to convert column value to float at line {idx + 1}, column index {col_idx}. Skipping multiplication.")
            modified_lines.append('\t'.join(columns))

        # Write the modified lines back to the file
        with open(input_file, 'w') as f:
            f.writelines(modified_lines)
        
        logging.info(f"Columns 'MonDen', 'MonDen(N)', and 'MonDen(H)' multiplied by {x} in file '{input_file}'.")
    except Exception as e:
        logging.error(f"Error occurred during column multiplication operation for file '{input_file}': {e}")

# Example usage
if __name__ == "__main__":
    # Example multiplication with x = 2
    multiply_columns('example.txt', 2)
