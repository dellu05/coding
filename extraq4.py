""" Given a set of N lines of English language, each comprises only of a-z
and A-Z. For each line, find the alphabets which have highest frequency
of occurance and print them (with capital letters first then small letters in
increasing order. """ 

def find_highest_frequency_letters(line):
    cleaned_line = [char for char in line if char.isalpha()]
    if not cleaned_line:
        return ""
    frequencies = {}
    for char in cleaned_line:
        frequencies[char] = frequencies.get(char, 0) + 1
    max_freq = max(frequencies.values())
    most_frequent_chars = [char for char, freq in frequencies.items() if freq == max_freq]
    most_frequent_chars.sort()
    return "".join(most_frequent_chars)
print("\n--- 2. Highest Frequency Alphabets ---")
try:
    n = int(input("Enter the number of lines (N): "))
    print(f"Enter your {n} lines:")
    lines = [input(f"Line {i+1}: ") for i in range(n)]
    print("\n--- Output Results ---")
    for i, line in enumerate(lines):
        result = find_highest_frequency_letters(line)
        print(f"Line {i+1} Highest Frequency: {result}")
except ValueError:
    print("Please enter a valid integer for N.")
