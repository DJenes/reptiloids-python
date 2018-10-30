# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Решение системы линейных уравнений",
                          pos=wx.DefaultPosition, size=wx.Size(90, 210),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.gbSizer1 = wx.GridBagSizer(0, 0)
        self.gbSizer1.SetFlexibleDirection(wx.BOTH)
        self.gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.num_of_lines = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        self.num_of_lines.SetMaxLength(1)
        self.gbSizer1.Add(self.num_of_lines, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"N уравнений", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.gbSizer1.Add(self.m_staticText1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, 'Построить', wx.DefaultPosition, wx.Size(100, -1), 0)
        self.gbSizer1.Add(self.m_button2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, 'Решить', wx.DefaultPosition, wx.Size(100, -1), 0)
        self.gbSizer1.Add(self.m_button3, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, 'Очистить', wx.DefaultPosition, wx.Size(100, -1), 0)
        self.gbSizer1.Add(self.m_button4, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.SetSizer(self.gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.init_grid)
        self.m_button3.Bind(wx.EVT_BUTTON, self.solve)
        self.m_button4.Bind(wx.EVT_BUTTON, self.clear)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def init_grid(self, event):
        event.Skip()

    def solve(self, event):
        event.Skip()

    def clear(self, event):
        event.Skip()
