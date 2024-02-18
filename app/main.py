import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

specialCharactersToValueMap = {}

def match_literals(input_line, literal):
    if len(literal)==1:
        return literal in input_line
    literal_values = specialCharactersToValueMap.get(literal, [])
    for c in literal_values:
        if c in input_line:
            return True
    return False


def match_pattern(input_line, pattern):

    return match_literals(input_line, pattern)
    # else:
    #     raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    specialCharactersToValueMap["\\d"] = [str(i) for i in range(10)]

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
