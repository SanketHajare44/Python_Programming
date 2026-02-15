# Steps for Machine Learning Application

# Step 1 : Data Gathering or collection
# step 2 : Data Analysis (coding starts from here)
# step 3 : Data cleaning
# step 4 : Model selection
# step 5 : Model training
# step 6 : Model testing / Evaluation
# step 7 : Model Improvement (eg. radio hyper parameter tuning)
# step 8 : Prediction / Deployment

import sklearn

def main():
    print("Ball classification case study")

    # Data Gathering

    Fetures =[[35,"Rough"],[47,"Rough"],[90, "Smooth"], [48,"Rough"], [90, "Smooth"],[35,"Rough"],[92, "Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96, "Smooth"],[43,"Rough"],[110, "Smooth"],[35,"Rough"],[95,"Smooth"]] 
    Labels = ["Tennis",    "Tennis",        "Cricket",      "Tennis",       "Cricket",      "Tennis",   "Cricket",  "Tennis",   "Tennis",    "Tennis",      "Cricket",    "Tennis",       "Cricket",   "Tennis",    "Cricket"]

if __name__ == "__main__":
    main()

# Dataset size 15