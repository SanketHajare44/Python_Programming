import pandas as pd

def main():
    Data = [11,21,51,101,111]

    print(Data)                 # prints the list

    sobj = pd.Series(Data)          # Data contains should homogenous

    print(sobj)                 # prints the series 

if __name__ == "__main__":
    main()