# Help Section

```
Description: Help w/ Python, C++, JS, Bash, PowerShell

Python:
  help(list)              # full docs for list
  dir([])                 # list methods
  [].__doc__              # one-line docstring
  globals().keys()        # global variables / functions
  vars(object())          # instance attributes

JavaScript(Browser):
  console.log(Object.getOwnPropertyNames(Math))  // all Math methods
  console.log(Object.keys(obj))                  // instance enumerable props
  console.log(globalThis)                        // global names / functions

Linux/Bash:
  man ls           # documentation
  whatis ls        # one-line description
  apropos copy     # search by keyword
  alias            # list aliases
  declare -F       # list functions
  compgen -v       # list variables

PowerShell:
  Get-Help Get-Process
  Get-Member $obj
  Get-Alias
```

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Purpose</th>
      <th>Python</th>
      <th>JavaScript (Node / Browser)</th>
      <th>C++</th>
      <th>Bash / Linux</th>
      <th>PowerShell</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Get documentation / help</td>
      <td><code>help(obj)</code></td>
      <td>console.log(obj) with MDN / inspect</td>
      <td>Check header files / cppreference.com</td>
      <td><code>man &lt;cmd&gt;</code></td>
      <td><code>Get-Help &lt;cmd&gt;</code></td>
    </tr>
    <tr>
      <td>Quick one-line description</td>
      <td><code>obj.__doc__</code></td>
      <td>No direct equivalent</td>
      <td>—</td>
      <td><code>whatis &lt;cmd&gt;</code></td>
      <td><code>Get-Help &lt;cmd&gt; -Online</code></td>
    </tr>
    <tr>
      <td>List all attributes / methods of object</td>
      <td><code>dir(obj)</code></td>
      <td><code>Object.getOwnPropertyNames(obj)</code></td>
      <td>Header inspection / IDE class browser</td>
      <td><code>declare -F</code> (functions)</td>
      <td><code>Get-Member &lt;obj&gt;</code></td>
    </tr>
    <tr>
      <td>List instance properties (enumerable)</td>
      <td><code>vars(obj)</code></td>
      <td><code>Object.keys(obj)</code></td>
      <td>—</td>
      <td><code>compgen -v</code> (variables)</td>
      <td><code>Get-Member -MemberType Property</code></td>
    </tr>
    <tr>
      <td>List global names / aliases</td>
      <td><code>globals().keys()</code></td>
      <td><code>globalThis</code></td>
      <td>Preprocessor macros / constants</td>
      <td><code>alias</code></td>
      <td><code>Get-Alias</code></td>
    </tr>
    <tr>
      <td>Create alias / shortcut</td>
      <td><code>import module as alias</code></td>
      <td><code>const alias = require('module')</code></td>
      <td>using / typedef</td>
      <td><code>alias ll='ls -la'</code></td>
      <td><code>Set-Alias ll Get-ChildItem</code></td>
    </tr>
    <tr>
      <td>Search by keyword</td>
      <td><code>help("keyword")</code></td>
      <td>Search MDN / Google</td>
      <td>—</td>
      <td><code>apropos &lt;keyword&gt;</code></td>
      <td><code>Get-Help *keyword*</code></td>
    </tr>
    <tr>
      <td>List files / directories</td>
      <td><code>os.listdir()</code></td>
      <td><code>fs.readdirSync()</code> / <code>console.dir()</code></td>
      <td>Filesystem APIs / IDE browser</td>
      <td><code>ls</code></td>
      <td><code>Get-ChildItem</code></td>
    </tr>
    <tr>
      <td>Read file contents</td>
      <td><code>open("file").read()</code></td>
      <td><code>fs.readFileSync("file", "utf8")</code></td>
      <td>ifstream / file streams</td>
      <td><code>cat file</code></td>
      <td><code>Get-Content file</code></td>
    </tr>
    <tr>
      <td>Find files / search filesystem</td>
      <td><code>glob.glob("pattern")</code></td>
      <td><code>fs.readdirSync() + filter</code></td>
      <td>Filesystem APIs / Boost.Filesystem</td>
      <td><code>find . -name "pattern"</code></td>
      <td><code>Get-ChildItem -Recurse -Filter "pattern"</code></td>
    </tr>
    <tr>
      <td>Search text / pattern</td>
      <td><code>re.search(pattern, text)</code></td>
      <td><code>RegExp</code> + <code>string.match()</code></td>
      <td><code>std::regex_search</code></td>
      <td><code>grep "pattern" file</code></td>
      <td><code>Select-String -Pattern "pattern"</code></td>
    </tr>
    <tr>
      <td>Stream text editing</td>
      <td><code>re.sub(pattern, repl, text)</code></td>
      <td><code>string.replace()</code></td>
      <td>std::regex_replace</td>
      <td><code>sed 's/pattern/repl/' file</code></td>
      <td><code>(Get-Content file) -replace "pattern","repl"</code></td>
    </tr>
    <tr>
      <td>Text processing / columns</td>
      <td><code>csv.reader</code> / <code>split()</code></td>
      <td><code>split()</code> / libraries like <code>papaparse</code></td>
      <td>stringstream / <code>std::getline</code></td>
      <td><code>awk '{print $1,$2}' file</code></td>
      <td><code>ForEach-Object { $_.Split(" ")[0] }</code></td>
    </tr>
  </tbody>
</table>


## Back to README.md
[BACK](../README.md)