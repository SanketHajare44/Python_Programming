import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

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

    #   Step 4 : Split the dataset for training and testing

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

    # Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()

    # Independent variable scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature is done")

    #   Step 6 : Explore the multiple values of k 
    #   Hyper parameter tunning (k)

    print(Border)
    print("Step 6 : Explore the multiple values of k ")
    print(Border)


    accuracy_scores = []
    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        
        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)
    
    print(Border)
    print("Accuracy report of all k values from 1 to 20")

    for value in accuracy_scores:
        print(value)

    print(Border)
    

def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()