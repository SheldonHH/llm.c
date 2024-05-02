```bash
brew install cflow

python3 -m venv ~/my_venv
source ~/my_venv/bin/activate

pip3 install graphviz; pip3 install imageio; pip3 install cairosvg; pip3 install bidict
```



```bash
cd RustMap-Tools
python3 cflow_generation.py ..

```



# install tree-sitter-cli
```bash
cd RustMap-Tools
git clone https://github.com/tree-sitter/tree-sitter-c.git
cd tree-sitter-c
```


```bash
gcc -shared -o tree-sitter-c.so -fPIC src/parser.c
```