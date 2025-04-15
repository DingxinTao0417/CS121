import sys

# tokenize(), param: Path - string, return: tokens - list
# Complexity: O(n), n here is the number of characters in the input file.
# tokenize function reads the input file line by line and processes every character
def tokenize(Path: str) -> list:
    tokens = []

    # is_valid(), param: c - string, return: boolean
    # Complexity: O(1)
    # is_valid function accept a character to determine if it's a valid for english or num char
    def is_valid(c: str) -> bool:
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') or c == '_'

    with open(Path, 'r', encoding='utf-8') as f:
        for line in f:
            token = ""
            for char in line:
                if is_valid(char):
                    token += char
                else:
                    if token:
                        tokens.append(token.lower())
                        token = ""
            if token:
                tokens.append(token.lower())

    return tokens

# computeWordFrequencies(), param: tokens - list, return: freq - dict
# Complexity: O(n), n here is the number of elements in tokens list.
# computeWordFrequencies function processes each element in tokens, put them into frequency dict.
# key is the word in tokens, value is the frequency of the word appeared in tokens list.
def computeWordFrequencies(tokens: list) -> dict:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq

# print_frequencies(), param: freq_map - dict, return: None
# Complexity: O(nlogn), n here is the number of keys in freq_map dictionary
# O(nlogn) is for python sorted function. Python sorted is Tim-Sort.
# Tim-Sort: Tim-Sort will split the array into sub arrays(runs) with a certain size
# For those runs, timsort uses insertion sort to sort the sub array，
# insertion sort in timsort time complexity is O(n)
# and then uses merge sort to combine those runs into a whole sorted array
# merge sort in timsort time complexity is O(nlogn), in total the timsort time complexity will be O(nlogn)
# It runs O(nlogn) for the best case. For worst case, it will be O(n).
# O(n) is for getting each key and value pair in sorted_freq map. n is the total number of keys in the map.
# Therefore, the overall time complexity will be O(nlogn) by Timsort.
# print_frequencies function prints every pair in freq_map to command line.
def print_frequencies(freq_map: dict) -> None:
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_freq:
        print(key+' -> '+str(value))

# main function, checks the number of arguments from command line, raises error if there's bad argument
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Has to follow the format: python PartA.py <filepath>")

    path = sys.argv[1]
    tokens = tokenize(path)
    freq_map = computeWordFrequencies(tokens)
    print_frequencies(freq_map)