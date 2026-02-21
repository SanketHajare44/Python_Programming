# used matplotlib and seaborn for visulization

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

def main():

    # Feature co-relation show karnya karta use kela jata
    dobj = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6], "C" : [7,8,9]})
    
    print(dobj)

    sns.heatmap(dobj.corr(), annot=True)

    plt.show()

if __name__ == "__main__":
    main()

