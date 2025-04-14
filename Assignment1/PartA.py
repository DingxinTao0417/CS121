import sys

def tokenize(Path) -> list:
    tokens = []

    # is_valid function accept a character to determine if
    # it's a valid for english or num char
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

def computeWordFrequencies(tokens: list) -> dict:
    freq = {}
    for token in tokens:
        if token not in freq:
            freq[token] = 1
        else:
            freq[token] += 1
    return freq

def print_frequencies(freq_map: dict) -> None:
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    for key,value in sorted_freq:
        print(key+' -> '+str(value))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Has to follow the format: python PartA.py <filepath>")

    path = sys.argv[1]
    tokens = tokenize(path)
    freq_map = computeWordFrequencies(tokens)
    print_frequencies(freq_map)