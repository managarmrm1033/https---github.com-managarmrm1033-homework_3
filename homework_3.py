from datetime import datetime

def get_days_from_today(date):
     while True:
          try:
               if isinstance(date, str):
                    date = datetime.strptime(date, "%Y.%m.%d").date()

               day_today = datetime.today().date()
               differense_day = date - day_today # або day_today - date щоб виходило плюсове значення ,а не -90
               return differense_day
          except TypeError:
               datetime_object = datetime.strptime(date, "%Y.%m.%d")
          except ValueError:
               print("Введіть парвильний формат данних (%Y.%m.%d або 2024.01.21)")
               date = input("Спробуйте будь ласка ще раз:)! ")
sup = input("Введіть дату: ")
print(get_days_from_today(sup))