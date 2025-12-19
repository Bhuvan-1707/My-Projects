# 📌 MFC_Clustering

**Clustering Web App**  
A Flask‑based interactive tool for generating synthetic datasets and exploring clustering results visually using Plotly.

---

## 🧠 Project Overview

This repository contains a web application that lets users:

✔ Generate synthetic 2D datasets with configurable parameters  
✔ Apply an online clustering algorithm (MATLAB‑style incremental update)  
✔ Choose between Uniform and Normal dataset types  
✔ Visualize data and clusters interactively in the browser via Plotly  
✔ Experiment with cluster counts and configurations  

This tool is ideal for learning clustering behavior and visual interpretation of unsupervised learning results.

---

## 🚀 Features

### 🔹 Dataset Generation
- Uniform and Normal synthetic data generation
- User‑configurable:
  - Number of clusters
  - Points per cluster
  - Cluster spread
  - Cluster variance

### 🔹 Clustering Algorithm
- Custom Python implementation inspired by MATLAB incremental centroid updates
- Evaluates cluster counts from `2` to `NCluster + 3`
- Chooses best cluster count based on minimum distortion (J‑score)

### 🔹 Interactive Visualization
- Flask‑based web UI
- Plotly for interactive plots (pan, zoom, hover)
- Color‑coded cluster visualization

---

## 📁 Project Structure

```
MFC_Clustering/
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/Bhuvan-1707/My-Projects.git
cd My-Projects/MFC_Clustering
python3 -m venv venv
source venv/bin/activate
pip install plotly flask numpy
```

---

## ▶️ Running the App

```bash
python app.py
```

Open browser:  
`http://localhost:5000`

---

## 🧪 Usage

1. Select dataset type (Uniform / Normal)
2. Enter cluster and data parameters
3. Click **Generate**
4. Click **Classify** to view clustering result

---

## 🧩 Algorithm Insight

The clustering logic closely matches MATLAB code with online centroid updates:

```matlab
C(tag(j),:) = (C(tag(j),:) + X(j,:))/2;
```

This ensures behavior consistency between MATLAB and Python.

---

## 📊 Outputs

- Interactive scatter plots
- Cluster‑wise coloring
- Display of best cluster count and least J‑score

---

## 📜 License

MIT License

---

## 👤 Author

**Bhuvan Rajasekar**  
GitHub: https://github.com/Bhuvan-1707
