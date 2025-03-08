from datetime import datetime

def get_days_from_today(date: str = None) -> int | None:
    try:
        today = datetime.now()
        days_diff = today - datetime.strptime(date, "%Y-%m-%d")
        result = int(days_diff.days)
        return result
    except (ValueError, TypeError) as error:
        print(error)
        return None

#print(get_days_from_today())