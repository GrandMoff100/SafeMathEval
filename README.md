# Safe Eval
This is a safe evaluation method for mathematical expressions. You can use in shell/terminal/bash (You can also use the Native Python Parser)

# Usage

```bash
evalsafe <expression> <expressions> ...
```

# Compiling from latest source

- **Clone the repo**
```bash
git clone https://github.com/GrandMoff100/SafeMathEval
```

- **Switch your Current Working Directory**
```bash
cd SafeMathEval
```

- **Run your OS-Specific compiling script**
> compile.bat for Windows, compile.sh for MacOS, and Linux
```bash
# Windows
bat compile.bat

# Linux & MacOS
sh compile.sh
```

- **Test**

```bash
evalsafe "1+2-3+(5/2**3)"
```

# Native Python Parser

Import ``Parser`` from parser.py

```py
from parser import Parser

myparser = Parser()

expressions = [
    # Multiple Expressions Here
    "1+2+4",
    "1+(3/4-1)**4"
]

for expr in expressions:
    print(myparser.eval(expr))
```
