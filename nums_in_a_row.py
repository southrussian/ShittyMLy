def count_removed_numbers(sequence):
    result = 0
    current_number = None
    current_count = 0

    for number in sequence:
        if current_number is not None:
            if current_number == number:
                current_count += 1
            else:
                if current_count >= 3:
                    result += current_count
                current_number = number
                current_count = 1
        else:
            current_number = number
            current_count = 1

    # Check for the last subsequence
    if current_count >= 3:
        result += current_count

    return result

# Reading input
try:
    input_sequence = input().split()
    sequence = list(map(int, input_sequence))
    removed_count = count_removed_numbers(sequence)
    print(removed_count)
except ValueError:
    print("Invalid input")
