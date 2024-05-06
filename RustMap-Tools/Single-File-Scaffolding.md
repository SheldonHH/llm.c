Single File Scaffolding
```bash

git clone https//github.com/sheldonhh/llm.c.git

# for ubuntu
apt update -y
apt install cflow sudo python3-pip -y

sudo apt install python3-graphviz python3-imageio -y
# pip3 install graphviz imageio




gcc -E /root/llm.c/train_gpt2.c -o /root/llm.c/train_gpt2.i
sed -i '' '/^# [0-9]/d' /root/llm.c/train_gpt2.i


cd RustMap-Tools
# 生成callgraph
python3 cflow_single_two_args.py /root/llm.c/train_gpt2.i

# 根据callgraph生成给予.i的脚手架
python3 scaffolding-singlefile.py /root/llm.c/i-train_gpt2-callgraph.dot

# 查看生成的内容

# 根据原本.c的所依赖的header,生成.h.rs脚手架
python3 create_headers.py

```