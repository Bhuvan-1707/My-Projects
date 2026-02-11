Assignment Report\
![Amrita Logo](static/images/AmritaLogo.png)\
Bhuvan Rajasekar - CB.SC.U4AIE24209\
AIE-C\
Mathematics for Computing - 4 (22MAT230)

## MFC_Graphs
A small Flask web application that visualizes undirected graphs, generates random or manual graphs, computes graph matrices, and provides interactive SVG rendering with node dragging.

### ✨ Features
Generate random undirected graphs by specifying number of nodes and edges.

Enter manual edge lists (outgoing/incoming node pairs) to build custom graphs.

View interactive SVG graph visualization with draggable nodes in the browser.

Display key graph matrices: Incidence, Adjacency, Degree, and Laplacian.

Handles constraints like no self-loops or duplicate edges in random generation.

### 📁 Project Structure
```
MFC_Graphs/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/             # Static assets
│   ├── style.css       # Styling
│   ├── graph.js        # SVG graph rendering and interactivity
│   └── images/         # Graph images
│       └── graph.png
├── templates/          # HTML templates
│   └── index.html      # Main page for input and results
└── README.md           # Project documentation
```
### 🚀 Getting Started
Prerequisites

```
Python >= 3.10
pip
```

### Installation
```
git clone https://github.com/Bhuvan-1707/My-Projects.git
cd MFC_Graphs
```
```
pip install -r requirements.txt
```
Run the app
### Development (Flask built-in server):

```
python app.py
```
Then open a browser and go to:
http://127.0.0.1:5000/

### 👨‍💻 Usage
On the main page, choose Random Graph or Manual Graph.

For Random: Enter number of nodes and edges, then click Submit.

For Manual: Enter space-separated outgoing nodes (e.g., "1 2 3") and incoming nodes (e.g., "2 3 1"), then click Submit.

View the interactive SVG graph (drag nodes around) and computed matrices: Incidence, Adjacency, Degree, Laplacian.

Node numbers must be positive integers; manual lists must match in length.

### 📦 Dependencies
Main dependencies:

Flask – web framework.
NetworkX – graph generation and matrix computations.
Matplotlib – graph image generation.

### 🌐 Deployment
This app targets platforms that support server-side Python execution.

Typical steps:

Ensure the following files and folders are present on the server:
```
app.py

requirements.txt

templates/

static/ (including CSS, JS, images)
```
Install dependencies:

```
pip install -r requirements.txt
Run with: python app.py or use a WSGI server like Gunicorn for production.
```

Ensure the platform allows static file serving and JavaScript execution.