import os
import random
from copy import copy
import Data_save
import ALL_object
from Draw_object import *
# класс истории изменений
class His:

    def __init__(self):
        self.puth = 'dir' + str(random.randint(1, 10000000))
        os.mkdir(self.puth, mode=0o777, dir_fd=None)

        self.alls = []
        self.index = 0

    def __len__(self):
        return len(self.alls)

    def new(self, all):
        name = self.puth + '/his' + str(self.__len__())
        f = open(name, 'w')
        Data_save.save_all(all, f)
        return name

    def append(self, all):
        if self.__len__() > self.index + 1:
            for i in range(self.index + 1, self.__len__()):
                self.alls.pop(self.index + 1)
        self.index = self.__len__()
        self.alls.append(self.new(all))


    def get(self):
        # self.alls[self.index] = All()
        all = ALL_object.All()

        name = self.puth + '/his' + str(self.index)
        now_file = open(name, 'r')
        if now_file:
            s = now_file.readlines()
            now_file.close()
        for i in s:
            try:
                eval(i)
            except:
                pas
        print(all)
        return all

    def rs(self):
        if self.index > 0:
            self.index -= 1

    def ss(self):
        if self.index < self.__len__() - 1:
            self.index += 1

    def __str__(self):
        for i in self.alls:
            print(i)
        return str(len(self.alls))
