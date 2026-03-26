#Подключаем модуль
import pygame

# Инициализация pygame
pygame.init()

#Установка стартовых значений и настройки
FPS = 

#Ширина и высота экрана
SCREEN_WIDTH = 
SCREEN_HEIGHT = 

#Инициализируем объект окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Загружаем изображение из относительного пути (только внутри директории проекта)
background_img = pygame.image.load("")
#Отрисовываем изображение в буфер (пока не выводим на экран)
#Каждый следующий blit нарисует что-то поверх предыдущего с наслоением
screen.blit(background_img, (0,0))

#Создаем объект для отслеживания времени
clock = pygame.time.Clock()

#Для проверки игрового цикла
running = True

#Дельта-тайм - разница во времени в милисекундах между предыдущим и текущим кадром.
dt = 0




player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player_pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:


    screen.blit(background_img, (0,0))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
        
            running = False
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:  
            print(f"Нажата кнопка: {event.button}")
            
            print(f"Позиция: {event.pos}")

        '''if event.type == pygame.MOUSEBUTTONUP:  # Кнопка мыши отпущена
            print(f"Отпущена кнопка: {event.button}")
            print(f"Позиция: {event.pos}")'''
    
    
    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.draw.circle(screen, "red", player_pos2, 40)
    
    key = pygame.key.get_pressed()
    key2 = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if player_pos.y >= 300 * dt: player_pos.y -= 300 * dt
    if key[pygame.K_s]:
        if player_pos.y <= screen.get_height() - 300 * dt: player_pos.y += 300 * dt
    if key[pygame.K_a]:
        if player_pos.x >= 300 * dt: player_pos.x -= 300 * dt
    if key[pygame.K_d]:
        if player_pos.x <= screen.get_width() - 300 * dt: player_pos.x += 300 * dt

    if key2[pygame.K_UP]:
        if player_pos2.y >= 300 * dt: player_pos2.y -= 300 * dt
    if key2[pygame.K_DOWN]:
        if player_pos2.y <= screen.get_height() - 300 * dt: player_pos2.y += 300 * dt
    if key2[pygame.K_LEFT]:
        if player_pos2.x >= 300 * dt: player_pos2.x -= 300 * dt
    if key2[pygame.K_RIGHT]:
        if player_pos2.x <= screen.get_width() - 300 * dt: player_pos2.x += 300 * dt


    
    pygame.display.flip()


    dt = clock.tick(FPS) / 1000

pygame.quit()
