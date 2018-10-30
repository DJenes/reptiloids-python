import numpy
import wx
import logging
from MyFrame import MyFrame


class MainFrame(MyFrame):
    def __init__(self, *args, **kwargs):
        MyFrame.__init__(self, *args, **kwargs)
        self.status = False
        self.cells = []

    # create grid for numpy
    def init_grid(self, event):
        try:
            num = int(self.num_of_lines.GetValue())
        except ValueError:
            self.pop_up('Число, где тварь?!')
            return False
        if not self.status:
            self.status = True
            self.create_grid(num)
        logging.warning(num)

    # x - rows
    # y - cols + one additional for numpy
    def create_grid(self, count):
        self.auto_size()
        for x in range(0, count):
            self.cells.append([])
            for y in range(0, count + 1):
                element = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(35, -1), 0)
                element.SetMaxLength(2)
                self.gbSizer1.Add(element, wx.GBPosition(1 + x, 1 + y), wx.GBSpan(1, 1), wx.ALL, 5)
                self.cells[x].append(element)
        self.Layout()

    def solve(self, event):
        if self.validate_grid():
            v1 = [float(self.cells[x][-1].GetValue()) for x in range(0, len(self.cells))]
            m1 = []
            for x in range(0, len(self.cells)):
                m1.append([])
                for y in range(0, len(self.cells)):
                    m1[x].append(float(self.cells[x][y].GetValue()))
            answer = numpy.linalg.solve(m1, v1)
            logging.warning(v1)
            logging.warning(m1)
            logging.warning(answer)

    def validate_grid(self):
        for x in range(0, len(self.cells)):
            for y in range(0, len(self.cells) + 1):
                try:
                    int(self.cells[x][y].GetValue())
                except ValueError:
                    self.pop_up('Снова выходишь на связь, Ебанашка? Где число?!!')
                    return False
        return True

    def pop_up(self, message):
        dial = wx.MessageDialog(None, message, 'Ошибка валидации', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()

    def clear(self, event):
        self.auto_size()
        if self.status:
            self.status = False
            for x in range(0, len(self.cells)):
                for y in range(0, len(self.cells) + 1):
                    self.cells[x][y].Destroy()
            self.cells = []

    def auto_size(self):
        width = 500
        height = 100
        if len(self.cells) > 4:
            height = 100 + (len(self.cells) - 4) * 20
        self.SetSize(wx.Size(width, height))


app = wx.App()
frame = MainFrame(None)
frame.Show()
app.MainLoop()

# TODO: autosizing
# TODO: logging to file
# TODO: tests
# TODO: fix prospector
# TODO: windows for answer
