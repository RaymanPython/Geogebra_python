import geometry_object
from Draw_object import *
from class_name_point import Name_Point
# класс хранящий все объекты

class All:

    def __init__(self):
        self.all_sprites = []
        self.point = []
        self.point_names = Name_Point()

    def draw_setka(self):
        delta = 40
        for i in range(25):
            ind1 = self.add_point(-100, delta * i)
            ind2 = self.add_point(-50, delta * i)
            self.point[ind1].save = False
            self.point[ind2].save = False
            line = Line(ind1, ind2)
            line.color = BLUE
            line.h = 2
            line.remove = False
            line.save = False
            self.all_sprites.append(line)
            ind1 = self.add_point(delta * i, -100)
            ind2 = self.add_point(delta * i, -50)
            self.point[ind1].save = False
            self.point[ind2].save = False
            line = Line(ind1, ind2)
            line.color = BLUE
            line.h = 2
            line.remove = False
            line.save = False
            self.all_sprites.append(line)

    def sprites(self):
        return self.all_sprites + self.point

    def __len__(self):
        return len(self.point)

    def add_point(self, x, y):
        for i in range(self.__len__()):
            a = self.point[i]
            try:
                if a.sq_dist(x, y) <= 25:
                    self.point[i].show = True
                    return i
            except:
                continue
        self.point.append(Point(x, y, self.point_names.append()))
        return self.__len__() - 1

    def add_object(self, object):
        # добавление обьекта построенного по двумточками
        self.all_sprites.append(object)
        self.cross()

    def __str__(self):
        # # print(self.point)
        return f'len_point = {len(self.point)}, len_all_object = {len(self.all_sprites)}'

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

    def sum(self, i, j):
        for k in range(len(self.all_sprites)):
            a = self.all_sprites[k]
            if not a.show:
                continue
            if type(a) == Triangle:
                if self.all_sprites[k].C == j:
                    self.all_sprites[k].C = i
            elif type(a) == Vcircle:
                return
            try:
                if self.all_sprites[k].A == j:
                    # # print(True, True)
                    self.all_sprites[k].A = i
                if self.all_sprites[k].B == j:
                    # # print(True, False, k, j, i)
                    self.all_sprites[k].B = i
            except:
                pass
        # # print(list(map(str, self.point)))

    def upted_index(self, index):
        remove = False
        for i in range(self.__len__()):
            if i == index:
                continue
            if type(self.point[i]) == type(None) or self.point[index].show == False:
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
        # self.cross()

    def poisk(self, p, typeb=Point):
        if typeb != Point:
            for i in range(len(self.all_sprites)):
                if type(self.all_sprites[i]) == typeb:
                    if self.all_sprites[i].in_to(p, 5):
                        return i
        else:
            for i in range(len(self.point)):
                if self.point[i].in_to(p, 5):
                    return i

    def cross(self):
        for i in range(len(self.all_sprites)):
            for j in range(i + 1, len(self.all_sprites)):
                a = self.all_sprites[i]
                b = self.all_sprites[j]
                points = a.cross(b)
                for point in points:
                    ind = self.add_point(point.x, point.y)
                    self.point[ind].show = False

    def move(self, x, y):
        for i in range(len(self.point)):
            self.point[i].x += x
            self.point[i].y += y
