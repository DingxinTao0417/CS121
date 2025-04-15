import sys
import PartA as PA

# find_common_tokens(), param: file1, file2(path of these two files) - string, return: length of common tokens integer
# Complexity: O(n+m), n and m are the number of characters in each file, tokenize function reads and tokenizes file linearly
# find_common_tokens function uses set intersection of two token lists, and count the number of common token in two lists.
def find_common_tokens(file1, file2):
    tokens1 = set(PA.tokenize(file1))
    tokens2 = set(PA.tokenize(file2))
    common_tokens = tokens1 & tokens2
    return len(common_tokens)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("There must be 2 text arguments in the input")

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    common_tokens = find_common_tokens(file1, file2)
    print(common_tokens)