# Проект FitLife - MVP версия 1.0
WATER_ML_PER_KG = 30
ML_IN_LITER = 1000


def main():
    """Основная функция программы."""
    # 1. Знакомство
    user_name = input("Привет! Как вас зовут? ")
    user_age = int(input("Введите ваш возраст (полных лет, целым числом): "))

    # 2. Сбор данных
    user_weight = float(
        input("Введите ваш вес (в кг, например 70.5): ").replace(",", ".")
    )
    user_height = float(
        input("Введите ваш рост (в метрах, например 1.75): ").replace(",", ".")
    )

    # 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
    # Формула ИМТ: вес разделить на (рост в квадрате)
    bmi = user_weight / (user_height ** 2)
    bmi = round(bmi, 1)

    # Подсчет воды: вес * 30 мл
    water_needed = user_weight * WATER_ML_PER_KG
    water_l = water_needed / ML_IN_LITER

    # Возврат всех перечисленных значений
    return user_name, user_age, bmi, water_needed, water_l


if __name__ == "__main__":
    user_name, user_age, bmi, water_needed, water_l = main()   
    # 4. Вывод красивого результата
    print(
        f"Привет, {user_name}!\n"
        f"Вам {user_age} лет.\n"
        f"Ваш индекс массы тела: {bmi:.1f}\n"
        f"Рекомендуемая норма воды: {water_l:.1f} л. в день\n"
        "Расчет окончен. Будьте здоровы!",
    )
