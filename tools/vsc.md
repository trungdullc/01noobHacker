# Visual Studio Code

```
Source: https://code.visualstudio.com/Docs
Description: Code Editor
```

<table>
    <tr>
      <th>Action</th>
      <th>Windows/Linux</th>
      <th>Mac</th>
    </tr>
    <tr>
      <td>Select All</td>
      <td><kbd>Ctrl</kbd> + <kbd>A</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>A</kbd></td>
    </tr>
    <tr>
      <td>Indent (Tab)</td>
      <td><kbd>Tab ❤️</kbd></td>
      <td><kbd>Tab</kbd></td>
    </tr>
    <tr>
      <td>Unindent (Shift + Tab)</td>
      <td><kbd>Shift</kbd> + <kbd>Tab</kbd> ❤️</td>
      <td><kbd>Shift</kbd> + <kbd>Tab</kbd></td>
    </tr>
    <tr>
      <td>Duplicate Line / Selection</td>
      <td><kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>↓</kbd></td>
      <td><kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>↓</kbd></td>
    </tr>
    <tr>
      <td>Move Line Up/Down</td>
      <td><kbd>Alt</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd></td>
      <td><kbd>Option</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd></td>
    </tr>
    <tr>
      <td>Comment/Uncomment Line ❤️</td>
      <td><kbd>Ctrl</kbd> + <kbd>/</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>/</kbd></td>
    </tr>
    <tr>
      <td>Multi-Cursor (Add Cursor)</td>
      <td><kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd></td>
      <td><kbd>Option</kbd> + <kbd>Cmd</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd></td>
    </tr>
    <tr>
      <td>Search in File</td>
      <td><kbd>Ctrl</kbd> + <kbd>F</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>F</kbd></td>
    </tr>
    <tr>
      <td>Search Across Files</td>
      <td><kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd></td>
    </tr>
    <tr>
      <td>Open File</td>
      <td><kbd>Ctrl</kbd> + <kbd>P</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>P</kbd></td>
    </tr>
    <tr>
      <td>Go to Definition</td>
      <td><kbd>F12</kbd></td>
      <td><kbd>F12</kbd></td>
    </tr>
    <tr>
      <td>Rename Symbol ❤️</td>
      <td><kbd>F2</kbd></td>
      <td><kbd>F2</kbd></td>
    </tr>
    <tr>
      <td>Format Document</td>
      <td><kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd></td>
      <td><kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>F</kbd></td>
    </tr>
    <tr>
      <td>Integrated Terminal</td>
      <td><kbd>Ctrl</kbd> + <kbd>`</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>`</kbd></td>
    </tr>
    <tr>
      <td>Command Palette</td>
      <td><kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd></td>
      <td><kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd></td>
    </tr>
  </table>

## CTF
[picoGym0012: Notepad++ and VSC](../picoCTF/picoGym0012.md)

## Useful
```
multiple selection            alt + mouse click
easy scroll and view errors   Right Click Right Scroll Bar > Minimap
```

## Extensions
```
Code Spell Checker            ❤️❤️❤️❤️❤️
Quokka                        run and debug .js and .ts
Code Runner                   run code in vsc
Live Server                   local development server
remote ssh
GitHub Copilot                AI Help and unit test (Paid Subscription)
Live Share                    Team works on same code
Prettier
Docker
JavaScript (ES6) code snippets
ES7 React/Redux/GraphQL

# AI
Python Extension Pack
Path Intellisense
GitHub Pull Request           click ... ❤️❤️❤️❤️❤️
Ruff                          Auto Formatter (PEP8 Python Style)
```

## AI
```
File > Save Workspace as      Double click shortcut new-project.code-workspace

# Create Virtual Environment 
python -m venv .venv
# Activate the Virtual Environment
Windows: .\.venv\Scripts\activate       macOS/Linux: source .venv/bin/activate
# Select Python Interpreter and choose the interpreter from .venv folder
Ctrl + Shift + P: Command Pallete   Python: Select Interpreter
# Install Required Packages
pip3 install django                     pip3 install flask
which pip
pip3 install pandas
# Deactivate the Virtual Environment
deactivate

# Format
Settings > Format on Save
Settings > Default Formatter > Ruff
```

## Run Jupyter Notebook (Rarely Use)
```
Double click notebook folder
Create notebook.ipynb (Note: Same like Google Colab Notebook)

Shortcuts:
   dd               delete cell
   b                insert cell
```

## Run Jupyter Interactive Window
```
Settings > Jupyter Interactive Window
Enable: When pressing shift+enter, send selected code in a Python file to the Jupyter interactive window as opposed to the Python terminal

... > Variables     See variables still in memory
```

## Back to README.md
[BACK](../README.md)