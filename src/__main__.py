import wx
from src.mainwindow import MainWindow

if __name__ == '__main__':
    app = wx.App()
    frm = MainWindow()
    frm.Show()
    app.MainLoop()