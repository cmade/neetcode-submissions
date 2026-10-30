from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = 1
    char = {}
    for key in word:
        if key not in char:
            char[key] = count
        else:
            char[key] += count
    return char
    pass




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

