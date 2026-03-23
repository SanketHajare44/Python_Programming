# Bagging -> DecisionClassifier is used as base model

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

#-----------------------------------------------------------------------
#   Step 1 : Load the dataset
#-----------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("shape of dataset : ",df.shape)
print("First 5 records : ",df.head())

#-----------------------------------------------------------------------
#   Step 2 : Seprate features and labels
#-----------------------------------------------------------------------

X = df.drop("target",axis=1)        # Independent

Y = df["target"]                    # Dependent

#-----------------------------------------------------------------------
#   Step 3 : Split dataset for training and testing
#-----------------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#-----------------------------------------------------------------------
#   Step 4 : Create base model
#-----------------------------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

#-----------------------------------------------------------------------
#   Step 5 : Create Bagging model
#-----------------------------------------------------------------------

bagging_model = BaggingClassifier(
                                    estimator=base_model,
                                    n_estimators=10,
                                    random_state=42
                                 )

#-----------------------------------------------------------------------
#   Step 6 : Train bagging model
#-----------------------------------------------------------------------

bagging_model.fit(X_train,Y_train)

#-----------------------------------------------------------------------
#   Step 7 : Test Bagging model
#-----------------------------------------------------------------------

Y_Pred = bagging_model.predict(X_test)

#-----------------------------------------------------------------------
#   Step 8 : Evaluate Bagging model
#-----------------------------------------------------------------------

print("Bagging Accuray : ",accuracy_score(Y_test,Y_Pred)*100)

print("Confusion Matrix : ")
print(confusion_matrix(Y_test,Y_Pred))