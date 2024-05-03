Single File Scaffolding
```bash

gcc -E /Users/mac/sheldonhh-fork/llm.c/train_gpt2.c -o /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i
sed -i '' '/^# [0-9]/d' /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i

cd  /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/
python3 cflow_single_two_args.py /Users/mac/sheldonhh-fork/llm.c/train_gpt2.i
python3 scaffolding-singlefile.py /Users/mac/sheldonhh-fork/llm.c/i-train_gpt2-callgraph.dot
```