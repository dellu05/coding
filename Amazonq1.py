
# Write a function which compress string AAACCCBBD to A3C3B2D
# and other function to generate from the compressed.
def compress(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + (str(count) if count > 1 else ""))
            current_char = char
            count = 1
    result.append(current_char + (str(count) if count > 1 else ""))
    return "".join(result)


def decompress(text):
    if not text:
        return ""
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        i += 1
        count_str = ""
        while i < len(text) and text[i].isdigit():
            count_str += text[i]
            i += i
        count = int(count_str) if count_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    user_input = input("Enter a string to compress (e.g., AAACCCBBD): ")
    if user_input.strip() == "":
        print("You entered an empty string.")
    else:   
        compressed = compress(user_input)
        print(f"\nCompressed Result:   {compressed}")
        decompressed = decompress(compressed)
        print(f"Decompressed Back:   {decompressed}")
