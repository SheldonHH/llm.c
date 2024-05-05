import re
import os

def extract_headers_and_create_files_20240504(source_file_path, target_directory):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 打开并读取源文件
    with open(source_file_path, 'r') as file:
        content = file.read()
    
    # 使用正则表达式查找所有匹配的include语句
    pattern = r'#include\s+"([^"]+)"'
    includes = re.findall(pattern, content)
    
    # 为每个找到的头文件名创建一个对应的.rs文件
    for header in includes:
        rs_file_path = os.path.join(target_directory, f"{header}.rs")
        with open(rs_file_path, 'w') as file:
            file.write("// Generated for corresponding C header\n")

    return includes



source_file_path="../train_gpt2.c"
extract_headers_and_create_files_20240504()