import os
from pathlib import Path

def format_keys_file(input_path: str, output_path: str, keys_per_line: int = 10):
    """
    Reads keys from an input file (one key per line) and writes them to an
    output file with a specified number of keys per line, separated by commas.
    """
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.is_file():
        print(f"Error: Input file not found at '{input_path}'")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            keys = [line.strip() for line in f if line.strip()]
        
        print(f"Read {len(keys)} keys from '{input_file.name}'.")

        # Create the output directory if it doesn't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            # Group keys into chunks of 'keys_per_line'
            for i in range(0, len(keys), keys_per_line):
                chunk = keys[i:i + keys_per_line]
                f.write(','.join(chunk) + '\n')
        
        print(f"Successfully formatted keys into '{output_file.name}' with {keys_per_line} keys per line.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the input file and create a corresponding output file name
    input_filename = "data/keys/keys_valid_20250817.txt"
    
    # Construct the full path relative to the project root
    project_root = Path(__file__).parent.parent
    input_filepath = project_root / input_filename
    
    # Create a formatted output filename
    output_filename = input_filepath.stem.replace("keys_valid", "formatted_keys") + input_filepath.suffix
    output_filepath = input_filepath.parent / output_filename

    format_keys_file(str(input_filepath), str(output_filepath))