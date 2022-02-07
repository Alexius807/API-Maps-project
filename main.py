import pygame
import requests
import sys
import os


def update_map(x, y):
    x, y = map(str, (x, y))
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
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    ## Инициализируем pygame
    # pygame.init()
    # screen = pygame.display.set_mode((600, 450))
    ## Рисуем картинку, загружаемую из только что созданного файла.
    # screen.blit(pygame.image.load(map_file), (0, 0))
    ## Переключаем экран и ждем закрытия окна.
    # pygame.display.flip()
    # while pygame.event.wait().type != pygame.QUIT:
    #    pass

    # pygame.quit()
    ## Удаляем за собой файл с изображением.
    # os.remove(map_file)


x, y = -71.092072, 42.359628
map_file = "map.png"
update_map(x, y)
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 450
                update_map(x, y)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_DOWN:
                y += 450
                update_map(x, y)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_RIGHT:
                x += 600
                update_map(x, y)
                screen.blit(pygame.image.load(map_file), (0, 0))
            if event.key == pygame.K_LEFT:
                x -= 600
                update_map(x, y)
                screen.blit(pygame.image.load(map_file), (0, 0))
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    pygame.display.flip()

# Удаляем за собой файл с изображением.
os.remove(map_file)
