Harkirat Singh
```
Code a simple Full Stack app with me
Youtube: https://www.youtube.com/watch?v=pfZT6Opgy4o

GitHub: Real time chat
Build a simple chat application using raw websockets in Node.js
github.com/hkirat/real-time-chat

BackEnd
    Next.JS
    WebSocket Server
FrontEnd

# Building a TypeScript Node.js project
npx tsc --init              # initializes/enables TypeScript
                            # and creates tsconfig.json and sets up TypeScript compiler
npm init -y                 # create package.json w/ default values to manage dependencies
vi tsconfig.json
    "outDir": "./dist",     # modify, where js files located
    "rootDir": "./src",     # modify, where index.ts located
npm install typescript      # install TypeScript locally

File Hierachy
    real-time-chat-app/
    ├── src/
    │   └── index.ts
    ├── package.json
    ├── tsconfig.json
    ├── README.md
    └── .gitignore

# git add and commit
ga .
git commit -m "added package.json and tsconfig.json"
git push

# Add libraries that help w/ websocket
Google: npm websocket library
https://www.npmjs.com/package/ws
npm install ws                          # package.json and node_modules

# Note: Socket.io is easier
# Copy the example and change the way import library
var WebSocketServer = require('websocket').server; → import {server} from "websocket"
npm i --save @types/websocket           # installs TypeScript type definitions for websocket npm package (from DefinitelyTyped)
                                        # some npm packages (websocket) written in plain JS and don't include TypeScript types
# add type: any
var server = http.createServer(function(request: any, response: any){})
server.listen(8080, function(){})

# add const and change library with alias
import {server as WebSocket Server} from "websocket"
const wsServer = new WebSocketServer({})

# if don't know argument type try string
function originIsAllowed(origin: string) {}

# in src create a store folder and Store.ts file
# Singleton class

20:05 (TO-DO)
```