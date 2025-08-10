import numpy as np
import pandas as pd

def main():
    df = pd.read_csv("Linear_Regression_Salary_Dataset.csv")
    # Let us take Y and X variables for Linear Regression
    # For reproducible results
    df = df.sample(frac=1).reset_index(drop=True)
    x = df['Years of Experience']
    Y = df['Salary']

    # Check missing value => No missing values
    To_Estimate=[]
    while(check(Y)==False or False==check(x)):
        locate(x,Y)
        clean(x,Y)
        print("cleaning")
    else:
        print("cleaned")

    # Split for training and testing - 80/20 Train Test Split
    split = 80
    x_test = x[(len(x)*split)//100:]
    x = x[0:(len(x)*split)//100]
    Y_test = Y[(len(Y)*split)//100:]
    Y = Y[0:(len(Y)*split)//100]

    # Numpy Arrays
    x = x.to_numpy()
    Y = Y.to_numpy()
    x = np.reshape(x,(len(x),1))
    Y = np.reshape(Y,(len(Y),1))
    x_test = x_test.to_numpy()
    x_test = np.reshape(x_test,(len(x_test),1))
    Y_test = Y_test.to_numpy()
    Y_test = np.reshape(Y_test,(len(Y_test),1))

    # Scaling the Train dataset
    x,xmin,xmax = scale(x)
    
    # Normalizing test
    x_test = (x_test - xmin)/(xmax - xmin)
    
    # Made the X and Y vectors in the shape of n*1
    z = np.ones(x.shape)
    X = np.concatenate((x,z),1)

    # Now the regression formulation
    w = np.linalg.pinv(X)@Y

    z_test = np.ones(x_test.shape)
    X_test = np.concatenate((x_test,z_test),1)

    # Prediction
    Y_Pred = X_test@w
    
    # Accuracy Prediction with tolerance 50% Error
    Tol = 0.5
    accuracy = accuracy_finder(Y_Pred,Y_test,Tol)
    print("Accuracy of ",accuracy,"/",len(Y_test),"for",Tol,"% error\n =>",(accuracy*100)/len(Y_test), "\nin split of",split,"/ 100")

    metrics(Y_test,Y_Pred)

def scale(x):
    minim = np.min(x)
    maxim = np.max(x)
    return (x-minim)/(maxim-minim),  minim, maxim

def check(Y):
    if np.isnan(Y).any() or np.isinf(Y).any():
        print("Found NaN or Inf in data!")
        return False
    return True

def locate(x,Y):
    for i in range(len(Y)):
        if(np.isnan(Y[i])):
            print("isnan :",i)
            print(Y[i],x[i])
    print()
    for i in range(len(x)):
        if(np.isnan(x[i])):
            print("isnan :",i)
            print(x[i],Y[i])

def clean(x,Y):
    todrop=[]
    for i in range(len(Y)):
        if(np.isnan(Y.iloc[i])):
            todrop.append(i)
    x = x.drop(todrop,inplace=True)
    Y = Y.drop(todrop,inplace=True)

def accuracy_finder(Pred,Test,Tol):
    return np.sum((abs(Pred-Test)/(Test))<Tol)

def metrics(Y_test,Y_Pred):
    mae = np.sum(abs(Y_Pred-Y_test))/len(Y_test)
    print("MAE = ",mae)
    mse = np.sum((Y_Pred-Y_test)**2)/len(Y_test)
    print("MSE = ",mse)
    rmse = np.sqrt(np.sum((Y_Pred-Y_test)**2)/len(Y_test))
    print("RMSE = ",rmse)
    mape = 100*np.sum(abs(Y_Pred-Y_test)/Y_test)/len(Y_test)
    print("MAPE = ",mape)
    ssr = np.sum((Y_Pred-Y_test)**2)
    sst = np.sum((Y_test - np.mean(Y_test))**2)
    rsquared = 1-(ssr/sst)
    print("R^2 = ",rsquared)

# def plot()
main()