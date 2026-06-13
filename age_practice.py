from datetime import date
born_year = int(input("What year were you born? "))
born_month = int(input("What month were you born? "))
born_day = int(input("What day were you born? "))

birth_date = date(born_year, born_month, born_day)

current_day = date.today()

not_pass_yet = (current_day.month, current_day.day) < (birth_date.month, birth_date.day)

calculate_age = current_day.year - birth_date.year - not_pass_yet

print(f"Your are currently {calculate_age} years old.")