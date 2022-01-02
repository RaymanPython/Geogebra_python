import pygame
import pygame_gui
import geometry_object
import random
import Data_save as data

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def point_to_geometry(a):
    return geometry_object.Point(a.x, a.y)

class Line(geometry_object.Line):

    def __init__(self, a, b):
        self.color = BLACK
        self.A = a
        self.B = b
        self.init()
        self.h = 5
        self.show = True
        self.remove = True

    def get_cor(self, x):
        return (x, self.y(x))

    def draw(self, screen):
        if self.b == 0:
            if self.a == 0:
                return
            else:
                p1, p2 = (int(-self.c / self.a), -100), (int(-self.c / self.a), 1000)
        else:
            p1, p2 = self.get_cor(-60), self.get_cor(1000)
        # pygame.draw.line(screen, self.color, (self.A.x, self.A.y), (self.B.x, self.B.y), 5)
        pygame.draw.line(screen, self.color, p1, p2, self.h)
        # # # print(p1, p2)

    def init(self):
        try:
            a = point_to_geometry(all.point[self.A])
            b = point_to_geometry(all.point[self.B])
            r = a.dist(b)
            super().__init__(a, b)
        except:
            self.removef()
            # # print(all.point[self.A])

    def removef(self):
        self.show = False
        self.A = None
        self.B = None

    def __str__(self):
        return f'Line({self.A}, {self.B})'


class Circle(geometry_object.Circle):

    def __init__(self, a, b):
        self.color = BLACK
        self.A = a
        self.B = b
        self.init()
        self.h = 5
        self.show = True
        self.remove = True

    def get_cor(self, x):
        return (x, self.y(x))

    def draw(self, screen):
        # pygame.draw.line(screen, self.color, (self.A.x, self.A.y), (self.B.x, self.B.y), 5)
        pygame.draw.circle(screen, self.color, (self.x,  self.y), self.r, self.h)
        # # # print(p1, p2)

    def init(self):
        try:
            a = point_to_geometry(all.point[self.A])
            b = point_to_geometry(all.point[self.B])
            r = a.dist(b)
            super().__init__(a.x, a.y, r)
        except:
            self.removef()

    def removef(self):
        self.show = False
        self.A = None
        self.B = None

    def __str__(self):
        return f'Circle({self.A}, {self.B})'



class Triangle(geometry_object.Triangle):

    def __init__(self, a, b=None, c=None):
        self.A = a
        self.B = b
        self.C = c
        self.h = 5
        self.color = BLACK
        self.show = True
        self.init()
        self.remove = True

    def draw(self, screen):
        for i in range(3):
            a = self.p[i]
            b = self.p[(i + 1) % 3]
            pygame.draw.line(screen, self.color, (a.x, a.y), (b.x,b.y), self.h)

    def init(self):
        try:
            if self.B == None and self.C == None:
                a = point_to_geometry(all.point[self.A])
                if not (a.show):
                    self.removef()
                    return
                super().__init__(a, a, a)
            elif self.B != None and self.C == None:
                a = point_to_geometry(all.point[self.A])
                b = point_to_geometry(all.point[self.B])
                super().__init__(a, b, b)
            else:
                a = point_to_geometry(all.point[self.A])
                b = point_to_geometry(all.point[self.B])
                c = point_to_geometry(all.point[self.C])
                super().__init__(a, b, c)
        except:
            self.removef()

    def removef(self):
        self.show = False
        self.A = None
        self.B = None
        self.C = None

    def __str__(self):
        return f'Triangle({self.A}, {self.B}, {self.C})'



class Vcircle(geometry_object.Circle):

    def __init__(self, ind):
        self.index = ind
        self.h = 5
        self.color = BLACK
        self.show = True
        self.remove = True

    def draw(self, screen):
        # pygame.draw.line(screen, self.color, (self.A.x, self.A.y), (self.B.x, self.B.y), 5)
        pygame.draw.circle(screen, self.color, (self.x,  self.y), self.r, self.h)

    def init(self):
        try:
            tr = all.all_sprites[self.index]
            circle = tr.min_circle()
            super().__init__(circle.x, circle.y, circle.r)
        except:
            self.removef()

    def removef(self):
        self.show = False
        self.x = None
        self.y = None

    def __str__(self):
        return f'Vcircle({self.index})'




class Point(geometry_object.Point):

    def __init__(self, x, y):
        # self.color = random.choice([BLUE, RED, GREEN])
        self.color = BLUE
        self.move = True
        super().__init__(x, y)
        # self.r = random.choice([5,10, 15, 20])
        self.r = 5
        self.show = True

    def draw(self, screen):
        if self.move:
            self.color = BLUE
        else:
            self.color = GREEN
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def removef(self):
        print(self.show)
        self.show = False

    def __str__(self):
        return f'{self.x}, {self.y}'


WIDTH = 900 # ширина игрового окна
HEIGHT = 700  # высота игрового окна
FPS = 30  # частота кадров в секунду


