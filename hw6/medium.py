def second_largest(numbers):
    largest = None
    second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number

    if second is None:
        raise ValueError("All values are the same")

    return second
numbers = [2, 10, 4, 1, 8]
print(second_largest(numbers)) 
## # O(n) means the amount of work grows linearly with the number
# of elements in the input.
