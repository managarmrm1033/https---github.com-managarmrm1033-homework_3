from datetime import datetime

def get_days_from_today(date):
     attemtps = 3
     while attemtps > 0:
          try:
               date = datetime.strptime(date, "%Y.%m.%d").date()
               day_today = datetime.today().date()
               differense_day = day_today - date # або day_today - date щоб виходило плюсове значення ,а не -90
               return differense_day
          except ValueError:
               print("Введіть парвильний формат данних (%Y.%m.%d або 2024.01.21)")
               date = input("Спробуйте будь ласка ще раз:)! ")
               attemtps -= 1
          return "Не вдалось ввести коректну дату"

sup = input("Введіть дату: ")
print(get_days_from_today(sup))