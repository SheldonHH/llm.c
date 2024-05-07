import sys
import os
import re


def extract_defines(file_path):
    defines = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#define'):
                parts = line.split()
                if len(parts) >= 3:
                    defines.append((parts[1], parts[2]))
    return defines

def write_rust_module(defines, output_path):
    with open(output_path, 'w') as file:
        file.write("// Converted defines from C header\n")
        file.write("#[macro_use]\n")
        file.write("macro_rules! my_macros {\n")
        for name, value in defines:
            file.write(f"pub const {name}: i32 = {value};\n")
        file.write("}\n")
