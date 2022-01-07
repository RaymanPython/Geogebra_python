import pygame
import geometry_object


def point_to_geometry(a):
    return geometry_object.Point(a.x, a.y)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


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
        from main import all
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
        from main import all
        try:
            a = point_to_geometry(all.point[self.A])
            b = point_to_geometry(all.point[self.B])
            r = a.dist(b)
            super().__init__(a.x, a.y, r)
        except:
            self.removef()

    def removef(self):
        print(Circle)
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
        try:
            if not self.show:
                return
            for i in range(3):
                a = self.p[i]
                b = self.p[(i + 1) % 3]
                pygame.draw.line(screen, self.color, (a.x, a.y), (b.x, b.y), self.h)
        except:
            self.removef()

    def init(self):
        from main import all
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
        from main import all
        try:
            tr = all.all_sprites[self.index]
            circle = tr.vc()
            super().__init__(circle.x, circle.y, circle.r)
        except:
            self.removef()

    def removef(self):
        print(Circle)
        self.show = False
        self.x = None
        self.y = None

    def __str__(self):
        return f'Vcircle({self.index})'

class Ocircle(geometry_object.Circle):

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
        from main import all
        try:
            tr = all.all_sprites[self.index]
            circle = tr.oc()
            super().__init__(circle.x, circle.y, circle.r)
        except:
            self.removef()

    def removef(self):
        self.show = False
        self.x = None
        self.y = None

    def __str__(self):
        return f'Vcircle({self.index})'

class Cos(geometry_object.Line):

    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.show = True
        self.remove = True
        self.h = 5
        self.color = BLACK

    def draw(self, screen):
        po = all.point[self.A]
        if len(self.li) == 1:
            pygame.draw.line(screen, self.color, (po.x, po.y), (self.li[0].x, self.li[0].y), self.h)
        elif len(self.li) == 2:
            pygame.draw.line(screen, self.color, (po.x, po.y), (self.li[0].x, self.li[0].y), self.h)
            pygame.draw.line(screen, self.color, (po.x, po.y), (self.li[1].x, self.li[1].y), self.h)

    def init(self):
        from main import all
        cr = all.all_sprites[self.B]
        po = all.point[self.A]
        li = cr.cross_line(po)
        self.li = li
        if len(li) > 0:
            super().__init__(li[0], po)
        else:
            pass




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
        try:
            if self.move:
                self.color = BLUE
            else:
                self.color = GREEN
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        except:
            pass

    def removef(self):
        print(self.show)
        self.show = False
        self.x = None
        self.y = None

    def __str__(self):
        return f'{self.x}, {self.y}'