import numpy
import wx
import logging
from MyFrame import MyFrame


class MainFrame(MyFrame):
    def __init__(self, *args, **kwargs):
        MyFrame.__init__(self, *args, **kwargs)
        self.status = False
        self.cells = []

    def init_grid(self, event):
        num = int(self.num_of_lines.GetValue())
        if not self.status:
            self.status = True
            self.create_grid(num)
        logging.warning(num)

    def create_grid(self, count):
        for x in range(0, count):
            self.cells.append([])
            for y in range(0, count+1):
                element = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
                self.gbSizer1.Add(element, wx.GBPosition(1 + x, 1 + y), wx.GBSpan(1, 1), wx.ALL, 5)
                self.cells[x].append(element)
        self.Layout()

    def solve(self, event):
        self.popUp()
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
        pass

    def popUp(self):
        wx.MessageDialog(self, 'fuck you', 'you too', wx.OK | wx.ICON_INFORMATION)

app = wx.App()
frame = MainFrame(None)
frame.Show()
app.MainLoop()

# TODO: autosizing
# TODO: validation of user input
# TODO: logging to file
# TODO: tests