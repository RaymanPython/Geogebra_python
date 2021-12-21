import pygame
import geometry_object
import random

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Line(geometry_object.Line):

    def __init__(self, a, b):
        self.color = BLACK
        super().__init__(a, b)
        self.A = a
        self.B = b

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

class Point(geometry_object.Point):

    def __init__(self, x, y):
        # self.color = random.choice([BLUE, RED, GREEN])
        self.color = BLUE
        super().__init__(x, y)
        # self.r = random.choice([5,10, 15, 20])
        self.r = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)



WIDTH = 700 # ширина игрового окна
HEIGHT = 700 # высота игрового окна
FPS = 30 # частота кадров в секунду

class All:

    def __init__(self):
        self.all_sprites = []
        self.point_conect = dict()

    def sprites(self):
        return self.all_sprites

    def __len__(self):
        return len(self.all_sprites)

    def add_point(self, x, y):
        a = geometry_object.Point(x, y)
        self.all_sprites.append(Point(x, y))
        self.point_conect[self.__len__() - 1] = []

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
        for i in range(self.__len__()):
            if type(self.all_sprites[i]) == Point:
                p = self.all_sprites[i]
                p = geometry_object.Point(p.x, p.y)
                if line.in_to(p, 5):
                    self.point_conect[i].append(self.__len__() - 1)

    def __str__(self):
        print(self.point_conect)
        return '5'

    def remove(self, ind):
        self.all_sprites[ind] = None

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


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#all_sprites = []

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
            elif event.key == pygame.K_r:
                object_type = 'remove'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if index_move != -1:
                pos = event.pos
                print(index_move)
                if type(all.all_sprites[index_move]) == Point:
                    all.all_sprites[index_move].__init__(pos[0], pos[1])
                    index_move = -1
            elif object_type == 'line':
                if len(mouse_cors) == 0:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    mouse_cors.append(pos)
                    a = mouse_cors[0]
                    a = geometry_object.Point(a[0], a[1])
                    all.add_point(pos[0], pos[1])
                    all.add_object(Line(a, a))
                elif len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    a = geometry_object.Point(a[0], a[1])
                    pos = event.pos
                    b = geometry_object.Point(pos[0], pos[1])
                    all.all_sprites[-1].__init__(a, b)
                    all.add_point(pos[0], pos[1])
                    mouse_cors = []
                # print(pos)
            elif object_type == 'point':
                pos = event.pos
                all.add_point(pos[0], pos[1])
            elif object_type == 'poisk':
                pos = event.pos
                for i in range(len(all)):
                    ob = all.all_sprites[i]
                    if type(ob) == Point:
                        if (ob.x - pos[0]) ** 2 + (ob.y - pos[1]) ** 2 <= 25:
                            index_move = i
                            all.all_sprites[i].color = RED
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
                        #all.all_sprites[i] = None

        elif event.type == pygame.MOUSEMOTION:
            if object_type != None and object_type != 'point':
                if len(mouse_cors) == 1:
                    a = mouse_cors[0]
                    a = geometry_object.Point(a[0], a[1])
                    b = event.pos
                    b = geometry_object.Point(b[0], b[1])
                    all.all_sprites[-1].__init__(a, b)
                    #mouse_cors = []
            if index_move != -1:
                pos = pygame.mouse.get_pos()
                # print(index_move)
                if type(all.all_sprites[index_move]) == Point:
                    all.all_sprites[index_move].__init__(pos[0], pos[1])
                    all.reinit(index_move)




    # Обновление

        # Обновление
        # all.all_sprites.update()

        # Отрисовка
    screen.fill(WHITE)
    for i in all.all_sprites:
        if type(i) == type(None):
            continue
        i.draw(screen)
        #print(i)

    clock.tick(30)
    # Обновляем экран после рисования объектов
    pygame.display.flip()
pygame.quit()
print(all.all_sprites)
print(all)