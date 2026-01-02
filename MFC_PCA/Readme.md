# PCA Visualization App

## Project Overview
This project is a Flask web application for visualizing Principal Component Analysis (PCA) on synthetic 2D datasets. Users generate elliptical, rectangular, or linear data via an HTML form in `index.html`, then animate PCA optimization showing principal axis alignment and squared error reduction.


## Key Features
- Generates datasets:
  - Ellipse: mean foci, spread, tilt.
  - Rectangle: start vertex, length/breadth, tilt.
  - Line: slope, intercept.
- Plots data with Plotly for static visualization.
- Animates PCA: centers data, computes covariance eigenvectors, rotates axis from 0 to optimal angle over 11 frames with error display.
- Session storage for data and plots between generate/animate steps.

## Setup Instructions
1. Install dependencies:
```
pip install flask flask-session plotly numpy
```
2. Create a `templates` folder and place `index.html` and `home.html` inside it.
3. Run the app:

```
python app.py
Use `debug=True` for development.
```
## Usage
1. Open `http://localhost:5000/home` (or `/` redirects there).
2. Select dataset type (Ellipse, Rectangle, Linear) and enter parameters via tabs.
3. Submit **Generate** to plot the data.
4. Click **Animate** to run PCA animation with play buttons (Slow/Medium/Fast).

## File Structure
- `app.py`: Main Flask application with data generation and PCA logic.
- `index.html`: Interactive form and results page.
- `templates/home.html`: Entry page (not attached; simple redirect or form).

## Data Generation Details
- **Ellipse**: Rotated Gaussian cluster.
- **Rectangle**: Uniform distribution in rotated box.
- **Line**: Uniform x with linear y.

## PCA Animation
Centers data, finds optimal eigenvector, animates rotation minimizing squared projection error. 11 frames, customizable speed.

## Technologies
- Backend: Flask, NumPy.
- Frontend: Plotly.js, HTML/JS tabs.
- Storage: Filesystem sessions.