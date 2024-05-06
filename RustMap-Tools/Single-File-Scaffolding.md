

# install tree-sitter-cli
```bash
cd RustMap-Tools
rm -rf tree-sitter-c
git clone https://github.com/tree-sitter/tree-sitter-c.git
cd tree-sitter-c
tree-sitter generate
gcc -shared -o tree-sitter-c.so -fPIC src/parser.c 
mv tree-sitter-c.so ..
cd ..
rm -rf tree-sitter-c
mkdir tree-sitter-c && mv tree-sitter-c.so tree-sitter-c
```




# Single File Scaffolding
```bash

git clone https//github.com/sheldonhh/llm.c.git
cd llm.c
current_path=$(pwd)
# 构建-v参数的值，这里假设你想映射的文件是在当前目录下的llm.c
volume_path="${current_path}:/root/llm.c"
docker run -itd -v "$volume_path" rust

# 使用 docker ps 命令配合 grep 来快速查找这个容器
CONTAINER_ID=$(docker ps -a --filter "ancestor=rust" --latest --format "{{.ID}}")
# 输出的容器ID存储在变量 CONTAINER_ID 中，你可以使用以下命令进入该容器：
docker exec -it $CONTAINER_ID /bin/bash

# docker run -itd -v "/Users/mac/sheldonhh-fork/llm.c:/root/llm.c" rust


# for ubuntu
apt update -y
apt install cflow sudo pip python3.11-venv -y

python3 -m venv ~/my_project_env
source ~/my_project_env/bin/activate
pip3 install graphviz imageio cairosvg tree_sitter bidict


# pip3 install graphviz imageio





cd /root/llm.c/
gcc -E /root/llm.c/train_gpt2.c -o /root/llm.c/train_gpt2.i
#!/bin/bash
FILE_PATH="/root/llm.c/train_gpt2.i"
OS=$(uname -s)
[[ "$OS" == "Darwin" ]] && sed -i '' '/^# [0-9]/d' "$FILE_PATH" || sed -i '/^# [0-9]/d' "$FILE_PATH"



cd /root/llm.c/RustMap-Tools
# 生成callgraph
python3 cflow_single_two_args.py /root/llm.c/train_gpt2.i



# delete existing scaffolding
rm -rf /root/llm.c/RustMap-Tools/train_gpt2_rs_gpt
# 根据callgraph生成给予.i的脚手架
python3 scaffolding-singlefile.py /root/llm.c/i-train_gpt2-callgraph.dot

# 查看生成的内容
# 根据原本.c的所依赖的header,生成.h.rs脚手架
python3 create_headers.py

```