# Best way to display Iris dataset on console

from sklearn.datasets import load_iris


def main():
    print("Iris classification case study")

    Dataset = load_iris()

    # Meta Data of Dataset
    print("Independent variables are : ")
    print(Dataset.feature_names)
    print("Length of Independent Variables : ",len(Dataset.feature_names))

    print("Dependent Variables are : ")
    print(Dataset.target_names)
    print("Length of dependent Variables : ",len(Dataset.target_names))

if __name__ == "__main__":
    main()
