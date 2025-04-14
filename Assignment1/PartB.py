import sys
import PartA as PA

def fine_common_tokens(file1, file2):
    tokens1 = set(PA.tokenize(file1))
    tokens2 = set(PA.tokenize(file2))
    common_tokens = tokens1 & tokens2
    return len(common_tokens)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("There must be 2 text arguments in the input")

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    common_tokens = fine_common_tokens(file1, file2)
    print(common_tokens)