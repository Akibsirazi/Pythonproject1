def process_numbers(numbers):
    if len(numbers) != 10:
        raise ValueError("You must provide exactly 10 numbers.")

    largest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / len(numbers)

    return largest, average, smallest
print ("largest numbers:")
print("average numbers:")
print("smallest numbers:")




