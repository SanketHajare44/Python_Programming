import pandas as pd

def main():

    sobj = pd.Series([25000,27000,29000,30000], index=["PPA","LB","Python","React"])      #int64 -> 64 bit  # userdefine index gived as string
                                                                                            # also we can create using dictionary data type  like key value pair

    print(sobj)

    print(sobj["Python"])

if __name__ == "__main__":
    main()