import os
import random
from copy import copy

# класс истории изменений
class His:

    def __init__(self):
        os.mkdir(str(random.randint(1, 10000000)), mode=0o777, *, dir_fd=None)

        self.alls = []
        self.index = 0

    def __len__(self):
        return len(self.alls)

    def append(self, all):
        self.index = self.__len__()
        self.alls = copy(self.alls) + [(copy(all))]


    def get(self):
        # self.alls[self.index] = All()
        return copy(self.alls[self.index])

    def rs(self):
        if self.index > 0:
            self.index -= 1

    def ss(self):
        if self.index < self.__len__() - 1:
            self.index += 1

    def __str__(self):
        for i in self.alls:
            print(i.__len__())
        return str(len(self.alls))
