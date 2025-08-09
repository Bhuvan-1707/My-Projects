import numpy as np
import pandas as pd

def main():
    df = pd.read_csv("/home/bhuvan1707/Desktop/Prediction-LinearReg-PseudoInv/Predicting_Salary_Based_on_Experience_using_LR_PINV/Linear_Regression_Salary_Dataset.csv")
    # Let us take Y and X variables for Linear Regression
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

    # Split for training and testing
    x_test = x[(len(x)*4)//5:]
    x = x[0:(len(x)*4)//5]
    Y_test = Y[(len(Y)*4)//5:]
    Y = Y[0:(len(Y)*4)//5]

    # Numpy Arrays
    x = x.to_numpy()
    Y = Y.to_numpy()
    x = np.reshape(x,(len(x),1))
    Y = np.reshape(Y,(len(Y),1))

    # Scaling the Train dataset
    x,xmin,xmax = scale(x)

    # Made the X and Y vectors in the shape of n*1
    z = np.ones(x.shape)
    X = np.concatenate((x,z),1)

    # Now the regression formulation
    w = np.linalg.pinv(X)@Y

    # Now we have obtained weights for prediction Individual testing
    n=5
    print((x_test.iloc[n]-xmin)/(xmax-xmin),Y_test.iloc[n])
    print(((x_test.iloc[n]-xmin)/(xmax-xmin))*w[0] + w[1])






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

main()