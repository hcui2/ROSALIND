import sys

def pattern_count(text: str, pattern: str) -> int:
    count = 0
    k = len(pattern)
    for i in range(len(text) - len(pattern)):
        if text[i: i+ k] == pattern:
            count += 1
    return count


if __name__ == '__main__':
    test_file = sys.argv[1]
    with open(test_file) as f:
        text = next(f).strip()
        pattern = next(f).strip()

        count = pattern_count(text, pattern)
        print(count)
