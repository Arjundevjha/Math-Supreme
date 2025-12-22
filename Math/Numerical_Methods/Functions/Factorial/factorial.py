
def factorial(num):
    result = 1
    if num == 0:
        return 1
    else:
        for idx in range(1,num +1):
            result = idx*result 
    return result

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is: {factorial(num)}")