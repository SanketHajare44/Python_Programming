# used matplotlib and seaborn for visulization

import matplotlib.pyplot as plt 
import seaborn as sns

def main():

    # genrly used for Detecting Outliers
    sns.boxplot(x=[10,20,30,110])

    plt.show()

if __name__ == "__main__":
    main()

