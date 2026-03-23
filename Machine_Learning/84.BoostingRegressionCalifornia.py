# Boosting -> Regression

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,r2_score

#-----------------------------------------------------------------------
#   Step 1 : Load the dataset
#-----------------------------------------------------------------------

df = pd.read_csv("california_housing.csv")

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
#   Step 4 : Create gradient boosting model
#-----------------------------------------------------------------------

boost_model = GradientBoostingRegressor(random_state=42,
                                          n_estimators=100,
                                          learning_rate=0.1,
                                          max_depth=3
                                       )

#-----------------------------------------------------------------------
#   Step 5 : Train boosting model
#-----------------------------------------------------------------------

boost_model.fit(X_train,Y_train)

#-----------------------------------------------------------------------
#   Step 6 : Test boosting model
#-----------------------------------------------------------------------

Y_Pred = boost_model.predict(X_test)

#-----------------------------------------------------------------------
#   Step 7 : Evaluate boosting model
#-----------------------------------------------------------------------

print("Mean sqared error : ",mean_squared_error(Y_test,Y_Pred))

print("r2 : ",r2_score(Y_test,Y_Pred))