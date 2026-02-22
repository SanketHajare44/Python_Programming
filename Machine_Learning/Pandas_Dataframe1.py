import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [23,26,25],
         "City" : ["Pune","Mumbai","Satara"]
    }

    dobj = pd.DataFrame(Data)                       # Dataframe is like 2D Array    (Dataframe is collection of series)

    print(dobj)

    print(dobj["City"])


if __name__ == "__main__":
    main()