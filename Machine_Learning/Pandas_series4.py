import pandas as pd

def main():

    sobj = pd.Series([11.0,21.0,51.0,101.0,111.0], index=[5,6,7,8,9])      #float64 -> 64 bit  # userdefine indexing

    print(sobj)

    print(sobj[7])  # o/p 51.0

if __name__ == "__main__":
    main()