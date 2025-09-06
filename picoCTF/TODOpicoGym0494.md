# picoGym Level 494: Pachinko 🧠 (Didn't Solve Correctly)
Source: https://play.picoctf.org/practice/challenge/494

## Goal
History has failed us, but no matter.<br>
Server source: https://challenge-files.picoctf.net/c_activist_birds/7eac27979c12e4bd449f03e40a8492044221b7d2a96ac85f1150e30983c56eac/server.tar.gz <br>
There are two flags in this challenge. Submit flag one here, and flag two in <b>Pachinko Revisited</b><br>
Website: http://activist-birds.picoctf.net:64694/

## What I learned
```
Most submissions just return "status":"success" without the flag
Brute Force: Occasionally server randomly responds with "flag":"picoCTF{...}"
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://challenge-files.picoctf.net/c_activist_birds/7eac27979c12e4bd449f03e40a8492044221b7d2a96ac85f1150e30983c56eac/server.tar.gz ⌨️
--2025-09-02 21:37:35--  https://challenge-files.picoctf.net/c_activist_birds/7eac27979c12e4bd449f03e40a8492044221b7d2a96ac85f1150e30983c56eac/server.tar.gz
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.95, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 56907 (56K) [application/octet-stream]
Saving to: 'server.tar.gz'

server.tar.gz                                              100%[======================================================================================================================================>]  55.57K  --.-KB/s    in 0.03s   

2025-09-02 21:37:35 (2.01 MB/s) - 'server.tar.gz' saved [56907/56907]

AsianHacker-picoctf@webshell:/tmp$ gunzip server.tar.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ tar -xf server.tar ⌨️
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  node-compile-cache  server  server.tar
AsianHacker-picoctf@webshell:/tmp$ cd server/ ⌨️
AsianHacker-picoctf@webshell:/tmp/server$ ls ⌨️
Dockerfile  cpu.js  index.js  package-lock.json  package.json  programs  public  utils.js  wasm
AsianHacker-picoctf@webshell:/tmp/server$ cat index.js ⌨️ 
const express = require('express');
const morgan = require('morgan');
const path = require('path');
const fs = require('fs').promises;
const { 
    checkInt,
    serializeCircuit
} = require('./utils');
const { runCPU } = require('./cpu');

const app = express();
const port = process.env.PORT || 3000;

app.use(morgan('dev'));
app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

const FLAG1 = process.env.FLAG1 || 'FLAG1';
const FLAG2 = process.env.FLAG2 || 'FLAG2';

function doRun(res, memory) {
  const flag = runCPU(memory);
  const result = memory[0x1000] | (memory[0x1001] << 8);
  if (memory.length < 0x1000) {
    return res.status(500).json({ error: 'Memory length is too short' });
  }

  let resp = "";

  if (flag) {
    resp += FLAG2 + "\n";
  } else {
    if (result === 0x1337) { 👀
      resp += FLAG1 + "\n";
    } else if (result === 0x3333) {
      resp += "wrong answer :(\n";
    } else {
      resp += "unknown error code: " + result;
    }
  }

  res.status(200).json({ status: 'success', flag: resp });
}

// Admin endpoint
app.post('/flag', async (req, res) => {
  if (req.body.flag1 !== FLAG1 || req.body.flag2 !== FLAG2) {
    return res.status(400).json({ error: 'Invalid password' });
  }

  const binary = await fs.readFile('./programs/flag.bin');
  const memory = new Uint8Array(binary.length);
  memory.set(binary);

  doRun(res, memory);
});

// Add the check endpoint
app.post('/check', async (req, res) => {
    const circuit = req.body.circuit;

    if (!Array.isArray(circuit) || 
        !circuit.every(entry => checkInt(entry?.input1) && 
                                checkInt(entry?.input2) && 
                                checkInt(entry?.output))) {
        return res.status(400).end();
    }

    const program = await fs.readFile('./programs/nand_checker.bin');
    
    // Generate random input state with only 0x0000 or 0xffff values
    const inputState = new Uint16Array(4);
    for (let i = 0; i < 4; i++) {
        inputState[i] = Math.random() < 0.5 ? 0x0000 : 0xffff;
    }
    
    // Create output state as inverse of input
    const outputState = new Uint16Array(4);
    for (let i = 0; i < 4; i++) {
        outputState[i] = inputState[i] === 0xffff ? 0x0000 : 0xffff;
    }
    
    const serialized = serializeCircuit(
        circuit,
        program,
        inputState,
        outputState
    );

    doRun(res, serialized);
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

Browser: view-source:http://activist-birds.picoctf.net:64694/ ⌨️
# View Page Source
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NAND Simulator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>NAND Simulator</h1>
    <div id="controls">
        <button id="reset-btn" onclick="resetGame()">Reset Circuit</button>
        <button onclick="addIntermediateNode()">Add Intermediate Node</button>
        <button id="play-btn" onclick="playAnimation()">Play Animation</button>
        <button id="submit-btn" onclick="submitCircuit()">Submit Circuit</button>
    </div>
    <div class="game-wrapper">
        <div id="game-container">
            <div class="goal-display"></div>
        </div>
    </div>

    <script>
        // State
        let selectedNode = null;
        let nodes = [];
        let connections = [];
        let tooltip = null;
        let nextNodeId = 2; // Start from 2 since output is 1
        let outputNodes = [];
        let isDragging = false;
        let dragTarget = null;
        let currentX, currentY, initialX, initialY;
        let ballArrivals = new Map();

        // Constants
        const GOALS = {
            flip: {
                description: 'Flip the outputs!'
            }
        };

        // Node Creation and Management
        function createNode(x, y, value, type) {
            const node = document.createElement('div');
            node.className = `node ${type}-node`;
            node.style.left = x + 'px';
            node.style.top = y + 'px';
            node.dataset.x = x;
            node.dataset.y = y;
            node.dataset.value = value;
            node.dataset.type = type;
            node.id = 'node-' + Math.random().toString(36).substr(2, 9);
            
            if (type === 'output') {
                node.dataset.nodeId = (outputNodes.length + 1).toString();
            } else {
                node.dataset.nodeId = nextNodeId.toString();
                nextNodeId++;
            }
            node.textContent = node.dataset.nodeId;
            
            node.addEventListener('mousedown', startDragging);
            node.addEventListener('click', () => handleNodeClick(node));
            node.addEventListener('mousemove', (e) => showTooltip(node, e));
            node.addEventListener('mouseout', hideTooltip);
            
            document.getElementById('game-container').appendChild(node);
            (type === 'output' ? outputNodes : nodes).push(node);
            return node;
        }

        function addIntermediateNode() {
            const x = Math.random() * 800 + 50;
            const y = Math.random() * 100 + 50;
            return createNode(x, y, '1', 'nand');
        }

        function createOutputNodes() {
            const containerWidth = 900;
            const containerHeight = 600;
            const spacing = 150;
            const startX = containerWidth/2 - (spacing * 1.5);
            for (let i = 0; i < 4; i++) {
                createNode(startX + (i * spacing), containerHeight - 150, '?', 'output');
            }
        }

        // Node Value Updates
        function updateNandValue(nandNode) {
            const input1 = nodes.find(n => n.id === nandNode.dataset.input1);
            const input2 = nodes.find(n => n.id === nandNode.dataset.input2);
            
            if (input1 && input2) {
                const val1 = parseInt(input1.dataset.value);
                const val2 = parseInt(input2.dataset.value);
                const nandResult = ~(val1 & val2) & 1;
                nandNode.dataset.value = nandResult;
                
                // Propagate updates
                nodes.forEach(node => {
                    if ((node.dataset.input1 === nandNode.id || node.dataset.input2 === nandNode.id) && 
                        node.dataset.type === 'nand') {
                        updateNandValue(node);
                    }
                });
                
                outputNodes.forEach(node => {
                    if (node.dataset.input1 === nandNode.id || node.dataset.input2 === nandNode.id) {
                        node.dataset.value = nandNode.dataset.value;
                    }
                });
            }
        }

        // Connection Management
        function drawConnection(from, to) {
            const connection = document.createElement('div');
            connection.className = 'connection';
            connection.dataset.fromId = from.id;
            connection.dataset.toId = to.id;
            
            const fromX = parseFloat(from.dataset.x) + from.offsetWidth/2;
            const fromY = parseFloat(from.dataset.y) + from.offsetHeight/2;
            const toX = parseFloat(to.dataset.x) + to.offsetWidth/2;
            const toY = parseFloat(to.dataset.y) + to.offsetHeight/2;
            
            const dx = toX - fromX;
            const dy = toY - fromY;
            const length = Math.sqrt(dx * dx + dy * dy);
            const angle = Math.atan2(dy, dx) * 180 / Math.PI;
            
            connection.style.width = length + 'px';
            connection.style.left = fromX + 'px';
            connection.style.top = fromY + 'px';
            connection.style.transform = `rotate(${angle}deg)`;
            
            document.getElementById('game-container').appendChild(connection);
            connections.push(connection);
        }

        function updateConnections() {
            connections.forEach(conn => conn.remove());
            connections = [];
            
            const findNodeById = (id) => nodes.find(n => n.id === id) || outputNodes.find(n => n.id === id);
            
            // Draw all connections
            [...nodes, ...outputNodes].forEach(node => {
                if (node.dataset.input1) {
                    const input1 = findNodeById(node.dataset.input1);
                    if (input1) drawConnection(input1, node);
                }
                if (node.dataset.input2) {
                    const input2 = findNodeById(node.dataset.input2);
                    if (input2) drawConnection(input2, node);
                }
            });
        }

        // Node Interaction
        function handleNodeClick(node) {
            if (!selectedNode) {
                if (node.dataset.type === 'output') return;
                selectedNode = node;
                node.classList.add('selected');
            } else if (selectedNode !== node) {
                const existingInputs = [];
                if (node.dataset.input1) existingInputs.push(node.dataset.input1);
                if (node.dataset.input2) existingInputs.push(node.dataset.input2);
                
                if (!existingInputs.includes(selectedNode.id) && existingInputs.length < 2) {
                    if (!node.dataset.input1) {
                        node.dataset.input1 = selectedNode.id;
                    } else {
                        node.dataset.input2 = selectedNode.id;
                    }
                    
                    drawConnection(selectedNode, node);
                    if (node.dataset.type === 'nand') {
                        updateNandValue(node);
                    } else {
                        node.dataset.value = selectedNode.dataset.value;
                    }
                }
                
                selectedNode.classList.remove('selected');
                selectedNode = null;
            }
        }

        // Drag and Drop
        function startDragging(e) {
            dragTarget = e.target;
            isDragging = true;
            
            const containerRect = document.getElementById('game-container').getBoundingClientRect();
            const nodeRect = dragTarget.getBoundingClientRect();
            
            initialX = e.clientX - nodeRect.left;
            initialY = e.clientY - nodeRect.top;
            
            dragTarget.classList.add('dragging');
            
            document.addEventListener('mousemove', drag);
            document.addEventListener('mouseup', stopDragging);
        }

        function drag(e) {
            if (!isDragging) return;
            e.preventDefault();
            
            const containerRect = document.getElementById('game-container').getBoundingClientRect();
            
            currentX = e.clientX - containerRect.left - initialX;
            currentY = e.clientY - containerRect.top - initialY;
            
            currentX = Math.max(0, Math.min(currentX, containerRect.width - dragTarget.offsetWidth));
            currentY = Math.max(0, Math.min(currentY, containerRect.height - dragTarget.offsetHeight));
            
            dragTarget.style.left = currentX + 'px';
            dragTarget.style.top = currentY + 'px';
            dragTarget.dataset.x = currentX;
            dragTarget.dataset.y = currentY;
            
            updateConnections();
        }

        function stopDragging() {
            isDragging = false;
            if (dragTarget) {
                dragTarget.classList.remove('dragging');
                dragTarget = null;
            }
            document.removeEventListener('mousemove', drag);
            document.removeEventListener('mouseup', stopDragging);
        }

        // UI Updates
        function updateCircuitSerialization() {
            const serializationDiv = document.getElementById('circuit-serialization');
            let serialization = '';
            
            const findNodeById = (id) => nodes.find(n => n.id === id) || outputNodes.find(n => n.id === id);
            
            nodes.filter(n => n.dataset.type === 'nand' && n.dataset.input1 && n.dataset.input2).forEach(nand => {
                const input1 = findNodeById(nand.dataset.input1);
                const input2 = findNodeById(nand.dataset.input2);
                if (input1 && input2) {
                    serialization += `${input1.dataset.nodeId} ${input2.dataset.nodeId} ${nand.dataset.nodeId}<br>`;
                }
            });
            
            outputNodes.forEach(output => {
                if (output.dataset.input1 && output.dataset.input2) {
                    const input1 = findNodeById(output.dataset.input1);
                    const input2 = findNodeById(output.dataset.input2);
                    if (input1 && input2) {
                        serialization += `${input1.dataset.nodeId} ${input2.dataset.nodeId} 1<br>`;
                    }
                }
            });
            
            serializationDiv.innerHTML = serialization;
        }

        function updateTruthTable() {
            const table = document.getElementById('truth-table-content');
            const goal = GOALS.xor;
            
            let html = '<table><tr><th>Input A</th><th>Input B</th><th>Target</th><th>Current</th></tr>';
            
            const inputNodes = nodes.filter(n => n.dataset.type === 'input')
                                   .sort((a, b) => parseFloat(a.dataset.x) - parseFloat(b.dataset.x));
            const outputNode = outputNodes[0];
            
            goal.truthTable.forEach(entry => {
                const isCurrentRow = inputNodes.length === 2 && 
                                   parseInt(inputNodes[0].dataset.value) === entry.inputs[0] && 
                                   parseInt(inputNodes[1].dataset.value) === entry.inputs[1];
                
                const currentOutput = isCurrentRow ? (outputNode ? outputNode.dataset.value : '?') : '-';
                
                html += `<tr class="${isCurrentRow ? 'current' : ''}">
                    <td>${entry.inputs[0]}</td>
                    <td>${entry.inputs[1]}</td>
                    <td>${entry.output}</td>
                    <td>${currentOutput}</td>
                </tr>`;
            });
            
            html += '</table>';
            table.innerHTML = html;
        }

        function checkCircuit() {
            const outputNode = outputNodes[0];
            if (!outputNode || outputNode.dataset.value === '?') return;

            const goal = GOALS.xor;
            const inputs = nodes.filter(n => n.dataset.type === 'input')
                              .map(n => parseInt(n.dataset.value));
            
            const entry = goal.truthTable.find(e => 
                e.inputs.every((val, idx) => val === inputs[idx])
            );

            if (entry && parseInt(outputNode.dataset.value) === entry.output) {
                outputNode.classList.add('correct');
            } else {
                outputNode.classList.remove('correct');
            }
            
            updateTruthTable();
        }

        // Tooltip Management
        function createTooltip() {
            tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            document.body.appendChild(tooltip);
        }

        function showTooltip(node, event) {
            const type = node.dataset.type === 'input' ? 'Input' : 
                        node.dataset.type === 'output' ? 'Target Output' : 'NAND';
            tooltip.textContent = `${type} Node: ${node.dataset.value}`;
            tooltip.style.left = event.pageX + 10 + 'px';
            tooltip.style.top = event.pageY + 10 + 'px';
            tooltip.style.opacity = '1';
        }

        function hideTooltip() {
            if (tooltip) tooltip.style.opacity = '0';
        }

        // Animation
        async function playAnimation() {
            const playBtn = document.getElementById('play-btn');
            playBtn.disabled = true;
            
            try {
                ballArrivals.clear();
                nodes.filter(n => n.dataset.type === 'nand')
                     .forEach(nand => ballArrivals.set(nand.id, new Set()));
                
                const inputNodes = nodes.filter(n => n.dataset.type === 'input');
                await Promise.all(inputNodes.map(node => sendBallFromNode(node)));
            } catch (error) {
                console.error('Animation error:', error);
            } finally {
                playBtn.disabled = false;
            }
        }

        async function sendBallFromNode(node) {
            node.style.transform = 'scale(1.2)';
            await new Promise(resolve => setTimeout(resolve, 100));
            node.style.transform = '';
            
            const children = findChildNodes(node);
            await Promise.all(children.map(async (child) => {
                const ball = createBall(node);
                await animateBallToNode(ball, node, child);
                
                if (child.dataset.type === 'nand') {
                    const arrivals = ballArrivals.get(child.id);
                    arrivals.add(node.id);
                    
                    if (arrivals.has(child.dataset.input1) && arrivals.has(child.dataset.input2)) {
                        const input1 = nodes.find(n => n.id === child.dataset.input1);
                        const input2 = nodes.find(n => n.id === child.dataset.input2);
                        updateNandValue(child);
                        await sendBallFromNode(child);
                    }
                }
                
                ball.remove();
            }));
        }

        function findChildNodes(node) {
            if (node.dataset.type === 'input' || node.dataset.type === 'nand') {
                return [...nodes, ...outputNodes].filter(n => 
                    n.dataset.input1 === node.id || n.dataset.input2 === node.id
                );
            }
            return [];
        }

        async function animateBallToNode(ball, fromNode, toNode) {
            const startX = parseFloat(fromNode.dataset.x) + fromNode.offsetWidth/2 - 6;
            const startY = parseFloat(fromNode.dataset.y) + fromNode.offsetHeight/2 - 6;
            ball.style.left = startX + 'px';
            ball.style.top = startY + 'px';
            
            await new Promise(resolve => setTimeout(resolve, 100));
            
            const endX = parseFloat(toNode.dataset.x) + toNode.offsetWidth/2 - 6;
            const endY = parseFloat(toNode.dataset.y) + toNode.offsetHeight/2 - 6;
            ball.style.transition = 'all 0.5s ease-in-out';
            ball.style.left = endX + 'px';
            ball.style.top = endY + 'px';
            
            await new Promise(resolve => setTimeout(resolve, 500));
            
            toNode.style.transform = 'scale(1.2)';
            await new Promise(resolve => setTimeout(resolve, 100));
            toNode.style.transform = '';
        }

        function createBall(startNode) {
            const ball = document.createElement('div');
            ball.className = 'ball';
            const x = parseFloat(startNode.dataset.x) + startNode.offsetWidth/2 - 6;
            const y = parseFloat(startNode.dataset.y) + startNode.offsetHeight/2 - 6;
            ball.style.left = x + 'px';
            ball.style.top = y + 'px';
            document.getElementById('game-container').appendChild(ball);
            return ball;
        }

        // Game Management
        function resetGame() {
            nodes.forEach(node => node.remove());
            outputNodes.forEach(node => node.remove());
            connections.forEach(conn => conn.remove());
            nodes = [];
            outputNodes = [];
            connections = [];
            selectedNode = null;
            nextNodeId = 5; // Start after output nodes (1-4)

            const spacing = 150;
            const startX = 100;
            for (let i = 0; i < 4; i++) {
                const x = startX + (i * spacing);
                const y = Math.random() * 100 + 50;
                const value = Math.round(Math.random());
                createNode(x, y, value, 'input');
            }
            createOutputNodes();
            updateGoalDisplay();
        }

        function updateGoalDisplay() {
            const goalDisplay = document.querySelector('.goal-display');
            goalDisplay.textContent = GOALS.xor.description;
        }

        // Event Listeners
        document.getElementById('game-container').addEventListener('click', function(e) {
            if (e.target === this && selectedNode) {
                selectedNode.classList.remove('selected');
                selectedNode = null;
            }
        });

        // Initialize
        createTooltip();
        resetGame();

        async function submitCircuit() {
            // Convert nodes to circuit format
            const circuit = [];
            
            // Add NAND gates
            nodes.forEach(node => {
                if (node.dataset.input1 && node.dataset.input2) {
                    circuit.push({
                        input1: parseInt(nodes.find(n => n.id === node.dataset.input1)?.dataset.nodeId),
                        input2: parseInt(nodes.find(n => n.id === node.dataset.input2)?.dataset.nodeId),
                        output: parseInt(node.dataset.nodeId)
                    });
                }
            });

            // Add all output nodes
            outputNodes.forEach((outputNode, index) => {
                if (outputNode.dataset.input1 && outputNode.dataset.input2) {
                    circuit.push({
                        input1: parseInt(nodes.find(n => n.id === outputNode.dataset.input1)?.dataset.nodeId),
                        input2: parseInt(nodes.find(n => n.id === outputNode.dataset.input2)?.dataset.nodeId),
                        output: index + 1  // Output nodes are numbered 1-4
                    });
                }
            });

            try {
                const response = await fetch('/check', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ circuit })
                });

                const result = await response.json();
                if (result.flag) {
                    alert('Congratulations! Flag: ' + result.flag);
                } else {
                    alert('Circuit submitted successfully!');
                }
            } catch (error) {
                console.error('Error submitting circuit:', error);
                alert('Error submitting circuit. Please try again.');
            }
        }
    </script>
</body>
</html>  

AsianHacker-picoctf@webshell:/tmp/server$ cat utils.js ⌨️
const fs = require('fs');
const path = require('path');

// JSON parsing utilities
function loadCpuSignals() {
    const json = JSON.parse(fs.readFileSync(path.join(__dirname, '../verilog/cpu.json'), 'utf8'));
    return {
        clock: getBitFromJson(json, "clock"),
        addr: getBitsFromJson(json, "addr"),
        inp_val: getBitsFromJson(json, "inp_val"),
        out_val: getBitsFromJson(json, "out_val"),
        reset: getBitFromJson(json, "reset"),
        write_enable: getBitFromJson(json, "write_enable"),
        halted: getBitFromJson(json, "halted"),
        flag: getBitFromJson(json, "flag"),
    };
}

function getBitFromJson(json, name) {
    const bits = getBitsFromJson(json, name);
    if (bits.length !== 1) throw new Error(`Expected single bit for ${name}`);
    return bits[0];
}

function getBitsFromJson(json, name) {
    const ports = json.modules.cpu.netnames;
    const bits = ports[name].bits;
    return bits.map(v => {
        if (typeof v === 'string' && v === '0') return 0;
        const n = parseInt(v);
        if (n === 0 || n === 1) throw new Error(`Unexpected 0 or 1 as non-string value`);
        return n;
    });
}

// Bit manipulation utilities
function getBitsValue(state, bits) {
    let result = 0;
    for (let i = 0; i < bits.length; i++) {
        result |= ((state[bits[i]] >> 7) & 1) << i;
    }
    return result;
}

function setBits(state, bits, value) {
    for (let i = 0; i < bits.length; i++) {
        state[bits[i]] = ((value >> i) & 1) ? 255 : 0;
    }
}

function splitBits(bits, at) {
    return [bits.slice(0, at), bits.slice(at)];
}

// Circuit validation utilities
function checkInt(value) {
    if (value === undefined) return false;
    if (typeof value !== 'number') return false;
    if (value !== Math.floor(value)) return false;
    return value > 0 && value <= 0xFFFF;
}

function serializeCircuit(circuit, program, inputState, outputState) {
    const memory = new Uint8Array(65536); // 64KB memory

    // Copy program at start
    memory.set(program);

    // Serialize output state at 0x1000
const outputView = new Uint16Array(memory.buffer, 0x1000);
    outputView[0] = outputState.length;
    outputView.set(outputState, 1);

    // Serialize input state at 0x2000
    const inputView = new Uint16Array(memory.buffer, 0x2000);
    inputView.set(inputState, outputState.length + 1);

    // Serialize circuit at 0x3000
    const circuitView = new Uint16Array(memory.buffer, 0x3000);
    circuit.forEach((gate, i) => {
        const offset = i * 3;
        circuitView[offset] = gate.input1;
        circuitView[offset + 1] = gate.input2;
        circuitView[offset + 2] = gate.output;
    });

    return memory;
}

module.exports = {
    loadCpuSignals,
    getBitsValue,
    setBits,
    splitBits,
    checkInt,
    serializeCircuit
};

AsianHacker-picoctf@webshell:/tmp/server$ cd programs/ ⌨️
AsianHacker-picoctf@webshell:/tmp/server/programs$ ls ⌨️
flag.bin  nand_checker.bin
AsianHacker-picoctf@webshell:/tmp/server/programs$ objdump -b binary -m i386:x86-64 -D nand_checker.bin ⌨️

nand_checker.bin:     file format binary

Disassembly of section .data:

0000000000000000 <.data>:
   0:   4d 00 00                rex.WRB add %r8b,(%r8)
   3:   30 5d 00                xor    %bl,0x0(%rbp)
   6:   00 10                   add    %dl,(%rax)
   8:   6d                      insl   (%dx),%es:(%rdi)
   9:   00 00                   add    %al,(%rax)
   b:   20 08                   and    %cl,(%rax)
   d:   00 01                   add    %al,(%rcx)
   f:   04 2d                   add    $0x2d,%al
  11:   00 00                   add    %al,(%rax)
  13:   10 1b                   adc    %bl,(%rbx)
  15:   00 04 02                add    %al,(%rdx,%rax,1)
  18:   1c 22                   sbb    $0x22,%al
  1a:   17                      (bad)  
  1b:   12 1c 4c                adc    (%rsp,%rcx,2),%bl
  1e:   18 00                   sbb    %al,(%rax)
  20:   1c 14                   sbb    $0x14,%al
  22:   0b 04 44                or     (%rsp,%rax,2),%eax
  25:   02 1b                   add    (%rbx),%bl
  27:   04 44                   add    $0x44,%al
  29:   02 2b                   add    (%rbx),%ch
  2b:   04 44                   add    $0x44,%al
  2d:   02 0c 4c                add    (%rsp,%rcx,2),%cl
  30:   1c 4c                   sbb    $0x4c,%al
  32:   2c 4c                   sub    $0x4c,%al
  34:   01 00                   add    %eax,(%rax)
  36:   11 01                   adc    %eax,(%rcx)
  38:   21 02                   and    %eax,(%rdx)
  3a:   01 06                   add    %eax,(%rsi)
  3c:   11 06                   adc    %eax,(%rsi)
  3e:   21 06                   and    %eax,(%rsi)
  40:   0b 00                   or     (%rax),%eax
  42:   1b 01                   sbb    (%rcx),%eax
  44:   06                      (bad)  
  45:   01 29                   add    %ebp,(%rcx)
  47:   00 78 00                add    %bh,0x0(%rax)
  4a:   7c 22                   jl     0x6e
  4c:   0b 05 1d 00 ff ff       or     -0xffe3(%rip),%eax        # 0xffffffffffff006f
  52:   28 02                   sub    %al,(%rdx)
  54:   78 00                   js     0x56
  56:   51                      push   %rcx
  57:   02 61 02                add    0x2(%rcx),%ah
  5a:   3b 05 4b 06 37 73       cmp    0x7337064b(%rip),%eax        # 0x733706ab
  60:   47 74 31                rex.RXB je 0x94
  63:   04 3c                   add    $0x3c,%al
  65:   6c                      insb   (%dx),%es:(%rdi)
  66:   37                      (bad)  
  67:   32 3c 6c                xor    (%rsp,%rbp,2),%bh
  6a:   7c 72                   jl     0xde
  6c:   01 01                   add    %eax,(%rcx)
  6e:   0c 7e                   or     $0x7e,%al
  70:   7c 56                   jl     0xc8
  72:   0d 00 33 33 5d          or     $0x5d333300,%eax
  77:   00 00                   add    %al,(%rax)
  79:   10 59 00                adc    %bl,0x0(%rcx)
  7c:   0f 00 0d 00 37 13 5d    str    0x5d133700(%rip)        # 0x5d133783
  83:   00 00                   add    %al,(%rax)
  85:   10 59 00                adc    %bl,0x0(%rcx)
  88:   0f                      .byte 0xf
        ...
AsianHacker-picoctf@webshell:/tmp/server/programs$ objdump -b binary -m i386:x86-64 -D flag.bin ⌨️       

flag.bin:     file format binary

Disassembly of section .data:

0000000000000000 <.data>:
   0:   0d 00 73 6f 1d          or     $0x1d6f7300,%eax
   5:   00 63 65                add    %ah,0x65(%rbx)
   8:   2d 00 69 2e 3d          sub    $0x3d2e6900,%eax
   d:   00 00                   add    %al,(%rax)
   f:   6f                      outsl  %ds:(%rsi),(%dx)
  10:   0e                      (bad)  
  11:   00 0f                   add    %cl,(%rdi)
        ...

# Inspect: Network
# Submit there is /check 🕵️‍♀️

# Burp Suite, Connect and Submit
# Request
POST /check HTTP/1.1
Host: activist-birds.picoctf.net:60948
Content-Length: 118
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://activist-birds.picoctf.net:60948
Referer: http://activist-birds.picoctf.net:60948/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"circuit":[{"input1":5,"input2":6,"output":1},{"input1":6,"input2":7,"output":2},{"input1":7,"input2":8,"output":3}]} 👀

# Use Request
AsianHacker-picoctf@webshell:/tmp$ vi server.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat server.py ⌨️
import requests

url = "http://activist-birds.picoctf.net:60948/check"
data = {
  "circuit":[
    {"input1":5,"input2":6,"output":1},
    {"input1":6,"input2":7,"output":2},
    {"input1":7,"input2":8,"output":3}]
}

for i in range(100):
  res = requests.post(url, json=data).text
  if "pico" in res:
    print(res)
    break

AsianHacker-picoctf@webshell:/tmp$ python3 server.py ⌨️
{"status":"success","flag":"picoCTF{p4ch1nk0_f146_0n3_e947b9d7}\n"} 🔐

Method 2: Keep Submit until get flag
```

## Flag
picoCTF{p4ch1nk0_f146_0n3_e947b9d7}

## Continue
[Continue](./picoGym0494.md)