import pygame
import requests
import sys
import os


def show_map(x, y):
    api_server = "http://static-maps.yandex.ru/1.x/"
    delta = "0.002"
    params = {
        "ll": f'{x},{y}',
        "spn": ",".join([delta, delta]),
        "l": "map"
    }

    response = requests.get(api_server, params=params)

    if not response:
        print("Ошибка выполнения запроса")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)


show_map('-71.092072', '42.359628')
