# Linear Regression Based Salary Prediction

## Overview
This project builds a **Linear Regression model** to predict salaries based on **years of experience**, implemented using both a **Python script** and a **Jupyter Notebook**. It visualizes actual vs predicted results and evaluates model performance with key error metrics.

## Files
- **Linear_Regression.py**  
  Loads and preprocesses the dataset, splits it into training and testing sets, applies normalization, performs linear regression using the **pseudoinverse method**, predicts salaries, and computes performance metrics — **MAE**, **MSE**, **RMSE**, **MAPE**, and **R²**.  
  Generates and saves visualizations for model evaluation.

- **Analysis.ipynb**  
  Jupyter Notebook that provides detailed exploratory data analysis (EDA), including education-level effects, descriptive statistics, and additional visualizations to understand salary trends and regression behavior.

- **Scatter-Plot.jpg**  
  Scatter plot showing **predicted salary (X-axis)** vs **actual salary (Y-axis)**, along with the regression line.

- **Prediction-Plot.jpg**  
  Line plot comparing **actual vs predicted salaries** for each test instance.

## How to Run
1. **Install Python** (version 3.10 or above recommended).  
2. **Install required libraries:**
   ```bash
   pip install numpy pandas matplotlib
   ```
3. **Place the dataset** in the same directory as the script.  
4. **Run the main script:**
   ```bash
   python Linear_Regression.py
   ```
5. **Explore the notebook (optional):**
   ```bash
   jupyter notebook Analysis.ipynb
   ```

## Features
- Reads and preprocesses experience–salary data  
- Splits data into training and testing sets (80/20)  
- Applies normalization and regression via pseudoinverse  
- Evaluates model with multiple performance metrics:  
  - Mean Absolute Error (MAE)  
  - Mean Squared Error (MSE)  
  - Root Mean Squared Error (RMSE)  
  - Mean Absolute Percentage Error (MAPE)  
  - Coefficient of Determination (R²)  
- Generates and saves plots:  
  - Scatter plot with regression line  
  - Actual vs Predicted salary plot  

## Outputs
After running the scripts, the following visualizations are generated:
- **Scatter-Plot.jpg** – Predicted vs Actual salary with regression line  
- **Prediction-Plot.jpg** – Actual vs Predicted salaries per test instance  

## License
This project is intended **for educational purposes only**.
