
def word_count(contents: str) -> int:
    words = contents.split()
    return len(words)

def char_count(contents: str):
    chars = {}
    contents_lowered = contents.lower()

    for char in contents_lowered:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def print_char_count(chars: dict) -> None:
    for char in chars:
        if char.isalpha():
            print(f"The '{char}' is was found {chars[char]} times")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    chars = char_count(file_contents)
    #print(chars)
    print_char_count(chars)

main()
