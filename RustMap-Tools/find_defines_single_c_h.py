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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not file_path.endswith(('.c', '.h')):
        print("The file must be a .c or .h file.")
        sys.exit(1)

    defines = find_defines(file_path)
    if defines:
        rust_code = convert_to_rust(defines, os.path.basename(file_path))
        print(f"// Converted defines from {os.path.basename(file_path)}")
        print("#[macro_use]")
        print("macro_rules! my_macros {")
        print(rust_code)
        print("}")

