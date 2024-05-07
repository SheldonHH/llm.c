import os
import re
import sys

def find_defines(file_path):
    defines = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'^#define\s+(\w+)\s+(\d+)$', line.strip())
            if match:
                defines.append((match.group(1), match.group(2)))
    return defines

def get_type_suffix(value):
    if len(value) <= 9:
        return "i32"
    elif len(value) <= 18:
        return "i64"
    else:
        return "f64"

def convert_to_rust(defines, file_name):
    rust_code = ""
    for name, value in defines:
        type_suffix = get_type_suffix(value)
        rust_code += f"pub const {name}: {type_suffix} = {value};\n"
    return rust_code

def process_files(directory):
    result = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(('.c', '.h')):
                file_path = os.path.join(root, file_name)
                defines = find_defines(file_path)
                if defines:
                    result[file_name] = defines
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    result_dict = process_files(directory_path)
    
    for file_name, defines in result_dict.items():
        rust_code = convert_to_rust(defines, file_name)
        print(f"// Converted defines from {file_name}")
        print("#[macro_use]")
        print("macro_rules! my_macros {")
        print(rust_code)
        print("}")
