const canva = document.getElementById("graph-canvas");
const width = canva.clientWidth;
const height = canva.clientHeight;

const nodes = adjmat.map((_, i) => ({ id: i + 1 }));

const edges = [];
for (let i = 0; i < adjmat.length; i++) {
    for (let j = i; j < adjmat[i].length; j++) {
        if (adjmat[i][j] === 1) {
            const edge = { source: i + 1, target: j + 1 };
            edges.push(edge);
        }
    }
}

const radius = Math.min(width, height) / 2 - 40;
const centerX = width / 2;
const centerY = height / 2;

nodes.forEach((node, index) => {
    const angle = (index / nodes.length) * 2 * Math.PI;
    node.x = centerX + radius * Math.cos(angle);
    node.y = centerY + radius * Math.sin(angle);
});

canva.innerHTML = '';

edges.forEach(edge => {
    const source = nodes[edge.source - 1];
    const target = nodes[edge.target - 1];
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", source.x);
    line.setAttribute("y1", source.y);
    line.setAttribute("x2", target.x);
    line.setAttribute("y2", target.y);
    line.setAttribute("stroke", "#000");
    line.setAttribute("stroke-width", 2);
    canva.appendChild(line);
    edge.line = line;
    edge.sourceNode = source;
    edge.targetNode = target;
});

nodes.forEach((node, index) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", node.x);
    circle.setAttribute("cy", node.y);
    circle.setAttribute("r", 15);
    circle.setAttribute("fill", "#1be7a3");
    circle.setAttribute("stroke", "#000");
    circle.setAttribute("stroke-width", 2);
    canva.appendChild(circle);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", node.x);
    text.setAttribute("y", node.y + 5);
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("font-size", "12px");
    text.setAttribute("fill", "#000");
    text.textContent = node.id;
    canva.appendChild(text);

    node.circle = circle;
    node.text = text;
    node.edges = [];
    node.nodeId = node.id;
});

edges.forEach(edge => {
    edge.sourceNode.edges.push(edge);
    edge.targetNode.edges.push(edge);
});

let selectedNode = null;

canva.addEventListener("mousemove", function(event) {
    if (selectedNode) {
        const pt = canva.createSVGPoint();
        pt.x = event.clientX;
        pt.y = event.clientY;
        const svgP = pt.matrixTransform(canva.getScreenCTM().inverse());

        selectedNode.x = svgP.x;
        selectedNode.y = svgP.y;

        selectedNode.circle.setAttribute("cx", svgP.x);
        selectedNode.circle.setAttribute("cy", svgP.y);
        selectedNode.text.setAttribute("x", svgP.x);
        selectedNode.text.setAttribute("y", svgP.y + 5);

        selectedNode.edges.forEach(edge => {
            if (edge.sourceNode === selectedNode) {
                edge.line.setAttribute("x1", svgP.x);
                edge.line.setAttribute("y1", svgP.y);
            }
            if (edge.targetNode === selectedNode) {
                edge.line.setAttribute("x2", svgP.x);
                edge.line.setAttribute("y2", svgP.y);
            }
        });
    }
});

canva.addEventListener("mouseup", function() {
    selectedNode = null;
});

nodes.forEach(node => {
    node.circle.addEventListener("mousedown", function() {
        selectedNode = node;
    });
    node.text.style.userSelect = "none";
    node.text.style.pointerEvents = "none";
});
