# Function to find the largest among three numbers
def find_the_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    
    return largest

# usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest_no = find_the_largest(num1, num2, num3)
print(f"The largest of the three numbers is: {largest_no}")
