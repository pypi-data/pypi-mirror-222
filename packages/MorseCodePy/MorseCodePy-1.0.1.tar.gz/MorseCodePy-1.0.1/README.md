
# MorseCodePy 1.0
## Introduction
MorseCodePy is a module that simplifies the process of translating normal text into **Morse code**. This versatile module supports various languages, including **English**, **Russian**, **Spanish**, **numbers**, **symbols** and **other**.
## Installation

Installing project using pip:

`pip install MorseCodePy` or `pip3 install MorseCodePy`
    
## How to use
`encode()` returns string with translated into Morse code. "string" is your string, that you want to translate. Also, you can customize `dit` and `dash`.

`codes` is a dictionary with letters, numbers & symbols and their Morse code translations. **Warning**: translations use 1's and 0's.

Examples:

```
import MorseCodePy as mc

string = "SOS"
t_string = mc.encode(string)

print(t_string)
# Output: ··· --- ···
```

```
import MorseCodePy as mc

string = "Bye!"
print(mc.encode(string, dit='0', dash='1'))
# Output: 1000 1011 0 101011
```

```
from MorseCodePy import codes

print(codes['a'])
# Output: 01
```
## Contact
**GitHub**: https://github.com/CrazyFlyKite

**Email**: karpenkoartem2846@gmail.com

**Discord**: CrazyFlyKite
