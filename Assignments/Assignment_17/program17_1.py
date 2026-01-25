''' Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
    for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
    parameters as number and perform the operation. Write on python program which call all the 
    functions from Arithmetic module by accepting the parameters from user.'''

import Arithmetic

def main():

    Ret = 0

    Ret = Arithmetic.Add(10,5)
    print(Ret)

    Ret = Arithmetic.Sub(10,5)
    print(Ret)

    Ret = Arithmetic.Multi(10,5)
    print(Ret)

    Ret = Arithmetic.Div(10,5)
    print(Ret)



if __name__ == "__main__":
        main()