#!/usr/bin/python

import MyFrame
import loadshedding
import wx
import datetime
# import requests.exceptions as ex


def changeShow(frame, group, loadshedding_data):
    dataa = loadshedding_data.getDatFile(group)
    iliness = dataa.split('\n')
    for ii in range(3, 10):
        ilinesss = iliness[ii].split(' ')
        ilinesss = ilinesss[1].split(',')
        frame.m_grid1.SetCellValue(ii - 3, 0, ilinesss[0])
        frame.m_grid1.SetCellValue(ii - 3, 1, ilinesss[1])


def choice_changed(event):
    global frame, loadshedding_data
    grpp = frame.m_choice5.GetSelection()
    grpp += 1
    changeShow(frame, grpp, loadshedding_data)
    dictii = loadshedding_data.dicti
    dictii["group"] = str(grpp)
    dictii["data"] = loadshedding_data.getDatFile(grpp)
    loadshedding_data.update_dicti(dictii)
    loadshedding_data.dicti = dictii


def refreshData(event):
    global loadshedding_data, frame
    try:
        loadshedding_data.refresh_data(loadshedding_data.dicti)
        changeShow(frame, loadshedding_data.dicti['group'], loadshedding_data)
        wx.MessageBox(
            "Data up to date now.",
            "Refresh Completed"
        )

    except:
        wx.MessageBox(
            "Sorry ! Cannot connect the server to update \
             the data.May be your Network is not helping us much.\n",
            "Connection Failed")


if __name__ == '__main__':
    loadshedding_data = loadshedding.loadsheddingData()
    dicti = loadshedding_data.dicti
    grpp = int(dicti["group"])
    data = dicti["data"]
    latest = dicti["latest"][:10]
    app = wx.App(False)
    frame = MyFrame.MyFrame(parent=None)
    frame.m_staticText23.SetLabelText("Last updated at " + latest)
    frame.m_choice5.SetSelection(grpp - 1)
    changeShow(frame, grpp, loadshedding_data)
    wkDay = (datetime.datetime.today().weekday() + 2) % 7
    if wkDay == 0:
        wkDay = 7
    frame.m_grid1.SelectRow(wkDay-1)

    # Connect Events
    frame.m_choice5.Bind(wx.EVT_CHOICE, choice_changed)
    frame.m_button2.Bind(wx.EVT_BUTTON, refreshData)

    frame.Show()
    app.MainLoop()
