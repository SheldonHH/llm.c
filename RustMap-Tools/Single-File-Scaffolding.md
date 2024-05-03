Single File Scaffolding
```bash

gcc -E /Users/mac/sheldonhh-fork/llm.c/train_gpt2.c -o /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i
sed -i '' '/^# [0-9]/d' /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i

cd  /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/

# 生成callgraph
python3 cflow_single_two_args.py /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i

# 根据callgraph生成给予.i的脚手架
python3 scaffolding-singlefile.py /Users/mac/sheldonhh-fork/llm.c/i-train_gpt2-callgraph.dot

# 根据原本.c的所依赖的header,生成.h.rs脚手架


```