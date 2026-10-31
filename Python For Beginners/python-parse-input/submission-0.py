from typing import List

def read_integers() -> List[int]:
    num_int = []
    num_string = input().split(",")
    for i in num_string:
        num_int.append(int(i))
    return num_int
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
