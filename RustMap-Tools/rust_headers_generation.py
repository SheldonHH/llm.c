import os
import re
import sys

def rust_headers_generation(source_file, target_directory):
    target_directory = os.path.join(target_directory, "headers")  # Create headers subdirectory within target directory

    # Ensure the headers directory exists
    os.makedirs(target_directory, exist_ok=True)

    # Check if the provided file is a .c file
    if not source_file.endswith('.c'):
        print("Error: The provided file is not a .c file.")
        sys.exit(1)

    # Read the contents of the file
    with open(source_file, 'r') as file:
        content = file.read()

    # Use regex to find all matching #include statements
    includes = re.findall(r'#include\s+"([^"]+)"', content)

    # Prepare content for mod.rs file
    mod_rs_content = []

    # Create .rs files only for files that have #include
    if includes:
        for header in includes:
            rs_filename = header.replace('.h', '.rs')
            rs_filepath = os.path.join(target_directory, rs_filename)
            
            # Add use statement for each .rs file to mod.rs
            mod_rs_content.append(f"use crate::headers::{rs_filename[:-3]};")  # Remove the .rs suffix from the filename
            
            # Create .rs file if it does not exist
            if not os.path.exists(rs_filepath):
                with open(rs_filepath, 'w') as new_file:
                    new_file.write('// Rust module corresponding to {}\n'.format(header))
                    print(f'Created {rs_filepath}')

    # Write the mod.rs file
    mod_rs_path = os.path.join(target_directory, "mod.rs")
    with open(mod_rs_path, 'w') as mod_rs_file:
        mod_rs_file.write('\n'.join(mod_rs_content))
        print(f"Created {mod_rs_path}")

    print("Completed!")
    return includes

if __name__ == "__main__":
    # Get .c file path and target directory path from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file.c> <target_directory>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    target_directory = sys.argv[2]
    process_c_file(source_file, target_directory)
