```bash

cd /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example
gcc -E example.c -o example.i

# mac
sed -i '' '/^# [0-9]/d' *.i
cd ..
python3 cflow_two_args.py c /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example
python3 cflow_two_args.py i /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example

```


```bash
cd /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/
dot -Tsvg c-callgraph.dot -o c-callgraph.svg


dot -Tsvg i-callgraph.dot -o i-callgraph.svg
```


remove absolute path from "c-callgraph.svg" and use dot to regenerate svg
