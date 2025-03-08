import re


def normalize_phone(num: str) -> str | None:
    pre_normalize = re.sub(r'[^0-9+]', '', num)
    if re.search(r'^\+', pre_normalize):
        return pre_normalize
    elif re.search(r'^380', pre_normalize):
        return f'+{pre_normalize}'
    else:
        return f'+38{pre_normalize}'

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#Нормалізовані номери телефонів для SMS-розсилки:
# ['+380671234567', '+380952345678', '+380441234567',
# '+380501234567', '+380501233234', '+380503451234',
# '+380508889900', '+380501112222', '+380501112211']
