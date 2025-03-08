from random import sample
from typing import List

def get_numbers_ticket(min: int = None, max: int = None, quantity: int = None) -> List[int]:
    for arg in (min, max, quantity):
        if isinstance(arg, bool):
            print('\'bool\' object cannot be interpreted as integer')
            return []
    try:
        random_list = sample(range(min, max), quantity)
        sorted_list = sorted(random_list)
        return sorted_list
    except (ValueError, TypeError) as error:
        print(error)
        return []

#print(get_numbers_ticket(1,49,6))