import sys
from main import main

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main_column_edit.py <input_file> <multiplication_factor>")
    else:
        input_file = sys.argv[1]
        multiplication_factor = float(sys.argv[2])
        main(input_file, multiplication_factor)
