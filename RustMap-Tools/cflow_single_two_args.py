import os
import subprocess
import sys
import graphviz

def generate_cflow_dot(file_path):
    # 生成 dot 文件的命令
    command = f'cflow --format=dot {file_path}'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    dot_content = process.communicate()[0].decode()

    all_dot_content = "digraph G {\n"
    all_dot_content += 'rankdir="LR";\n'  # 使其从左到右布局

    # 去除生成内容的头部和尾部，因为我们只需要中间部分
    dot_lines = dot_content.split('\n')[2:-2]
    for line in dot_lines:
        all_dot_content += line + "\n"
    all_dot_content += "}"

    return all_dot_content

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("请提供文件路径作为命令行参数.")
        sys.exit(1)

    file_path = sys.argv[1]
    file_extension = os.path.splitext(file_path)[1]

    if file_extension not in ['.c', '.i']:
        print("不支持的文件类型.")
        sys.exit(1)

    dot_content = generate_cflow_dot(file_path)

    # 使用graphviz库渲染生成SVG文件
    dot_graph = graphviz.Source(dot_content)

    # 修改输出文件名，仅包含文件名而不是完整路径
    output_prefix = os.path.splitext(os.path.basename(file_path))[0] + "-callgraph"
    callgraph_svg_file = f"{output_prefix}.svg"
    callgraph_dot_file = f"i-{output_prefix}.dot"

    # 输出文件路径设置为文件原路径
    output_folder = os.path.dirname(file_path)
    callgraph_svg_path = os.path.join(output_folder, callgraph_svg_file)
    callgraph_dot_path = os.path.join(output_folder, callgraph_dot_file)

    dot_graph.render(filename=callgraph_svg_path, format="svg", view=False)
    dot_graph.render(filename=callgraph_dot_path, format="dot", view=False)

    print(f"已生成 {callgraph_svg_path} 和 {callgraph_dot_path}")
