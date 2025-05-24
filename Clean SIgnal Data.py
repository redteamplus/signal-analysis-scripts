from pathlib import Path
import re

# Define the paths to the rolling code files
file_paths = [
    "rolling1.txt",
    "rolling2.txt"
]

# Clean the files by removing "[Pause: ... samples]" and joining all hex parts
for path in file_paths:
    file = Path(path)
    with file.open('r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract only the hex data (ignore pause descriptions)
    cleaned_data = [re.match(r'^([a-fA-F0-9]+)', line) for line in lines]
    cleaned_data = [match.group(1) for match in cleaned_data if match]

    # Join all hex chunks together to one line
    combined = ''.join(cleaned_data)

    # Write it back to the same file (overwrite)
    with file.open('w', encoding='utf-8') as f:
        f.write(combined)
