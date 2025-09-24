

# Task 1  ODD or Even numbers
number_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize an empty list to store odd numbers
odd_numbers = []
# Initialize an empty list to store even numbers
even_numbers = []

# Iterate through each number in the number_list
for i in number_list:
    # Check if the number is divisible by 2 with no remainder
    if i % 2 == 0:
        # If it is, the number is even, so append it to the even_numbers list
        even_numbers.append(i)
    else:
        # If it's not divisible by 2 with no remainder, the number is odd
        # Append it to the odd_numbers list
        odd_numbers.append(i)

# Print the list of odd numbers
print("ODD numbers :",odd_numbers)
# Print the list of even numbers
print("Even numbers :",even_numbers)

print("-----------------------------------")


# Task-2 Prime Number

task2 = [10, 501, 22, 37, 100, 999, 87, 351]
for number in task2:
    # Rule: Prime numbers must be greater than 1.
    # If the number is 1 or less, it's not prime.
    if number <= 1:
        print("not the prime number: ", number)
        continue # Skip to the next number in the list

    # Assume the number is prime initially.
    # We will try to find a divisor to prove it's not prime.
    is_prime = True

    # Iterate from 2 up to (but not including) the number itself.
    # This loop checks for potential divisors.
    for i in range(2, number):
        # If the number is perfectly divisible by 'i' (i.e., no remainder)...
        if number % i == 0:
            # then it has a divisor other than 1 and itself, so it's not prime.
            is_prime = False
            break # No need to check further divisors for this number, exit the inner loop.


    # If 'is_prime' is still True, it means no divisors were found.
    if is_prime:
        print("It is the prime number", number)
    else:
        # If 'is_prime' became False, it means a divisor was found.
        print("not the prime number", number)

print("-----------------------------------")

# Task-3 Finding Happy Number

number_list = [10, 501, 22, 37, 100, 999, 87, 351]

def is_happy_number(n):
    """
    Checks if a given number is a happy number.

    A happy number is a number which, when repeatedly replaced by the sum of the
    square of its digits, eventually reaches 1. If the process results in an
    endless cycle of numbers that do not include 1, the number is unhappy.

    Args:
        n: An integer to check.
    """
    # Initialize a list to keep track of numbers encountered during the process.
    # This is crucial to detect cycles (unhappy numbers).
    visited = []
    # Initialize a flag to control the loop. 'ret' stands for 'return' or 'repeat'.
    ret = True
    # Continue the process as long as 'ret' is True.
    while ret:
        # Initialize a variable to store the sum of the squares of the digits.
        digit_sum = 0
        # Iterate through each digit of the current number 'n'.
        for i in str(n):
            # Convert the digit character to an integer, square it.
            square = int(i) ** 2
            # Add the squared digit to the sum.
            digit_sum += square

        # Check if the sum of squares is 1. If it is, the number is happy.
        if digit_sum == 1:
            print(n, "is a happy number")
            ret = False # Set ret to False to exit the loop.

        # Check if the current sum of squares has been encountered before.
        # If it has, it means we've entered a cycle, and the number is unhappy.
        if digit_sum in visited:
            print(n, "is not a happy number") # Print that the original number (or intermediate) is unhappy
            ret = False # Set ret to False to exit the loop.

        # Add the current sum of squares to the list of visited numbers.
        visited.append(digit_sum)
        # Update 'n' to be the calculated sum of squares for the next iteration.
        n = digit_sum

# Iterate through each number in the predefined list.
for j in number_list:
    # Call the is_happy_number function for each number to check if it's happy or not.
    is_happy_number(j)

print("-----------------------------------")

# Task-4 find the first and last number
number = 12345

# Use an f-string to format the output.
# To get the first number, we first convert 'number' to a string using str(number).
# Then we use string indexing [0] to access the first character.
# To get the last number, we again convert 'number' to a string.
# We use negative indexing [-1] to access the last character, which is the last digit.
print(f" First number: {str(number)[0]}, Last number: {str(number)[-1]} ")

print("-----------------------------------")

# Task-5 find all the ways to make use of 10 rupees using 1,2,5,10 rupee coins
total = 10
ways = []

# Try all possible numbers of 10-rupee coins
for c10 in range(0, 2):   # 0 or 1 ten-rupee coin
    for c5 in range(0, 3):   # 0, 1, or 2 five-rupee coins
        for c2 in range(0, 6):  # 0 to 5 two-rupee coins
            for c1 in range(0, 11):  # 0 to 10 one-rupee coins
                # Check if the total adds up to 10
                if 10*c10 + 5*c5 + 2*c2 + c1 == total:
                    ways.append((c10, c5, c2, c1))

print("Total ways:", len(ways))


