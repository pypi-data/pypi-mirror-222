# Introduction

<div align="center">

<figure><img src=".gitbook/assets/Screenshot 2023-07-10 at 12.06.03 AM.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

## roblox-pyc

[**Docs**](https://robloxpyc.gitbook.io/roblox-pyc) **|** [**Devforum**](https://devforum.roblox.com/t/roblox-py-python-luau/2457105?u=dev98799) **|** [**Github**](https://github.com/AsynchronousAI/roblox.pyc) **|** [**Tests/Examples**](https://github.com/AsynchronousAI/roblox.py/tree/main/test)

***

```
pip install roblox-pyc
```



Python, Lunar, C, C++ Compiler for Roblox.

Python 3.13 (dev), C (all versions), C++ (all versions), Lunar -> Lua(u)

> This has NO RELATION with .pyc files, roblox-py, or roblox-ts

> C/C++ is still in progress.

> Python is fully implemented, all code should work because it supports the dev build of Python 3.13.

***

### Features

* 🔄 **Interchangeable**\
  roblox-pyc supports using Lua, Lunar, roblox-ts, C, C++, and Python all at once so you can have the best of all sides.
* ☄️ **Ultrafast compiler**\
  The roblox-pyc compiler is designed so entire projects can be compiled in a matter of seconds
* 📉 **Optimized code**\
  roblox-pyc is a source-source compiler, it doesn't use any WASM or anything like that to cheat its way and has major performance drops. It uses an AST and rewrites your code and optimizes it.
* ⚠️ **Easy error checking**\
  Your code can easily be checked for errors because of the precompiler error system.
* 🧩 **Cross-language module support**\
  roblox-pyc allows you to require/import modules from other languages.
* 🛠️ **Supports everything**\
  Regardless if you use Rojo, Argon, in Mac, Windows with any code editors or anything else roblox-pyc is highly customizable and allows you to use any of them
* ↗️ **Customizable**\
  You can customize roblox-pyc to change your C/C++ version or dynamic library or any QoL features, not only that roblox-pyc and all of its dependencies are open-source so you can mod it and change anything to your liking
* 💻 **Languages**\
  roblox-pyc supports a great variety of languages that are fully programmed.
* 🌎 **Upload your code to the world**\
  Using a VScode sync plugin you can upload your code to the world with GitHub, GitLab, whatever.
* 📲 **In-roblox plugin**\
  If you dont what to use VScode, python supports a roblox plugin which can be hosted in the terminal with all the features listed above!
* 🌙 **Lunar**\
  roblox-pyc comes with a custom language called lunar with amazing syntax features and an extended standard library, which is a modified version of MoonScript for roblox

***
## Unsupported features
- Import * (python)
- Syntax based slicing (python) (workaround: use slice builtin function)
- C/C++ (not implemented yet)
- _\_slots_\_ (python) (adding soon)
- _\_dict_\_ (python) (adding soon)
***

### Credits

* [Highlighter](https://github.com/boatbomber/Highlighter). modified to work with python (plugin usage)
* [TextBoxPlus](https://github.com/boatbomber/TextBoxPlus). uses a modified version with autocomplete (plugin usage)
* [pythonlua](https://github.com/dmitrii-eremin/python-lua). this is heavily modified version with flask implementation and compiler changes. (read licenses in [copyright.txt](COPYRIGHTS.txt))
* [seasnake](https://github.com/pybee/seasnake) and sealang. Modified to convert C/C++ to Luau rather than C/C++ to Python 2.7
* [MoonScript](https://github.com/leafo/moonscript). Modified to work with the Roblox API (Lunar).
* [LuauAST](). roblox-pyc uses roblox-ts's LuauAST to generate Luau code. (not used in current versions)
