```bash

cd /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example
gcc -E example.c -o example.i
cd ..
python3 cflow_generation.py c /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example
python3 cflow_generation.py i /Users/mac/sheldonhh-fork/llm.c/RustMap-Tools/example

```