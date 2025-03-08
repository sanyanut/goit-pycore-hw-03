from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # today = datetime(year=2025, month=12, day=31).date()  to check upcoming birthday for the next year
    today = datetime.now().date()
    upcoming_birthdays_list = []

    for user in users:
        birthday = user['birthday']
        formatted_birthday = datetime.strptime(birthday, "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, formatted_birthday.month, formatted_birthday.day).date()

        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, formatted_birthday.month, formatted_birthday.day).date()

        days_diff = birthday_this_year - today

        if days_diff.days <= 7 and birthday_this_year.weekday() <= 4:
            upcoming_birthdays_list.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

        elif days_diff.days <= 7 and birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
            upcoming_birthdays_list.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

        elif days_diff.days <= 7 and birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)
            upcoming_birthdays_list.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays_list

users = [
    {"name": "John Doe", "birthday": "1985.03.15"},
    {"name": "Coco Loco", "birthday": "1990.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {"name": "Test Rambo", "birthday": "1990.01.04"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
