from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    length = len(my_list)
    for i in my_list:
        if len(my_list) == 3:
            return my_list
        elif length > 4:
            length -= 1
        else:
            return my_list[i:]

    pass


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
