import pygame
import pygame_gui
import geometry_object
import Data_save as data
from copy import copy
from History import His
from ALL_object import All
from Draw_object import *
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 900 # ширина игрового окна
HEIGHT = 700  # высота игрового окна
FPS = 30  # частота кадров в секунду

def save(all):
    data.save(all)

def open_file():
    global all
    all = All()
    all.draw_setka()
    s = data.open()
    for i in s:
        try:
            eval(i)
        except:
            pass

# Создаем игру и окно
pygame.init()

pygame.display.set_caption('Mini_Geogebra')

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((WIDTH, HEIGHT))
clock = pygame.time.Clock()


manager = pygame_gui.UIManager((WIDTH, HEIGHT))
time_delta = clock.tick(30) / 1000.0
text = [['сохранить', 'прямая', 'окружность', 'треугольник', 'точка', 'удаление', 'переместить', 'вписанная',
         'описанная', 'касательная'],
        ['открыть'],
        ['назад'],
        ['вперёд']]
text_object = [['save', 'line', 'circle', 'triangle', 'point', 'remove', 'poisk', 'vcircle', 'ocircle', 'cos'],
               ['open'],
               ['-1'],
               ['+1']]
button = []
wb = 100
hb = 50
for i in range(len(text)):
    for j in range(len(text[i])):
        button.append([])
        button[i].append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((i * wb + 1, j * hb), (wb - 2, hb - 2)),
                                            text=text[i][j],
                                            manager=manager)
                  )
# all_sprites = []

# Цикл игры

