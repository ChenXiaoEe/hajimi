import os
from pathlib import Path

def deduplicate_keys_in_file(file_path: Path):
    """
    Reads a file, removes duplicate lines, and overwrites the file
    with the unique, sorted lines.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            keys = {line.strip() for line in f if line.strip()}
        
        unique_keys = sorted(list(keys))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            for key in unique_keys:
                f.write(key + '\n')
        
        print(f"Processed {file_path.name}: Found {len(unique_keys)} unique keys.")
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

def process_directory(directory: str):
    """
    Finds all 'keys_valid_*.txt' files in a directory and processes them.
    """
    key_dir = Path(directory)
    if not key_dir.is_dir():
        print(f"Error: Directory '{directory}' not found.")
        return

    key_files = list(key_dir.glob("keys_valid_*.txt"))
    if not key_files:
        print(f"No 'keys_valid_*.txt' files found in '{directory}'.")
        return

    print(f"Found {len(key_files)} files to process...")
    for file_path in key_files:
        deduplicate_keys_in_file(file_path)

if __name__ == "__main__":
    # The script is in utils/, so the target directory is ../data/keys
    target_directory = Path(__file__).parent.parent / "data" / "keys"
    process_directory(str(target_directory))
    print("\nDeduplication process completed for all files.")