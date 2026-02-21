import pandas as pd

def main():

    # Data contains should homogenous
    sobj = pd.Series([11,21,51,101,111])        #int64 -> 64 bit

    print(sobj)                 # prints the series  

if __name__ == "__main__":
    main()