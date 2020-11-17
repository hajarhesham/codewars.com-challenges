def largest_pair_sum(numbers):
    n = len(numbers)
    for num in numbers:
        numbers.sort()
        max = numbers[n-1]
        maxtwo = numbers[n-2]
    return max + maxtwo
