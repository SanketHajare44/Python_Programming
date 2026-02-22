# using matplotlib and seaborn for visulization

import matplotlib.pyplot as plt 
import seaborn as sns

def main():

    # contigeous value
    sns.histplot(data=[10,20,30,20,20,20,30,40])

    plt.show()

if __name__ == "__main__":
    main()