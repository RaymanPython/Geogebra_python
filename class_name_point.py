

class Name_Point:

    def __init__(self):
        self.s = 'ABCDEFGHKLMOPRSTUHJIQWZVY'
        self.names = []
        self.k = 0
        self.names_dict = dict()
        for i in self.s:
            self.names_dict[i] = -1

    def append(self):
        self.k %= len(self.s)
        try:
            self.names_dict[self.s[self.k]] += 1
            if self.names_dict[self.s[self.k]] == 0:
                self.k += 1
                return self.s[self.k - 1]
            else:
                self.k += 1
                return self.s[self.k - 1] + ' ' + str(self.names_dict[self.s[self.k - 1]] )
        except:
            self.k += 1
            return self.s[self.k - 1]