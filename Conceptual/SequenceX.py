Value1 = [10,20,30,40,10]   # list   -   Diplicate
print(Value1[0])            # 10
Value1[2] = 35
print(Value1[2])            # 35


Value2 = (10,20,30,40,10)   # tuple  -  Diplicate
print(Value2[0])            # 10
Value2[2] = 35              # Error
print(Value2[2])            # 30


Value3 = {10,20,30,40,10}   # set    -  No Diplicate
print(Value3[0])            # Error