def maximum_difference(numbers):
    if len(numbers) < 2:
        raise ValueError("Array must contain at least two numbers")

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers[1:]:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return largest - smallest



numbers = [2, 10, 4, 1, 8]
print(maximum_difference(numbers)) 
## # O(n) means the amount of work grows linearly with the number
# of elements in the input.