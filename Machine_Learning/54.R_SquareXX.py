from sklearn.metrics import r2_score
 
def main():
    Y_actual = [3,4,2,4,5]              # Y
    Y_Predicted = [3,4,2,4,5] # Yp

    r2 = r2_score(Y_actual,Y_Predicted)

    print("Actual values : Y ",Y_actual)
    print("Predicted values : Yp ",Y_Predicted)
    print("R square value : ",r2)                   # 1.0  accuracy 100%        


if __name__ == "__main__":
    main()