print("-----------------------------------")
# Task 6 Given #list Find the duplicate numbers

list1 = [1, 2, 3, 4, 5,10]
list2 = [3, 5, 7, 9,10]
list3 = [0, 2, 3, 5, 8,10]

# Convert lists to sets
set1,set2,set3 = set(list1), set(list2), set(list3)

# Find common duplicates
duplicates = set1 & set2 & set3
print("Duplicates in all three lists:", duplicates)


print("-----------------------------------")

# Task 7 Finding the first non-repeating number in a list

# numbers is a list of integers.
numbers = [4, 5, 1, 2, 3, 2, 0, 4, 5]

# Step 1: Count frequencies
freq = {}
# Loop through each number in the list to count its occurrences.
for num in numbers:
    # The .get() method returns the value for the specified key (num).
    # If the key does not exist, it returns the default value (0).
    # We then add 1 to this value, effectively counting each number.
    freq[num] = freq.get(num, 0) + 1

# Step 2: Find the first non-repeated number
# Iterate through the original list again to maintain the order.
for num in numbers:
    # Check if the frequency of the current number is exactly 1.
    if freq[num] == 1:
        # If the count is 1, it's a non-repeated number.
        # Print it and exit the loop immediately since we've found the first one.
        print(num, "is the first non-repeated number")
        break
print("-----------------------------------")


# Task 8 Finding the minimum value in a rotated sorted array

# The input array. It's a sorted array that has been rotated.
numbers = [6, 7, 1, 2, 3, 4, 5]

# Initialize pointers for the search range.
# 'lowest' starts at the beginning of the array.
# 'highest' starts at the end of the array.
lowest, highest = 0, len(numbers)-1

# Start a loop that continues as long as the search range is valid (i.e., 'lowest' is less than 'highest').
while lowest < highest:
    # Calculate the middle index of the current search range.
    # The '//2' ensures integer division.
    mid  = (lowest+highest)//2

    # Check if the middle element is less than the highest element.
    # This means the right half of the array is sorted and the pivot (minimum value)
    # must be in the left half, including the 'mid' point.
    if numbers[mid] < numbers[highest]:
        # Narrow the search range by moving the 'highest' pointer to 'mid'.
        highest = mid

    # If the middle element is greater than the highest element,
    # the pivot must be in the right half of the array.
    elif numbers[mid] > numbers[highest]:
        # Narrow the search range by moving the 'lowest' pointer to 'mid + 1'.
        lowest = mid + 1

# Once the loop ends, 'lowest' and 'highest' will both point to the index
# of the minimum value.
print(f" the min value is {numbers[lowest]}")


print("-----------------------------------")

# Task 9 given the pyhton list[10,20,30,9] and a value is 59 and find the triplet in the list whose sum is equal to given value
numbers = [10, 20, 30, 9]
target_sum = 59

n = len(numbers)
found = False

# The first loop picks the first element of the triplet.
for i in range(n):
    # The second loop picks the second element. It starts from `i+1`
    # to avoid using the same element twice and to prevent duplicate triplets.
    for j in range(i + 1, n):
        # The third loop picks the third element. It starts from `j+1`
        # to ensure the three elements are distinct.
        for k in range(j + 1, n):
            # Check if the sum of the three elements equals the target sum.
            if numbers[i] + numbers[j] + numbers[k] == target_sum:
                # If the sum matches, print the triplet.
                print(f"Triplet found: ({numbers[i]}, {numbers[j]}, {numbers[k]})")
                # Set the flag to True to indicate that a triplet has been found.
                found = True
                # Break out of the innermost loop.
                break




print("-----------------------------------")
# task 10 given pyhton list [4,2,-3,1,6] write the program to find isf there is a sub-list with sum equal to zero
numbers =  [4, 2, -3, 1, 6]
# Get the total number of elements in the list.
len_numbers = len(numbers)

# The outer loop iterates through each element of the list.
# 'i' represents the starting index of a potential sub-list.
for i in range(len_numbers):
    # Initialize 'current_sum' to 0 at the beginning of each new sub-list.
    current_sum = 0
    # The inner loop iterates from the current starting index 'i' to the end of the list.
    # 'j' represents the ending index of the potential sub-list.
    for j in range(i, len_numbers):
        # Add the current number to the 'current_sum' to find the sum of the sub-list.
        current_sum += numbers[j]
        # Check if the 'current_sum' is equal to 0.
        if current_sum == 0:
            # If the sum is 0, a sub-list with a sum of 0 has been found.
            # Print the sub-list using slicing from the starting index 'i' to the ending index 'j'.
            print("Sub-list with sum 0 found:", numbers[i:j + 1])
            # Break out of the inner loop to find the next possible sub-list starting at a new 'i'.
            break



