light_level = int(input("Введите уровень освещенности (1-10): "))
if light_level < 4:
    print("Яркость ламп: низкая")
elif light_level < 7:
    print("Яркость ламп: средняя")
else:
    print("Яркость ламп: высокая")
