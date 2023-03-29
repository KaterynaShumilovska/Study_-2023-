# Завдання 1
def my_first_function():
    return 'Це моя перша функція.'


print(my_first_function())


# Завдання 2
def square_num(a):
    return a * a


num = int(input('Введіть число, квадрат якого необхідно розрахувати: '))
print(f'Квадрат числа {num} дорівнює: {square_num(num)}')

# Завдання 3
films = ['Spider-man: No way to home',
         'Crazy Stupid Love.',
         'Die Hard',
         'Dead Poets Society',
         'Home Alone',
         'Seven',
         'Memento',
         'Harry Potter and the Prisoner of Azkaban',
         "One Flew Over the Cuckoo's Nest"
         ]


def names_of_films_more_than_8_letters(film):
    new_films_list = []
    for i in film:
        if len(i) > 8:
            new_films_list.append(i)
    return new_films_list


print(f'Список фільмів назва яких більше 8 літер: {names_of_films_more_than_8_letters(films)}')

# Завдання 4
test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]


def average_and_first_number_than_greater_average(number_list):
    result = []
    average = sum(number_list) / len(number_list)
    result.append(average)
    for i in number_list:
        if i > average:
            result.append(i)
            return tuple(result)


print(average_and_first_number_than_greater_average(test_list))


# Завдання 5
def even_numbers(number_list):
    result = []
    for i in number_list:
        if i % 2 == 0:
            result.append(i)
    return result


print(even_numbers(test_list))

# Завдання 6
grade = [('Англійська мова', 88), ('Біологія', 90), ('Математика', 97), ('Українська мова', 82)]


def highest_score(scores):
    high_score = 0
    for i, j in scores:
        if high_score <= j:
            high_score = j
    return i


print(f'Найвища оцінка отримана з предмету: {highest_score(grade)}')


# Завдання 7


def number_to_power(num, step = 2):
    return num ** step


print(number_to_power(8))


# Завдання 8
films_title = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}


def seach_film(imdb_id):
    for i in films_title['results']:
        if i.get("imdb_id") == imdb_id:
            title_film = i["title"]
            return title_film


imdb = input('Введіть imdb_id фільму для пошуку: ')
print(f'Назва  фільму, який ви шукали: {seach_film(imdb)}')