running = True
history = His()
mouse_cors = []
object_type = ''
sprite_move = -1
index_move = -1
all = All()
all.draw_setka()
index = 0
flag = True
poisk_list = []
history.append(all)
while running:
    flag = True
    # print(history, history.index, len(history.get()))
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                for i in range(len(button)):
                    for j in range(len(button[i])):
                        if event.ui_element == button[i][j]:
                            object_type = text_object[i][j]
                            flag = False
                            if object_type == 'save':
                                save(all)
                            elif object_type == 'open':
                                open_file()
                            elif object_type == '-1':
                                history.rs()
                                all = All()
                                all.draw_setka()
                                all = history.get()
                                object_type = ''
                            elif object_type == '+1':
                                history.ss()
                                all = All()
                                all.draw_setka()
                                all = history.get()
                                object_type = ''
        if event.type == pygame.KEYDOWN:
            # If pressed key is ESC quit program
            if event.key == pygame.K_1:
                object_type = 'poisk'
            elif event.key == pygame.K_2:
                object_type = 'line'
            elif event.key == pygame.K_3:
                object_type = 'point'
            elif event.key == pygame.K_4:
                object_type = 'circle'
            elif event.key == pygame.K_5:
                object_type = 'triangle'
            elif event.key == pygame.K_r:
                object_type = 'remove'
            elif event.key == pygame.K_LEFT:
                all.move(10, 0)
            elif event.key == pygame.K_RIGHT:
                all.move(-10, 0)
            elif event.key == pygame.K_DOWN:
                all.move(0, -10)
            elif event.key == pygame.K_UP:
                all.move(0, 10)
        elif event.type == pygame.MOUSEBUTTONDOWN and flag:
            if event.pos[0] <= wb or event.pos[1] <= 2 * hb:
                pass
            # print(object_type)
            elif index_move != -1:
                pos = event.pos
                # # print(index_move)
                if type(all.point[index_move]) == Point:
                    all.point[index_move].__init__(pos[0], pos[1])
                    all.upted_index(index_move)
                    index_move = -1
            elif object_type == 'line':
                if len(mouse_cors) == 0:
                    pos = pygame.mouse.get_pos()
                    mouse_cors.append(pos)
                    a = mouse_cors[0]
                    a = geometry_object.Point(a[0], a[1])
                    ind1 = all.add_point(pos[0], pos[1])
                    ind2 = all.add_point(pos[0] + 10, pos[1])
                    all.add_object(Line(ind1, ind2))
                elif len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    pos = event.pos
                    all.point[all.all_sprites[-1].A].__init__(a[0], a[1])
                    all.point[all.all_sprites[-1].B].__init__(pos[0], pos[1])
                    all.upted_index(all.all_sprites[-1].B)
                    all.all_sprites[-1].init()
                    mouse_cors = []
            elif object_type == 'circle':
                if len(mouse_cors) == 0:
                    pos = pygame.mouse.get_pos()
                    mouse_cors.append(pos)
                    a = mouse_cors[0]
                    a = geometry_object.Point(a[0], a[1])
                    ind1 = all.add_point(pos[0], pos[1])
                    ind2 = all.add_point(pos[0] + 10, pos[1])
                    all.add_object(Circle(ind1, ind2))
                elif len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    pos = event.pos
                    all.point[all.all_sprites[-1].A].__init__(a[0], a[1])
                    all.point[all.all_sprites[-1].B].__init__(pos[0], pos[1])
                    all.upted_index(all.all_sprites[-1].B)
                    all.all_sprites[-1].init()
                    mouse_cors = []
                # # # print(pos)
            elif object_type == 'triangle':
                # print(object_type, 5)
                if len(mouse_cors) == 0:
                    pos = event.pos
                    ind1 = all.add_point(pos[0], pos[1])
                    ind2 = all.add_point(pos[0] + 10, pos[1])
                    tr = Triangle(ind1, ind2)
                    all.add_object(tr)
                    mouse_cors.append(pos)
                elif len(mouse_cors) == 1:
                    pos = event.pos
                    ind2 = all.add_point(pos[0] + 10, pos[1])
                    all.point[all.all_sprites[-1].B].__init__(pos[0], pos[1])
                    all.all_sprites[-1].C = ind2
                    all.upted_index(all.all_sprites[-1].B)
                    mouse_cors.append(pos)
                elif len(mouse_cors) == 2:
                    pos = event.pos
                    all.point[all.all_sprites[-1].C].__init__(pos[0], pos[1])
                    all.upted_index(all.all_sprites[-1].C)
                    mouse_cors = []
            elif object_type == 'point':
                pos = event.pos
                all.add_point(pos[0], pos[1])
            elif object_type == 'vcircle' or object_type == 'ocircle':
                for i in range(len(all.all_sprites)):
                    if not all.all_sprites[i].show:
                        continue
                    try:
                        if type(all.all_sprites[i]) == Triangle:
                            pos = event.pos
                            if all.all_sprites[i].in_to(geometry_object.Point(pos[0], pos[1]), 0):
                                if object_type == 'vcircle':
                                    all.add_object(Vcircle(i))
                                if object_type == 'ocircle':
                                    all.add_object(Ocircle(i))
                    except:
                        pass
            elif object_type == 'cos':
                ind = all.poisk(Point(event.pos[0], event.pos[1]), Point)
                ind1 = all.poisk(Point(event.pos[0], event.pos[1]), Circle)
                if ind != -1:
                    if len(poisk_list) == 0:
                        poisk_list.append((ind, Point))
                    elif len(poisk_list) == 1:
                        if poisk_list[0][1] == Point:
                            poisk_list[0] = (ind, Point)
                        else:
                            cs = Cos(ind, poisk_list[0][0])
                            all.add_object(cs)
                            poisk_list = []
                if ind1 != -1:
                    if len(poisk_list) == 0:
                        poisk_list.append((ind1, Circle))
                    elif len(poisk_list) == 1:
                        if poisk_list[0][1] == Circle:
                            poisk_list[0] = (ind1, Circle)
                        else:
                            cs = Cos(poisk_list[0][0], ind1)
                            all.add_object(cs)
                            poisk_list = []


            elif object_type == 'poisk':
                pos = event.pos
                for i in range(len(all)):
                    ob = all.point[i]
                    if type(ob) == Point:
                        if ob.sq_dist(pos[0], pos[1]) <= 25:
                            index_move = i
                            all.point[i].color = RED
            elif object_type == 'remove':
                pos = event.pos
                p = geometry_object.Point(pos[0], pos[1])
                for i in range(len(all.all_sprites)):
                    if not all.all_sprites[i].show:
                        continue
                    if type(all.all_sprites[i]) != Point and type(all.all_sprites[i]) != type(None):
                        # # # print(i, 'com', type(all.all_sprites[i]))
                        if all.all_sprites[i].show:
                            if all.all_sprites[i].in_to(p, 5):
                                all.remove(i)
                        # all.all_sprites[i] = None
                for i in range(len(all.point)):
                    if type(all.point[i]) == Point and type(all.point[i]) != type(None):
                        # # # print(i, 'com', type(all.all_sprites[i]))
                        if all.point[i].show:
                            if all.point[i].sq_dist(p) <= 25:
                                all.remove_point(i)
            if event.pos[0] <= wb or event.pos[1] <= 2 * hb:
                pass
            else:
                history.append(all)
        elif event.type == pygame.MOUSEMOTION:
            if object_type == 'triangle':
                if len(mouse_cors) == 0:
                    pass
                elif all.all_sprites[-1].C == None:
                    b = event.pos
                    all.point[all.all_sprites[-1].B].__init__(b[0], b[1])
                    all.all_sprites[-1].init()
                else:
                    b = event.pos
                    all.point[all.all_sprites[-1].C].__init__(b[0], b[1])
                    all.all_sprites[-1].init()
            elif object_type != None and object_type != 'point':
                if len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    b = event.pos
                    # all.point[all.all_sprites[-1].A].__init__(a[0], a[1])
                    all.point[all.all_sprites[-1].B].__init__(b[0], b[1])
                    # all.upted_index(all.all_sprites[-1].A)
                    # all.upted_index(all.all_sprites[-1].B)
                    all.all_sprites[-1].init()
                    # mouse_cors = []
            if index_move != -1:
                pos = pygame.mouse.get_pos()
                # # # print(index_move)
                if type(all.point[index_move]) == Point:
                    all.point[index_move].__init__(pos[0], pos[1])

        manager.process_events(event)
    manager.update(time_delta)
    # Обновление

    # Обновление
    # all.all_sprites.update()

    all.init()

    # all.upted()
    # Отрисовка
    screen.fill(WHITE)
    for i in all.sprites():
        if type(i) == type(None):
            continue
        if i.show:
            i.draw(screen)
        else:
            pass
        # # # print(i)
    clock.tick(30)

    manager.draw_ui(screen)
    # Обновляем экран после рисования объектов
    pygame.display.flip()
pygame.quit()
# # print(all.all_sprites)
# # print(all)