from datetime import datetime
def get_days_from_today(date):
    given_date = datetime.strptime(date_input, '%Y-%m-%d')
    date = datetime.date(given_date)
    today = datetime.today().date()
    print(date)
    print(today)
    delta_days = (today - date).days
    print(delta_days)
    return delta_days
    


    
# Приклад використання функції
date_input = input('Введіть дату в форматі рік-місяць-день: ')
try:
  if date_input : 
   print(f'Кількість днів від {date_input} до сьогодні: {get_days_from_today(date_input)}')
  else:
   print("Невірний формат") 
except Exception:
    print(f"Вибачте стадась помилка - невірний формат: {date_input}")