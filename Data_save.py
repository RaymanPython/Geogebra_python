import tkinter.filedialog as fd
import tkinter

TYPE_GEO_PY = '.geopy'
filetypes = ("Геогебра обьект", TYPE_GEO_PY),

def save_all(all, new_file):
    if new_file == None:
        return

    for i in all.point:
        if i.save:
            new_file.write(f'all.add_point({str(i)})' + '\n')
            arg = i.__dict__
            # print(type(i).__getnewargs__())
            for j in arg:
                new_file.write(f'all.point[-1].__setattr__("{j}", {arg[j]})' + '\n')
    for i in all.all_sprites:
        if i.save:
            new_file.write(f'all.add_object({str(i)})' + '\n')
            arg = i.__dict__
            # print(i.__getinitargs__())
            for j in arg:
                new_file.write(f'all.all_sprites[-1].__setattr__("{j}", {arg[j]})' + '\n')

    new_file.close()


def save(all):
    tkinter.Tk().withdraw()
    new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=TYPE_GEO_PY,
                                filetypes=(filetypes))
    save_all(all, new_file)

def open():
    tkinter.Tk().withdraw()
    my_file = fd.askopenfile(title="Открыть файл", filetypes=filetypes)
    s = ''
    if my_file:
        s = my_file.readlines()
        my_file.close()
    return s
