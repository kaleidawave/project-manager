import wx
from src.settings import SettingsWindow
from src.project import NewProjectWindow
from src.files import LoadProjects
import src.constants as CONSTANTS

class MainWindow(wx.Frame):
    """Main App Window"""
    def __init__(self):
        wx.Frame.__init__(self, None, title=CONSTANTS.APPNAME)
        self.SetMinSize((600, 373))

        self.Panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        openproject = wx.Button(self.Panel, 1, 'New Project')
        openproject.Bind(wx.EVT_BUTTON, self.NewProject)
        vbox.Add(openproject, 0, wx.ALL, 20)

        self.List = wx.ListCtrl(self.Panel, 1, style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.LC_SINGLE_SEL)
        self.List.AppendColumn('Name', width=wx.LIST_AUTOSIZE)
        self.List.AppendColumn('Location', width=wx.LIST_AUTOSIZE)
        self.List.SetMaxSize((-1, 400))
        vbox.Add(self.List, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self.Panel.SetSizer(vbox)

        self.MakeMenuBar()
        self.DialogWindow = None;
        self.Bind(wx.EVT_CLOSE, self.Exit, self)
        self.SetIcon(wx.Icon(CONSTANTS.APPICON))
        
        self.LoadProjectsIntoTable()

    def MakeMenuBar(self):
        FileMenu = wx.Menu()

        SettingsItem = FileMenu.Append(-1, "&Settings...\tCtrl-Shift-S", "Application Settings")
        self.Bind(wx.EVT_MENU, self.ShowSettings, SettingsItem)

        MenuBar = wx.MenuBar()
        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

    def LoadProjectsIntoTable(self):
        self.projects = LoadProjects()['projects']
        for project in self.projects:
            self.List.Append(list(project.values()))

    def ShowSettings(self, event):
        """Shows settings window"""
        print(self.GetSize())
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