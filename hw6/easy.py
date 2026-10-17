
def array_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [1, 2, 3, 4, 5]
print(array_sum(numbers))
# # O(n) means the amount of work grows linearly with the number
# of elements in the input.