class All:

    def __init__(self):
        self.all_sprites = []
        self.point = []


    def sprites(self):
        return self.all_sprites + self.point

    def __len__(self):
        return len(self.point)

    def add_point(self, x, y):
        a = geometry_object.Point(x, y)
        for i in range(self.__len__()):
            a = self.point[i]
            if (x - a.x) ** 2 + (y - a.y) ** 2 <= 25:
                return i
        self.point.append(Point(x, y))
        return self.__len__() - 1

    def add_object(self, ob):
        # добавление обьекта построенного по двумточками
        line = ob
        self.all_sprites.append(line)


    def __str__(self):
        # # print(self.point)
        return '5'

    def remove(self, ind):
        if self.all_sprites[ind].remove:
            self.all_sprites[ind].removef()

    def remove_point(self, ind):
        self.point[ind].removef()

    def upted(self):
        for i in range(self.__len__()):
            for j in range(i + 2, self.__len__()):
                a = self.point[i]
                b = self.point[j]
                if (a.x - b.x) ** 2 + (a.y - b.y) ** 2 <= 25:
                    self.point[j] = self.point[i]

    def sum(self, i , j):
        for k in range(len(self.all_sprites)):
            a = self.all_sprites[k]
            if not a.show:
                continue
            if type(a) == Triangle:
                if self.all_sprites[k].C == j:
                    self.all_sprites[k].C = i
            if self.all_sprites[k].A == j:
                # # print(True, True)
                self.all_sprites[k].A = i
            if self.all_sprites[k].B == j:
                # # print(True, False, k, j, i)
                self.all_sprites[k].B = i
        # # print(list(map(str, self.point)))

    def upted_index(self, index):
        remove = False
        for i in range(self.__len__()):
            if i == index:
                continue
            if type(self.point[i]) == type(None) or type(self.point[index]) == type(None):
                continue
            if self.point[i].sq_dist(self.point[index]) <= 25:
                self.sum(i, index)
                remove = True
        if remove:
            self.remove_point(index)

    def init(self):
        for i in range(len(self.all_sprites)):
            if type(self.all_sprites[i]) != type(None) and self.all_sprites[i].show:
                self.all_sprites[i].init()


def save(all):
    data.save(all)

def open_file():
    global all
    all = All()
    s = data.open()
    for i in s:
        print(i)
        eval(i)

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
text = ['прямая', 'окружность', 'треугольник', 'точка', 'удаление', 'переместить', 'вписанная окружность', 'сохранить', 'открыть']
text_object = ['line', 'circle', 'triangle', 'point', 'remove', 'poisk', 'vcircle', 'save', 'open']
button = []
wb = 100
hb = 50
for i in range(len(text)):
    button.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((i * wb + 1, 0), (wb - 2, hb - 2)),
                                            text=text[i],
                                            manager=manager)
                  )
# all_sprites = []

# Цикл игры

running = True

mouse_cors = []
object_type = ''
sprite_move = -1
index_move = -1
all = All()
delta = 40
for i in range(20):
    ind1 = all.add_point(-100,  delta * i)
    ind2 = all.add_point(-50, delta * i)
    line = Line(ind1, ind2)
    line.color = BLUE
    line.h = 2
    line.remove = False
    all.all_sprites.append(line)
    ind1 = all.add_point(delta * i, -100)
    ind2 = all.add_point(delta * i, -50)
    line = Line(ind1, ind2)
    line.color = BLUE
    line.h = 2
    line.remove = False
    all.all_sprites.append(line)
while running:
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
                    if event.ui_element == button[i]:
                        object_type = text_object[i]
                        if object_type == 'save':
                            save(all)
                        elif object_type == 'open':
                            open_file()
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] <= hb:
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
            elif object_type == 'vcircle':
                for i in range(len(all.all_sprites)):
                    if type(all.all_sprites[i]) == Triangle:
                        pos = event.pos
                        if all.all_sprites[i].in_to(geometry_object.Point(pos[0], pos[1])):
                            all.add_object(Vcircle(i))

            elif object_type == 'poisk':
                pos = event.pos
                for i in range(len(all)):
                    ob = all.point[i]
                    if type(ob) == Point:
                        if (ob.x - pos[0]) ** 2 + (ob.y - pos[1]) ** 2 <= 25:
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
                        if all.all_sprites[i].in_to(p, 5):
                            all.remove(i)
                        # all.all_sprites[i] = None
                for i in range(len(all.point)):
                    if type(all.point[i]) == Point and type(all.point[i]) != type(None):
                        # # # print(i, 'com', type(all.all_sprites[i]))
                        if all.point[i].in_to(p, 5):
                            all.remove_point(i)


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
        # # # print(i)
    clock.tick(30)

    manager.draw_ui(screen)
    # Обновляем экран после рисования объектов
    pygame.display.flip()
pygame.quit()
# # print(all.all_sprites)
# # print(all)