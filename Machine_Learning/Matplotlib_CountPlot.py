# used matplotlib and seaborn for visulization

import matplotlib.pyplot as plt 
import seaborn as sns

def main():

    # catagorical data
    sns.countplot(x=["A","B","A","A","B","A","C"])

    plt.show()

if __name__ == "__main__":
    main()


# if data contiguse(numeric) -> go for histoplot
# if data catogrial(strings) -> go for countplot()
