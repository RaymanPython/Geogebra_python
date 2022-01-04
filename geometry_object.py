import math


class Point:
    def __init__(self, x=None, y=None, polar=False):
        self.polar = polar
        if type(x) == Point:
            self = x
        elif not polar:
            self.x = x
            self.y = y
        else:
            self.a = y
            self.r = x
            self.x = math.cos(y) * x
            self.y = math.sin(y) * x

    def sq_dist(self, x=None, y=None):
        try:
            if type(y) == type(None):
                x1, y1 = x.x, x.y
            else:
                x1, y1 = x, y
            return (self.x - x1) ** 2 + (self.y - y1) ** 2
        except:
            return 10000

    def dist(self, x=0, y=0):
        if type(x) == Point:
            x1, y1 = x.x, x.y
        else:
            x1, y1 = x, y
        return math.sqrt((self.x - x1) ** 2 + (self.y - y1) ** 2)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def in_to(self, p, eps):
        try:
            return self.sq_dist(p) <= eps ** 2
        except:
            return False

    def __str__(self):
        return f'{self.x}, {self.y}'


class Vector(Point):

    def __init__(self, *s):
        s = list(s)
        if len(s) == 0:
            self.x = 0
            self.y = 0
        elif len(s) == 1:
            if type(s[0]) == Point:
                self.x = s[0].x
                self.y = s[0].y
        elif len(s) == 2:
            if type(s[0]) == Point and type(s[1]) == Point:
                self.x = s[1].x - s[0].x
                self.y = s[1].y - s[0].y
            else:
                self.x, self.y = float(s[0]), float(s[1])
        elif len(s) == 4:
            self.x = s[2] - s[0]
            self.y = s[3] - s[1]

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y

    def vector_product(self, other):
        return self.x * other.y - other.x * self.y

    def __xor__(self, other):
        return self.vector_product(other)

    def mul(self, other):
        return Vector(self.x * other, self.y * other)

    def dot_product(self, other):
        return self.scalar_product(other)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.mul(other)
        return self.scalar_product(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + other.mul(-1)

    def cross_product(self, other):
        return self.vector_product(other)

    def phi(self):
        a = math.atan2(self.y, self.x)
        if a < 0:
            a += 2 * math.pi
        return a

    def sq_dist(self):
        return self.x ** 2 + self.y ** 2

    def in_to(self, p1, p2, p3):
        a = Vector(p2, p3)
        b = Vector(p2, p1)
        if b.sq_dist() == 0:
            return True
        else:
            if (a * b) ** 2 == a.sq_dist() * b.sq_dist() and a * b > 0:
                return True
            else:
                return False

    def prov(self, p1, p2, p3, p4):
        a = Vector(p1, p2)
        b = Vector(p3, p4)
        c = Vector(p1, p3)
        if c.sq_dist() == 0:
            return True
        if a ^ b == 0:
            if a ^ c != 0:
                return False
            else:
                if a * b >= 0:
                    return True
                elif a * c >= 0:
                    return True
                else:
                    return False
        else:
            if (c ^ a) * (c ^ b) >= 0 and (b ^ a) * (b ^ c) >= 0:
                return True
            else:
                return False


class Line:
    def __init__(self, *s):
        if len(s) == 0:
            self.a, self.b, self.c = map(float, input().split())
        elif len(s) == 2:
            p1, p2 = s[1], s[0]
            self.a = p1.y - p2.y
            self.b = p2.x - p1.x
            self.c = p1.x * p2.y - p2.x * p1.y
        elif len(s) == 3:
            self.a, self.b, self.c = s

    def perpendicular(self, *s):
        if len(s) == 1:
            x, y = s[0].x, s[0].y
        elif len(s) == 2:
            x, y = s[0], s[1]
        return Line(self.b, -self.a, -self.b * x + self.a * y)

    def __xor__(self, other):
        return self.perpendicular(other)

    def in_to1(self, *s, eps=0):
        if len(s) == 1:
            x, y = s[0].x, s[0].y
        elif len(s) == 2:
            x, y = s[0], s[1]
        return abs(self.a * x + self.b * y + self.c) <= eps

    def in_to_class(self, s, eps=0):
        x, y = s.x, s.y
        print(abs(self.a * x + self.b * y + self.c))
        return abs(self.a * x + self.b * y + self.c) <= eps

    def in_to(self, s, eps=0):
        try:
            return self.or_h(s) <= eps
        except:
            return False

    def sign(self, p1, p2):
        return self.f(p1.x, p1.y) * self.f(p2.x, p2.y) > 0

    def f(self, x, y):
        return self.a * x + self.b * y + self.c

    def y(self, x):
        return (-self.a * x - self.c) / self.b

    def __eq__(self, line1):
        return self.a * line1.b == self.b * line1.a and self.b * line1.c == self.c * line1.b and self.a * line1.c == self.c * line1.a

    def is_parallel(self, line1):
        return self.a * line1.b == self.b * line1.a

    def classification(self, line1):
        if (self.a ** 2 + self.b ** 2) * (line1.a ** 2 + line1.b ** 2) == 0:
            return 0
        elif self == line1:
            return 1
        elif self.is_parallel(line1):
            return 2
        elif self.a * line1.a + self.b * line1.b == 0:
            return 3
        else:
            return 0

    def h(self, p):
        return abs(self.a * p.x + self.b * p.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    def norm(self):
        return Vector(self.a, self.b)

    def or_h(self, p):
        return abs(self.a * p.x + self.b * p.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    def base(self, p):
        a = Vector(p.x, p.y)
        n = self.norm()
        return a - n * (((a * n) + self.c) / n.sq_dist())

    def get_point(self):
        if self.b == 0:
            return Point(-self.c / self.a, 0)
        else:
            return Point(0, -self.c / self.b)

    def para_d(self, d):
        n = self.norm()
        v = n * (d / n.dist())
        p = self.get_point()
        p1 = v + p
        c2 = -(n * p1)
        return Line(self.a, self.b, c2)

    def cross(self, line1):
        if self == line1:
            return [2]
        elif self.is_parallel(line1):
            return [0]
        y = (line1.c * self.a - self.c * line1.a) / (self.b * line1.a - line1.b * self.a)
        x = (line1.c * self.b - self.c * line1.b) / (self.a * line1.b - line1.a * self.b)
        p = Point(x, y)
        return [p]

    def __sub__(self, p):
        if p.x == 0 and p.y == 0:
            return self
        else:
            a, b, c = self.a, self.b, self.c
            if b == 0:
                c -= p.y + p.y

    def __str__(self):
        return str(self.a) + ' ' + str(self.b) + ' ' + str(self.c)


def round_float(x, n):
    s = str(round(x, n))
    x, y = map(str, s.split('.'))
    y += '0' * n
    y = y[:n]
    return x + '.' + y


class Circle:
    def __init__(self, *s):
        if len(s) == 0:
            self.x, self.y, self.r = map(float, input().split())
        if len(s) == 3:
            self.x, self.y, self.r = s[0], s[1], s[2]


    def dist_line(self, line):
        h = line.h(Point(self.x, self.y)) - self.r
        if h < 0:
            return 0
        else:
            return h

    def cros(self, line):
        if line.b == 0:
            x = -line.c / line.a
            if (x - self.x) ** 2 == self.r ** 2:
                return [Point(x, self.y)]
            elif (x - self.x) ** 2 < self.r ** 2:
                yr = self.r ** 2 - (self.x - x) ** 2
                yr = math.sqrt(yr)
                return [Point(x, self.y + yr), Point(x, y - yr)]
            else:
                return []
        k = -line.a / line.b
        b = -line.c / line.b
        b += k * self.x - self.y
        d = (2 * k * b) ** 2 - 4 * (1 + k ** 2) * (b ** 2 - self.r ** 2)
        if d < 0:
            return []
        elif d == 0:
            x = -2 * k * b / (2 + 2 * k ** 2)
            x += self.x
            return [Point(x, line.y(x))]
        elif d > 0:
            d = math.sqrt(d)
            xl = [(-2 * k * b + d) / (2 + 2 * k * k), (-2 * k * b - d) / (2 + 2 * k * k)]
            for i in range(len(xl)):
                xl[i] += self.x
                xl[i] = Point(xl[i], line.y(xl[i]))
            return xl


    def engl(self, p, c=True):
        s = p.dist(Point(self.x, self.y))
        if c:
            return 2 * math.asin(self.r / s)
        else:
            return math.asin(self.r / s)

    def round(self, p, a):
        return Point(p.x * math.cos(a) - p.y * math.sin(a), p.x * math.sin(a) + p.y * math.cos(a))

    def round_line(self, line, fi):
        a = line.a * math.cos(fi) - line.b * math.sin(fi)
        b = line.a * math.sin(fi) + line.b * math.cos(fi)
        c = line.c
        return Line(a, b, c)

    def cross_line(self, p):
        if (p.x - self.x) ** 2 + (p.y - self.y) ** 2 > self.r ** 2:
            t = p.dist(self.x, self.y)
            if p.y - self.y < 0:
                fi = math.acos((p.x - self.x) / t)
            else:
                fi = -math.acos((p.x - self.x) / t)
            xn = self.r ** 2 / t
            yn = (self.r * math.sqrt(t ** 2 - self.r ** 2)) / t
            cos = math.cos(fi)
            sin = math.sin(fi)
            return [Point(xn * cos + yn * sin + self.x, yn * cos - xn * sin + self.y),
                    Point(xn * cos - yn * sin + self.x, -yn * cos - xn * sin + self.y)]
        if (p.x - self.x) ** 2 + (p.y - self.y) ** 2 == self.r ** 2:
            return [p]
        else:
            return []

    def dug(self, p1, p2):
        if self.r == 0:
            return 0
        p = Point(self.x, self.y)
        v1 = Vector(p, p1)
        v2 = Vector(p, p2)
        a = math.acos(v1 * v2 / (v1.dist() * v2.dist()))
        return a * self.r

    def ci(self, other):
        if self.x == other.x and self.y == other.y:
            if self.r == other.r:
                return [0, 0, 0]
            else:
                return []
        else:
            if Vector(self.x, self.y).sq_dist(Vector(other.x, other.y)) ** 2 < (self.r - other.r) ** 2:
                pass
            elif Vector(self.x, self.y).sq_dist(Vector(other.x, other.y)) ** 2 == (self.r - other.r) ** 2:
                pass
            elif Vector(self.x, self.y).sq_dist(Vector(other.x, other.y)) ** 2 == (self.r + other.r) ** 2:
                return []
            elif Vector(self.x, self.y).sq_dist(Vector(other.x, other.y)) ** 2 > (self.r + other.r) ** 2:
                return []
            else:
                return []

    def cross_circlee(self, other):
        if self.x == other.x and self.y == other.y:
            if self.r == other.r:
                return [0, 0, 0]
            else:
                return []
        else:
            t = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
            if other.y - self.y < 0:
                fi = math.acos((other.x - self.x) / t)
            elif other.y - self.y >= 0:
                fi = -math.acos((other.x - self.x) / t)
            if self.r ** 2 - other.r ** 2 + t ** 2 < 0:
                return []
            elif self.r ** 2 - other.r ** 2 + t ** 2 == 0:
                return [Point(self.r * math.cos(fi) + self.x, -self.r * math.sin(fi) + self.y)]
            elif self.r ** 2 - other.r ** 2 + t ** 2 > 0:
                xn = (self.r ** 2 - other.r ** 2 + t ** 2) / (2 * t)
                if self.r ** 2 - xn ** 2 < 0:
                    return []
                elif self.r ** 2 - xn ** 2 == 0:
                    return [Point(self.r * math.cos(fi) + self.x, -self.r * math.sin(fi) + self.y)]
                yn = math.sqrt(self.r ** 2 - xn ** 2)
                p1 = Point(xn * math.cos(fi) + yn * math.sin(fi) + self.x,
                           -xn * math.sin(fi) + yn * math.cos(fi) + self.y)
                p2 = Point(xn * math.cos(fi) - yn * math.sin(fi) + self.x,
                           -xn * math.sin(fi) - yn * math.cos(fi) + self.y)
                return [p1, p2]

    def in_to(self, p, eps=0):
        try:
            return (self.r - eps) ** 2 <= abs((self.x - p.x) ** 2 + (self.y - p.y) ** 2 <= (self.r + eps) ** 2)
        except:
            return False

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.r)


def round_n(x, n):
    x = round(x, n)
    x = str(x)
    x = x.split('.')
    x[1] += '0' * n
    x[1] = x[1][0: n]
    x = '.'.join(x)
    return x


def f(a, b, pos):
    return min(a.x, b.x) <= pos.x and pos.x <= max(a.x, b.x) and min(a.y, b.y) <= pos.y and pos.y <= max(a.y, b.y)


class Triangle:
    def __init__(self, a, b, c):
        self.p = [a, b, c]

    def bisector(self, i):
        i -= 1
        o, a, b = self.p[i], self.p[(i - 1) % 3], self.p[(i + 1) % 3]
        oa = Vector(o, a)
        ob = Vector(o, b)
        c = oa.mul(1 / oa.dist())
        d = ob.mul(1 / ob.dist())
        e = c + d
        return Line(e.y, -e.x, o.y * e.x - o.x * e.y)

    def mid_cross(self):
        a, b, c = self.p[0], self.p[1], self.p[2]
        mab = Point((a.x + b.x) / 2, (a.y + b.y) / 2)
        mbc = Point((b.x + c.x) / 2, (b.y + c.y) / 2)
        l1 = Line(c, mab)
        l2 = Line(a, mbc)
        return l1.cross(l2)[0]

    def mid_bisector(self):
        l1 = self.bisector(1)
        l2 = self.bisector(2)
        return l1.cross(l2)[0]

    def mid_h(self):
        a, b, c = self.p[0], self.p[1], self.p[2]
        l1 = Line(a, b).perpendicular(c)
        l2 = Line(b, c).perpendicular(a)
        return l1.cross(l2)[0]

    def midper(self):
        a, b, c = self.p[0], self.p[1], self.p[2]
        mab = Point((a.x + b.x) / 2, (a.y + b.y) / 2)
        mbc = Point((b.x + c.x) / 2, (b.y + c.y) / 2)
        l1 = Line(a, b).perpendicular(mab)
        l2 = Line(b, c).perpendicular(mbc)
        return l1.cross(l2)[0]

    def radius(self):
        return Line(self.p[0], self.p[1]).h(self.mid_bisector())

    def op_radius(self):
        return self.midper().dist(self.p[0].x, self.p[0].y)

    def in_v(self, o, a, b, p):
        oa = Vector(o, a)
        ob = Vector(o, b)
        op = Vector(o, p)
        return (oa ^ op) * (op ^ ob) >= 0

    def in_to(self, point, eps):
        try:
            for i in range(len(self.p)):
                if self.in_v(self.p[i], self.p[(i - 1) % len(self.p)], self.p[(i + 1) % len(self.p)], point):
                    pass
                else:
                    return False
            return True
        except:
            return False

    def min_circle(self):
        pc = self.midper()
        r = self.op_radius()
        for i in range(len(self.p)):
            a = Vector(self.p[i], self.p[(i - 1) % 3])
            b = Vector(self.p[i], self.p[(i + 1) % 3])
            if a * b < 0:
                pc = Point((self.p[(i - 1) % 3].x + self.p[(i + 1) % 3].x) / 2, (self.p[(i - 1) % 3].y + self.p[(i + 1) % 3].y) / 2)
                r = self.p[(i - 1) % 3].dist(self.p[(i + 1) % 3]) / 2
        return Circle(pc.x, pc.y, r)

    def oc(self):
        pc = self.midper()
        r = self.op_radius()
        return Circle(pc.x, pc.y, r)

    def vc(self):
        pc = self.mid_bisector()
        r = self.radius()
        return Circle(pc.x, pc.y, r)