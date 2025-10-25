# JavaScript

```javascript
Description: Programming Languange

// clear console
clear()
Console was cleared

// Note: using var because can reassign easier than let and const
// Use JS only as last resort to solve things since logic and math sometimes bug w/ its loose design 👀

// default
var myVariable                          // declare variable w/o assigning value
console.log(myVariable)
VM4925:1 undefined                      // undefine has a value but not defined yet vs null

var var1 = 2, var2 = 4;                 // multiple declaration w/ ,
console.log(var1 + var2)
VM5089:1 6
console.log(var1, var2)
VM5111:1 2 4

// Create object
const obj = { foo: 42, bar: () => "hello" };
undefined

// List all properties (own properties) <-> Python dir
console.log(Object.getOwnPropertyNames(obj));
VM224:1 (2) ['foo', 'bar']

// Include inherited properties as well
console.log(Object.getPrototypeOf(obj));
VM252:1 {__defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, __lookupSetter__: ƒ, …}

/**
 * Note: JSDoc only seen in IDEs
 * Adds two numbers.
 * @param {number} a - first number
 * @param {number} b - second number
 * @returns {number} sum of a and b
 */
function add(a, b) {
   return a + b;
}
add.meta = {
   description: "Adds two numbers",
   params: [{name: "a", type: "number"}, {name: "b", type: "number"}],
   returns: "number"
};

// show function
add
ƒ add(a, b) {
   return a + b;
}

// show JS object
add.meta
{description: 'Adds two numbers', params: Array(2), returns: 'number'}
// Note: Look in [Prototype] for built-in functions

// show specific property
add.meta.description
'Adds two numbers'
```

<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>Concept / Action</th>
      <th>Browser JS</th>
      <th>Node.js / Terminal JS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Print / log output</td>
      <td><code>console.log("Hello")</code> → prints to browser console</td>
      <td><code>console.log("Hello")</code> → prints to terminal</td>
    </tr>
    <tr>
      <td>Debug / inspect</td>
      <td><code>console.dir(obj)</code>, DevTools inspect</td>
      <td><code>console.dir(obj, {depth: null})</code></td>
    </tr>
    <tr>
      <td>Clear console</td>
      <td><code>console.clear()</code></td>
      <td><code>console.clear()</code></td>
    </tr>
    <tr>
      <td>Prompt for input</td>
      <td><code>prompt("Enter value")</code> → returns string</td>
      <td><code>require('readline').createInterface(...)</code> or <code>process.stdin</code></td>
    </tr>
    <tr>
      <td>Alert / popup</td>
      <td><code>alert("Hello")</code> → popup in browser</td>
      <td>Not available</td>
    </tr>
    <tr>
      <td>Environment global object</td>
      <td><code>window</code></td>
      <td><code>global</code></td>
    </tr>
    <tr>
      <td>Timer / async</td>
      <td><code>setTimeout</code>, <code>setInterval</code></td>
      <td>Same: <code>setTimeout</code>, <code>setInterval</code></td>
    </tr>
    <tr>
      <td>Module system</td>
      <td><code>&lt;script&gt;</code> / ES Modules <code>import</code></td>
      <td>CommonJS <code>require</code>, ES Modules <code>import</code></td>
    </tr>
    <tr>
      <td>File system access</td>
      <td>Not allowed</td>
      <td><code>fs</code> module (<code>fs.readFileSync</code>, <code>fs.writeFileSync</code>)</td>
    </tr>
    <tr>
      <td>Network requests</td>
      <td><code>fetch</code>, <code>XMLHttpRequest</code></td>
      <td><code>fetch</code>, <code>http</code>, <code>https</code> modules</td>
    </tr>
    <tr>
      <td>DOM access</td>
      <td><code>document</code>, <code>window</code></td>
      <td>Not available</td>
    </tr>
  </tbody>
</table>

