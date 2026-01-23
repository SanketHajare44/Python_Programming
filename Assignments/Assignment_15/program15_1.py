# Write a lambda function using map() which accepts list of numbers and returns a list of square of each number

Square = lambda no : no*no

def mapX(task,elements):
    results = list()
    for i in elements:
        Ans = task(i)
        results.append(Ans)
    return results

def main():
    data = [1,2,3,4,5,6,7,8,9]
    result = list()
    result =list(mapX(Square,data))

    print(result)

if __name__ == "__main__":
    main()