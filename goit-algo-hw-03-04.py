from datetime import datetime, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.03.10"},
    {"name": "Jane Smith", "birthday": "1990-03-15"},
    {"name": "Jane Smith1", "birthday": "1990-03-12"}
]
def get_upcoming_birthdays(users, days=7):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], "%Y-%m-%d").date()
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if 0 <= (birthday_this_year - today).days <= days:
                congratulation_date_str = birthday_this_year.strftime('%Y-%m-%d')
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date_str
                })
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')
    return upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