## Side Quest Browser vs Node.js
```javascript
Browser html: <script type="module" src="main.js"></script>
    main.js
    import ...

Node.js
    ES Modules                                      CommonJS
import { Math2 } from './math2.js';                     // const Math2 = require('./math2');

console.log(Math2.PI);                                  export const Math2 = {
console.log(Math2.square(4));                              PI: 3.14159,
console.log(Math2.cube(2));                                square(x) {
                                                              return x * x;
                                                            },
                                                            cube(x) {
                                                                return x * x * x;
                                                            }
                                                        };
```

## Side Quest ❤️❤️❤️❤️❤️
```javascript
Source: https://learnxinyminutes.com/javascript/

// Optional: Statements can be terminated by ; (recommended C/C++/Java like)
// Object is the object class
Object
ƒ Object() { [native code] }

console.log(Object.getOwnPropertyNames(Math));
VM1230:1 (44) ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'atan2', 'ceil', 'cbrt', 'expm1', 'clz32', 'cos', 'cosh', 'exp', 'floor', 'fround', 'hypot', 'imul', 'log', 'log1p', 'log2', 'log10', 'max', 'min', 'pow', 'random', 'round', 'sign', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc', 'E', 'LN10', 'LN2', 'LOG10E', 'LOG2E', 'PI', 'SQRT1_2', 'SQRT2', 'f16round']

console.log(Object.getPrototypeOf(Math));
VM1262:1 
{__defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, __lookupSetter__: ƒ, …}
constructor: ƒ Object()
hasOwnProperty: ƒ hasOwnProperty()
isPrototypeOf: ƒ isPrototypeOf()
toString: ƒ toString()
valueOf: ƒ valueOf()

console.log(Math.hasOwnProperty.length)
1

Math
Math {abs: ƒ, acos: ƒ, acosh: ƒ, asin: ƒ, asinh: ƒ, …}
E: 2.718281828459045
LN2: 0.6931471805599453
LN10: 2.302585092994046
LOG2E: 1.4426950408889634
LOG10E: 0.4342944819032518
PI: 3.141592653589793
SQRT1_2: 0.7071067811865476
SQRT2: 1.4142135623730951
abs: ƒ abs()
ceil: ƒ ceil()
exp: ƒ exp()
floor: ƒ floor()
random: ƒ random()
round: ƒ round()
sqrt: ƒ sqrt()
trunc: ƒ trunc()
Symbol(Symbol.toStringTag): "Math"

Math.ceil
ƒ ceil() { [native code] }                      // Note: Not local: https://chromium.googlesource.com/v8/v8.git/+/refs/heads/master/src/builtins/math.tq
// Create 2 different ceil functions
function myCeil(x) {
  if (x % 1 === 0) return x;                            // already an integer
  return (x > 0) ? (x - x % 1 + 1) : (x - x % 1);
}
// Create another ciel function
function myCeil(x) {
  var i = parseInt(x);                                  // parseInt converts string to number
  return (x === i || x < 0) ? i : i + 1;
}
window.parseInt
ƒ parseInt() { [native code] }

const obj = { foo: 42, bar: () => "hello" };    // Important: If want types use TypeScript (.ts)

typeof(1)
'number'
typeof(3.5)                             // 9✕10¹⁵ precisely
'number'
typeof("c")
'string'
typeof(true)
'boolean'
typeof(!false)                          // negation
'boolean'
typeof(add)
'function'
typeof(obj)
'object'
typeof(["Hello", "Hackers", 1337])      // arrays are a type of object in JS, but default similar list than an Array
'object'                                // typeof cannot distinguish regular objects {} from arrays [] ⚠️
Array.isArray(arr)
true
arr instanceof Array 
true
Array
ƒ Array() { [native code] }
console.log(Object.getOwnPropertyNames(Array));                                 ⭐⭐⭐⭐⭐
(7) ['length', 'name', 'prototype', 'isArray', 'from', 'fromAsync', 'of']       // Look at prototype
typeof(null)
'object'
// 3 special not-a-real-number values
typeof(Infinity)
'number'
typeof(-Infinity)
'number'
typeof(NaN)
'number'

2**31                           // Power same as in Python
2147483648
35/2                            // float division only in Python / float division vs C/C++ depends on type
17.5
18.5 % 7;                       // Wierd: Can mod fractions in JS 👀
4.5
parseInt("42") 
42
parseInt("101", 2)              // window.parseInt() converts string to int, this case binary to int
5

// Bitwise Operations
5 & 3                           // Bitwise AND: &       0101 & 0011 = 0001 → 1
1
5 | 3                           // Bitwise OR: |        // 0101 | 0011 = 0111 → 7
7
5 ^ 3                           // Bitwise XOR: ^       // 0101 ^ 0011 = 0110 → 6 (return 1 if bits are diff else 0)
6
~5                              // Bitwise NOT: ~       // ~0101 = 1010 → -6 (two's complement)(invert's all bits)
-6
1 << 2;                         // Bitwise Left Shift by 2 up to 32 bits
4
// Negative integers are stored using two's complement in 32 bits
// 8                            // 00000000 00000000 00000000 00001000 (32 bit binary representation)
// ~8 (invert all bits)         // 11111111 11111111 11111111 11110111
// ~8 + 1 (add 1)               // 11111111 11111111 11111111 11111000 (2's complement: To reverse Sub 1 than invert 👀)
-8 >> 2                         // ⚠️ JavaScript uses 32-bit signed integers, so the result can be negative
-2                              // -8 = 11111111111111111111111111111000
                                // >>2 = 11111111111111111111111111111110 → -2
-8 >>> 2;                       // Bitwise Unsigned Right Shift         // Shifts bits to right filling 0s, ignores sign
1073741822                      // window.parseInt() uses unsign integers so bestjust to sub -1 and invert

// Note: == is different in JS, type coercion (not strict like ===)
0 == "0"
true
false == 0 
true
"" == 0 
true
null == undefined;
true
// Strict comparision better to be used in JS ❤️❤️❤️
2 !== 1;
true
2 === 2;
true

// String Concatination on JS very loose
"1, 2, " + 3;
'1, 2, 3'
"Hello " + ["world", 2];
'Hello world,2'

// Simple Math-like object
const Math2 = {
   PI: 3.14159,
   square(x) {
      return x * x;
   },
   cube(x) {
      return x * x * x;
   }
};

console.log(Math2.PI); 
VM1469:1 3.14159
console.log(Math2.square(3));
VM1491:1 9
console.log(Math2.cube(2));
VM1513:1 8

// Inspect properties
console.log(Object.getOwnPropertyNames(Math2));
VM1546:2 (3) ['PI', 'square', 'cube']
console.log(Object.keys(Math2)); 
VM1592:1 (3) ['PI', 'square', 'cube']
console.log(Object.getPrototypeOf(Math2)); 
VM1586:1 {__defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, __lookupSetter__: ƒ, …}

// Browser                                                                              // Node.js
console.log(Object.keys(window));                                                       // console.log(Object.keys(global));                    
VM1600:1 (580) ['0', '1', '2', 'window', 'self', 'document', 'name', 'location', 'customElements', 'history', 'navigation', 'locationbar', 'menubar', 'personalbar', 'scrollbars', 'statusbar', 'toolbar', 'status', 'closed', 'frames', 'length', 'top', 'opener', 'parent', 'frameElement', 'navigator', 'origin', 'external', 'screen', 'innerWidth', 'innerHeight', 'scrollX', 'pageXOffset', 'scrollY', 'pageYOffset', 'visualViewport', 'screenX', 'screenY', 'outerWidth', 'outerHeight', 'devicePixelRatio', 'event', 'clientInformation', 'screenLeft', 'screenTop', 'styleMedia', 'onsearch', 'trustedTypes', 'performance', 'onappinstalled', 'onbeforeinstallprompt', 'crypto', 'indexedDB', 'sessionStorage', 'localStorage', 'onbeforexrselect', 'onabort', 'onbeforeinput', 'onbeforematch', 'onbeforetoggle', 'onblur', 'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 'oncommand', 'oncontentvisibilityautostatechange', 'oncontextlost', 'oncontextmenu', 'oncontextrestored', 'oncuechange', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformdata', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', …]

// Note: Closest thing to default array
let myarr = new Array(4);                 // creates an array of length 4
console.log(myarr);                       // [ <4 empty items> ]
VM3899:2 (4) [empty × 4]

let n = 10;                                 // number of elements
let step = 2;

let myarr = Array.from({ length: Math.ceil(n / step) }, (_, i) => i * step);
console.log(myarr);
VM3957:5 (5) [0, 2, 4, 6, 8]

// let and const cannot be redeclared in the same scope
// delete doesn’t remove them 👀
var arr2 = [];
for (var i = 0; i < 10; i += 2) { ❤️❤️❤️❤️❤️
  arr2.push(i);
}
console.log(arr2);
VM4070:5 (5) [0, 2, 4, 6, 8]

var arr2 = [0, 2, 4, 6, 8];
arr2.forEach(function(element) {                // old way w/ callback fx (hardest)
  console.log(element);
});
VM4092:4 0
VM4092:4 2
VM4092:4 4
VM4092:4 6
VM4092:4 8

arr2.forEach((element, index) => {              // Python enumerate(index,value) but reversed arguments
  console.log(index, element);
});
VM4131:2 0 0
VM4131:2 1 2
VM4131:2 2 4
VM4131:2 3 6
VM4131:2 4 8

arr2.forEach(i => console.log(i));               // modern way, arrow functions (easier, replace i w/ element)
VM4106:1 0
VM4106:1 2
VM4106:1 4
VM4106:1 6
VM4106:1 8

// Note: Closest thing to Hashmap/dictionary in JS is plain object
// Objects are mutable; values can be changed and new keys added
// Access a value that's not yet set, you'll get undefined 👀
// Create dictionary/plain object
let d = {a: 1, b: 2};

// Access properties
console.log(d["a"]);            // array notation
console.log(d.a);               // dot notation
VM3815:2 1
VM3815:3 1
d.c = 3;                        // Add a new property
console.log(d.c);
VM3823:2 3
d.a = 911;                      // Update an existing property
console.log(d.a);
VM3829:2 911
delete d.b;                     // Delete a property
console.log(d.b);               // undefined
VM3839:2 undefined

// Using dynamic keys
let key = "d";
d[key] = 4;
console.log(d.d);
VM3849:4 

// Iterate over keys and values
for (let k in d) {
  console.log(k, d[k]);
}
VM3873:3 a 911
VM3873:3 c 3
VM3873:3 d 4

// Note: Closest thing to Set
var mySet = new Set();          // var so can change use let in real life
console.log(mySet);
VM4156:2 Set(0) {size: 0}

var mySet = new Set([1, 2, 3, 2]);
console.log(mySet);             // duplicates removed
VM4174:2 Set(3) {1, 2, 3}

for (let val of mySet) {
  console.log(val);
}
VM4399:2 1
VM4399:2 2
VM4399:2 3

var arr3 = [...mySet];          // spread operator (convert to arr since set not have indexing)
console.log(arr3[0])
VM4485:1 1

mySet.add(4);
mySet.add(2);                   // 2 already exists → ignored
console.log(mySet);
VM4521:3 Set(4) {1, 2, 3, 4}

// Checking values
console.log(mySet.has(2));
console.log(mySet.has(5));
VM4531:1 true
VM4531:2 false

// Removing values
mySet.delete(2);
console.log(mySet);
mySet.clear();                  // removes all values
console.log(mySet);
VM4541:2 Set(3) {1, 3, 4}
VM4541:5 Set(0) {size: 0}

// Iterating over a Set
var mySet = new Set([10, 20, 30]);

for (let val of mySet) {                    // for...of
  console.log(val);
}

mySet.forEach(val => console.log(val));     // forEach
VM4573:5 10
VM4573:5 20
VM4573:5 30
VM4573:9 10
VM4573:9 20
VM4573:9 30

// Converting between Set and Array
// Array → Set
var arr4 = [1, 2, 2, 3];
var s4 = new Set(arr4);
console.log(s4);
VM4617:3 Set(3) {1, 2, 3}
// Set → Array
console.log([...s4]);
VM4625:1 (3) [1, 2, 3]

// Define the parent class Person
class Person {
   constructor(name, age) {
      this.name = name;
      this.age = age;
   }

   greet() {
      return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
   }
}
undefined

// Employee extends Person
class Employee extends Person {
   constructor(name, age, role) {           // Important: JavaScript does not support multiple constructors like C++/Java/Python 👀
      super(name, age);                     // call parent constructor
      this.role = role;
   }

   getRole() {
      return this.role;
   }
}
undefined

# Create new Employee from constructor
const bob = new Employee("Bob", 25, "Developer");
console.log(bob.greet());
VM1816:1 Hello, my name is Bob and I am 25 years old.
console.log(bob.getRole());
VM1826:1 Developer

// Private #
class Person {
  #secretMethod() {                         // private method
    return "This is private!";
  }

  reveal() {                                // public method
    return this.#secretMethod();
  }
}

const p = new Person();
console.log(p.reveal());
VM1923:1 This is private!
p.#secretMethod(); 
'This is private!'                          // This suppose to not work ⚠️

// Filter to find all built-in functions
Object.getOwnPropertyNames(window).filter(name => typeof window[name] === 'function' || typeof window[name] === 'object')

(1512) ['0', '1', '2', 'Object', 'Function', 'Array', 'Number', 'parseFloat', 'parseInt', 'Boolean', 'String', 'Symbol', 'Date', 'Promise', 'RegExp', 'Error', 'AggregateError', 'EvalError', 'RangeError', 'ReferenceError', 'SyntaxError', 'TypeError', 'URIError', 'globalThis', 'JSON', 'Math', 'Intl', 'ArrayBuffer', 'Atomics', 'Uint8Array', 'Int8Array', 'Uint16Array', 'Int16Array', 'Uint32Array', 'Int32Array', 'BigUint64Array', 'BigInt64Array', 'Uint8ClampedArray', 'Float32Array', 'Float64Array', 'DataView', 'Map', 'BigInt', 'Set', 'Iterator', 'WeakMap', 'WeakSet', 'Proxy', 'Reflect', 'FinalizationRegistry', 'WeakRef', 'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'escape', 'unescape', 'eval', 'isFinite', 'isNaN', 'console', 'Option', 'Image', 'Audio', 'webkitURL', 'webkitRTCPeerConnection', 'webkitMediaStream', 'WebKitMutationObserver', 'WebKitCSSMatrix', 'XPathResult', 'XPathExpression', 'XPathEvaluator', 'XMLSerializer', 'XMLHttpRequestUpload', 'XMLHttpRequestEventTarget', 'XMLHttpRequest', 'XMLDocument', 'WritableStreamDefaultWriter', 'WritableStreamDefaultController', 'WritableStream', 'Worker', 'WindowControlsOverlayGeometryChangeEvent', 'WindowControlsOverlay', 'Window', 'WheelEvent', 'WebSocket', 'WebGLVertexArrayObject', 'WebGLUniformLocation', 'WebGLTransformFeedback', 'WebGLTexture', 'WebGLSync', 'WebGLShaderPrecisionFormat', 'WebGLShader', 'WebGLSampler', 'WebGLRenderingContext', 'WebGLRenderbuffer', 'WebGLQuery', 'WebGLProgram', 'WebGLObject', 'WebGLFramebuffer', …]
```

