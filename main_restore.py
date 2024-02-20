import sys
from main import main

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main_restore.py <file_name1> <file_name2> ...")
    else:
        restore_files = sys.argv[1:]
        main(None, None, restore_files)
