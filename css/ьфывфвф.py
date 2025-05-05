age = int(input("Введите возраст: "))

if 0 <= age <= 120:
  age_prots = age % 10
  last_age_prots = age % 100

  if 11 <= last_age_prots <= 19:
    print(f"{age} лет")
  elif age_prots == 1:
    print(f"{age} год")
  elif 2 <= age_prots <= 4:
    print(f"{age} года")
  else:
    print(f"{age} лет")
else:
  print("Возраст должен быть от 0 до 120 лет.")