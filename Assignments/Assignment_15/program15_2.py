# Write a lambda function using filter() which accepts list of numbers and returns a list of even numbers

CheckEven = lambda no : (no %2 == 0)

def filterX(task, elements):
    results = list()

    for i in elements:
        if(i%2 == 0):
            results.append(i)
    
    return results

def main():
    data = [1,2,3,4,5,6,7,8,9]
    result = list()
    result =list(filterX(CheckEven,data))

    print(result)

if __name__ == "__main__":
    main()