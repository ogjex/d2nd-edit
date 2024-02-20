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

    # Modify the specified columns ('MonDen', 'MonDen(N)', and 'MonDen(H)')
    modified_lines = []
    for idx, line in enumerate(lines):
        # Skip the header row
        if idx == 0:
            modified_lines.append(line)
            continue

        columns = line.split('\t')
        # Check if the line has enough columns
        if len(columns) >= 66:  # Assuming 'MonDen', 'MonDen(N)', and 'MonDen(H)' are columns 64, 65, and 66
            # Multiply the specified columns by x and convert to integer
            for col_idx in [64, 65, 66]:
                try:
                    columns[col_idx] = str(int(float(columns[col_idx]) * x))
                except ValueError:
                    # Skip if the column value cannot be converted to float
                    pass
        modified_lines.append('\t'.join(columns))

    # Write the modified lines back to the file
    with open(input_file, 'w') as f:
        f.writelines(modified_lines)