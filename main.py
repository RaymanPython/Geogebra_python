

import pygame
import geometry_object
import random

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

    def get_cor(self, x):
        return (x, self.y(x))

    def draw(self, screen):
        if self.b == 0:
            if self.a == 0:
                return
            else:
                p1, p2 = (int(-self.c / self.a), 0), (int(-self.c / self.a), 1)
        else:
            p1, p2 = self.get_cor(-60), self.get_cor(1000)
        # pygame.draw.line(screen, self.color, (self.A.x, self.A.y), (self.B.x, self.B.y), 5)
        pygame.draw.line(screen, self.color, p1, p2, 5)
        # print(p1, p2)

    def init(self):
        a = point_to_geometry(all.point[self.A])
        b = point_to_geometry(all.point[self.B])
        r = a.dist(b)
        super().__init__(a, b)


class Circle(geometry_object.Circle):

    def __init__(self, a, b):
        self.color = BLACK
        self.A = a
        self.B = b
        self.init()

    def get_cor(self, x):
        return (x, self.y(x))

    def draw(self, screen):
        # pygame.draw.line(screen, self.color, (self.A.x, self.A.y), (self.B.x, self.B.y), 5)
        pygame.draw.circle(screen, self.color, (self.x,  self.y), self.r, 5)
        # print(p1, p2)

    def init(self):
        a = point_to_geometry(all.point[self.A])
        b = point_to_geometry(all.point[self.B])
        r = a.dist(b)
        super().__init__(a.x, a.y, r)





class Point(geometry_object.Point):

    def __init__(self, x, y):
        # self.color = random.choice([BLUE, RED, GREEN])
        self.color = BLUE
        self.move = True
        super().__init__(x, y)
        # self.r = random.choice([5,10, 15, 20])
        self.r = 5

    def draw(self, screen):
        if self.move:
            self.color = BLUE
        else:
            self.color = GREEN
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


WIDTH = 1000  # ширина игрового окна
HEIGHT = 1000  # высота игрового окна
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
        '''
        :param ind1:
        :param ind2:
        :return:
        x, y = self.all_sprites[ind1].x, self.all_sprites[ind1].y
        a = geometry_object.Point(x, y)
        x, y = self.all_sprites[ind2].x, self.all_sprites[ind2].y
        b = geometry_object.Point()
        point_conect = dict()
        '''
        line = ob
        self.all_sprites.append(line)
        '''
        for i in range(self.__len__()):
            if type(self.all_sprites[i]) == Point:
                p = self.all_sprites[i]
                p = geometry_object.Point(p.x, p.y)
                if line.in_to(p, 5):
                    self.point_conect[i].append(self.__len__() - 1)
        '''

    def __str__(self):
        print(self.point)
        return '5'

    def remove(self, ind):
        self.all_sprites[ind] = None

    def remove_point(self, ind):
        self.point[ind] = None

    def reinit(self, index):
        for i in self.point_conect[index]:
            if type(self.all_sprites[i]) != type(None):
                for j in range(self.__len__()):
                    if type(all.all_sprites[j]) == Point:
                        if i in self.point_conect[j]:
                            a = all.all_sprites[i]
                            a = geometry_object.Point(a.x, a.y)
                            b = all.all_sprites[j]
                            b = geometry_object.Point(b.x, b.y)
                            all.all_sprites[i].__init__(a, b)

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
            if self.all_sprites[k].A == j:
                print(True, True)
                self.all_sprites[k].A = i
            if self.all_sprites[k].B == j:
                print(True, False, k, j, i)
                self.all_sprites[k].B = i
        print(list(map(str, self.point)))
        for i in self.all_sprites:
            print(i.A, i.B)

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
            if type(self.all_sprites[i]) != type(None):
                self.all_sprites[i].init()


                


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# all_sprites = []

# Цикл игры

running = True

mouse_cors = []
object_type = 'line'
sprite_move = -1
index_move = -1
all = All()
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
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
            elif event.key == pygame.K_r:
                object_type = 'remove'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if index_move != -1:
                pos = event.pos
                print(index_move)
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
                    all.all_sprites[-1].init()
                    mouse_cors = []
                # print(pos)
            elif object_type == 'point':
                pos = event.pos
                all.add_point(pos[0], pos[1])
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
                for i in range(len(all)):
                    if type(all.all_sprites[i]) != Point and type(all.all_sprites[i]) != type(None):
                        print(i, 'com', type(all.all_sprites[i]))
                        if all.all_sprites[i].in_to(p, 5):
                            all.remove(i)
                            print(i)
                            all.all_sprites[i] = None
                        # all.all_sprites[i] = None

        elif event.type == pygame.MOUSEMOTION:
            if object_type != None and object_type != 'point':
                if len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    b = event.pos
                    all.point[all.all_sprites[-1].A].__init__(a[0], a[1])
                    all.point[all.all_sprites[-1].B].__init__(b[0], b[1])
                    all.upted_index(all.all_sprites[-1].A)
                    all.upted_index(all.all_sprites[-1].B)
                    all.all_sprites[-1].init()
                    # mouse_cors = []
            if index_move != -1:
                pos = pygame.mouse.get_pos()
                # print(index_move)
                if type(all.point[index_move]) == Point:
                    all.point[index_move].__init__(pos[0], pos[1])


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
        i.draw(screen)
        # print(i)
    clock.tick(30)
    # Обновляем экран после рисования объектов
    pygame.display.flip()
pygame.quit()
print(all.all_sprites)
print(all)



