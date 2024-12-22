def show_menu() -> None:
    print("Выберите пункт меню")
    print("1. Работа с числами")
    print("2. Работа с текстом")
    print("3. Выход")


def parse_numbers() -> list[int]:
    return list(map(int, input().split(',')))


def parse_strings() -> list[str]:
    return list(map(str, input().split(' ')))


def process_numbers() -> None:
    print("Введите числа через запятую: ", end="")
    numbers = parse_numbers()
    print("Максимальное число: " + str(find_max(numbers)))
    print("Минимальное число: " + str(find_min(numbers)))
    print("Сумма чисел: " + str(calculate_sum(numbers)))


def find_max(number) -> int:
    return max(number)


def find_min(number) -> int:
    return min(number)


def calculate_sum(numbers) -> int:
    return sum(numbers)


def process_strings() -> None:
    print("Введите текст: ", end="")
    words = parse_strings()
    count_symbols(words)
    count_words(words)


def count_words(words) -> None:
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    print("Частнотность слов:")
    for word in word_dictionary:
        print(word + ": " + str(word_dictionary[word]))


def count_symbols(words) -> None:
    letter_dictionary = {}
    for word in words:
        for letter in word:
            if letter in letter_dictionary:
                letter_dictionary[letter] += 1
            else:
                letter_dictionary[letter] = 1
    print("Частотность символов:")
    for letter in letter_dictionary:
        print(letter + ": " + str(letter_dictionary[letter]))


def handle_menu_point() -> bool:
    point = int(input())
    if point == 1:
        process_numbers()
        return True
    elif point == 2:
        process_strings()
        return True
    elif point == 3:
        return False
    else:
        print("Введён неизвестный пункт")
        return True


def want_to_continue():
    print("Хотите продолжить? (да/нет): ", end="")
    while True:
        answer = input()
        if answer == "да":
            return True
        elif answer == "нет":
            return False
        else:
            print("Неправильный ввод, укажите да или нет")


def run():
    while True:
        show_menu()
        if not handle_menu_point():
            break
        if not want_to_continue():
            break
