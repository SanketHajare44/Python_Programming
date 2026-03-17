import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousClassifier(Datapath):
    Border = "-"*40
    
    #   Step 1 : Load the dataset from CSV file

    print(Border)
    print("Step 1 : Load the dataset from CSV file")
    print(Border)

    df = pd.read_csv(Datapath)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    #   Step 2 : Clean the dataset by removing empty rows

    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)        # if one cell is empty then removed it

    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    #   Step 3 : Separate independent and dependent variable

    print(Border)
    print("Step 3 : Separate independent and dependent variable")
    print(Border)

    X = df.drop(columns = ['Class'])                # 1st 'Class column removed and other 13 used'

    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.tolist())
    print("Output column : ")



def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()