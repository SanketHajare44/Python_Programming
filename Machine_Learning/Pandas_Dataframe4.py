# Data spliting

import pandas as pd

def main():
    Data = {
        "Name" : ["Sagar","Amit","Pooja"],
        "Age" : [23,26,25],
         "City" : ["Pune","Mumbai","Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj.loc[1])          # loc() -> fetch specific row

# Output :

# Name      Amit
# Age         26
# City    Mumbai
# Name: 1, dtype: object


if __name__ == "__main__":
    main()