from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    name_list = []
    for names in age_dict:
        name_list.append(names)
    return name_list
    pass

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    age_list = []
    for names, ages in age_dict.items():
        age_list.append(ages)
    return age_list
    pass

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
