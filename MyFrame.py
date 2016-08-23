# -*- coding: utf-8 -*- 

"""

 Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
## PLEASE DO "NOT" EDIT THIS FILE!
"""
import wx
import wx.xrc
import wx.grid


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Loadshedding", pos=wx.DefaultPosition,
                          size=wx.Size(300, 500),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Loadshedding App By Amrit Ghimire"), wx.VERTICAL)

        m_choice5Choices = [u"Group 1", u"Group 2", u"Group 3", u"Group 4", u"Group 5", u"Group 6", u"Group 7"]
        self.m_choice5 = wx.Choice(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice5Choices, 0)
        self.m_choice5.SetSelection(6)
        sbSizer1.Add(self.m_choice5, 0, wx.ALL, 5)

        self.m_grid1 = wx.grid.Grid(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(7, 2)
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelValue(0, u"Morning")
        self.m_grid1.SetColLabelValue(1, u"Evening")
        self.m_grid1.SetColLabelValue(2, wx.EmptyString)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelValue(0, u"Sunday")
        self.m_grid1.SetRowLabelValue(1, u"Monday")
        self.m_grid1.SetRowLabelValue(2, u"Tuesday")
        self.m_grid1.SetRowLabelValue(3, u"WednesDay")
        self.m_grid1.SetRowLabelValue(4, u"Thursday")
        self.m_grid1.SetRowLabelValue(5, u"Friday")
        self.m_grid1.SetRowLabelValue(6, u"Saturday")
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sbSizer1.Add(self.m_grid1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Refresh Data", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        sbSizer1.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticText23 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Last Updated at", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        sbSizer1.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(sbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
