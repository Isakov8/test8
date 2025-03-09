while True:
    name = input("Введите ваше имя: ")
    if not name:
        print("Имя не указано, попробуйте снова")
        continue

    prof = input("Введите вашу профессию: ")
    if not prof:
        print("Профессия не указана, попробуйте снова")
        continue

    instrument = input("Какой любимый инструмент для тестирования? ")
    if not instrument:
        print("Инструмент не указан, попробуйте снова")
        continue

    print(f"{name}, ваш любимый инструмент: {instrument}")
    break
