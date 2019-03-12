import wx
from src.settings import SettingsWindow
from src.project import NewProjectWindow
import src.constants as CONSTANTS

class MainWindow(wx.Frame):
    """Main App Window"""
    def __init__(self):
        wx.Frame.__init__(self, None, title=CONSTANTS.APPNAME)
        self.SetMinSize((356, 146))

        self.Panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        openproject = wx.Button(self.Panel, 1, 'New Project')
        openproject.Bind(wx.EVT_BUTTON, self.NewProject)
        vbox.Add(openproject, 0, wx.EXPAND | wx.ALL, 20)

        self.Panel.SetSizer(vbox)

        self.MakeMenuBar()
        self.DialogWindow = None;
        self.Bind(wx.EVT_CLOSE, self.Exit, self)
        self.SetIcon(wx.Icon(CONSTANTS.APPICON))


    def MakeMenuBar(self):
        FileMenu = wx.Menu()

        SettingsItem = FileMenu.Append(-1, "&Settings...\tCtrl-Shift-S", "Application Settings")
        self.Bind(wx.EVT_MENU, self.ShowSettings, SettingsItem)

        MenuBar = wx.MenuBar()
        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

    def ShowSettings(self, event):
        """Shows settings window"""
        self.DialogWindow = SettingsWindow(self)
        self.DialogWindow.Show()

    def NewProject(self, event):
        """Shows NewProject window"""
        self.DialogWindow = NewProjectWindow(self)
        self.DialogWindow.Show()

    def Exit(self, event):
        """Fires on window exit"""
        if self.DialogWindow: self.DialogWindow.Close(True)
        self.Destroy()