## Side Quest ❤️❤️❤️❤️❤️ commonly used built-in methods
```javascript
Array Methods
Method	    What it does	                            Example
                                                        ["Hello", 45, true][0]                  → 'Hello'
var myVector = new Array()
console.log(myVector)
VM5426:1 []
myVector.push("Hi", "World", 911, 1337, 214.18, "Bye")  // Add to end
6                               // prototype: length
myVector.shift();               // Remove the first element
myVector.pop();                 // Remove the last element, return element
'Bye'
console.log(myVector)
VM6131:1 (4) ['World', 911, 1337, 214.18]
myVector.unshift(69);                                   // Add as the first element(begin/prepend)

myVector.splice(1,3)                                    // in place (perm, want to assign) and could also add things
(3) [911, 1337, 214.18]
myVector
['World']

myVector.push(1,2,3,4,5,6,7,8,9)
10
myVector.slice(1,4)                                     // slice allows negative index vs .substring (for strings)
(3) [1, 2, 3]
myVector.splice(1,3, "aliens", "have", "came")          // here is splice adding after removing
(3) [1, 2, 3]
myVector
(10) ['World', 'aliens', 'have', 'came', 4, 5, 6, 7, 8, 9]

join        Join all elements with ,                    myVector.join(",")                      → 'World,911,1337,214.18'
map❤️       Transform each element	                    [1,2,3].map(x => x*2)                   → [2,4,6]
filter❤️    Keep elements that pass a test	            [1,2,3,4].filter(x => x%2===0)          → [2,4]
reduce❤️    Reduce array to single value	            [1,2,3].reduce((a,b)=>a+b)              → 6
forEach❤️   Loop through elements	                    [1,2,3].forEach(x => console.log(x))
find	    Find first matching element	                [1,2,3].find(x => x>1)                  → 2
some	    Check if any element passes	                [1,2,3].some(x=>x>2)                    → true
every	    Check if all pass	                        [1,2,3].every(x=>x>0)                   → true
includes	Check if array contains value	            [1,2,3].includes(2)                     → true
sort	    Sort elements	                            [3,1,2].sort()                          → [1,2,3]

String Methods
Method	                                                Example
                                                        "Hello".length;                         5                   // property no len() or strlen()
                                                        "Hi Hackers".charAt(0);                 → 'H'
                                                        "Hi Hackers"[0];                        → 'H'
substring                                               "Hi Hackers".substring(0, 5);           → 'Hi Ha'           // excludes 5 like Python
split	                                                "a,b,c".split(",")                      → ["a","b","c"]
join	                                                ["a","b"].join("-")                     → "a-b"
trim	                                                " hi ".trim()                           → "hi"
replace	                                                "abc".replace("b","x")                  → "axc"
includes                                                "hello".includes("ell")                 → true
startsWith	                                            "hello".startsWith("he")                → true
endsWith	                                            "hello".endsWith("lo")                  → true
toUpperCase / toLowerCase	                            "hi".toUpperCase()                      → "HI"

Object / Utility Functions
Function	                                            Example
Object.keys(obj)	                                    List keys: {a:1,b:2}                    → ["a","b"]
Object.values(obj)	                                    List values: {a:1,b:2}                  → [1,2]
Object.entries(obj)	                                    Key/value pairs: {a:1}                  → [["a",1]]
Object.assign(target, source)	                        Merge objects: {a:1}, {b:2}             → {a:1,b:2}
Object.hasOwn()	                                        Check key exists (newer)

Global / Utility Functions
Function	                                            Example
parseInt("42")	                                        Convert string → int
parseFloat("3.14")	                                    String → float
isNaN(value)	                                        Check if value is Not-a-Number
Number(value)	                                        Convert to number
Boolean(value)	                                        Convert to true/false
Date.now()	                                            Current timestamp
setTimeout() / setInterval()	                        Delayed / repeated actions
JSON.stringify() / JSON.parse()	                        Convert objects ↔ JSON strings

Math Functions
Math.ceil(x), Math.floor(x), Math.round(x) → rounding
Math.max(a,b,...) / Math.min(a,b,...) → find extremes
Math.random() → random number between 0 and 1
Math.abs(x) → absolute value
Math.pow(a,b) / ** → exponentiation
```

## Side Quest ❤️❤️❤️❤️❤️ Logic and Control Structures
```javascript

```

## Back to README.md
[BACK](../README.md)