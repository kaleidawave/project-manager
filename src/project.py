import wx
import os
from src.files import CreateProject
import src.constants as CONSTANTS

class NewProjectWindow(wx.Frame):
    Name = "New Project"

    def __init__(self, parent):
        wx.Frame.__init__(self, None, title=self.Name)
        self.SetMinSize((365, 202))

        self.Panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Name
        vbox.Add(wx.StaticText(self.Panel, 1, "Project Name:"), 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        self.NameInput = wx.TextCtrl(self.Panel, 1)
        vbox.Add(self.NameInput, 0, wx.EXPAND | wx.ALL, 10)

        # Git
        GitBox = wx.BoxSizer()
        GitBox.Add(wx.StaticText(self.Panel, 1, "Create Git Repo:"), 1, wx.LEFT, 10)
        self.GitOption = wx.CheckBox(self.Panel, 1)
        GitBox.Add(self.GitOption, 0, wx.LEFT, 10)
        vbox.Add(GitBox)

        # Create Button
        CreateButton = wx.Button(self.Panel, 1, 'Create Project')
        CreateButton.Bind(wx.EVT_BUTTON, self.CreateProject)
        vbox.Add(CreateButton, 0, wx.EXPAND | wx.ALL, 10)

        self.Panel.SetSizer(vbox)
        self.SetIcon(wx.Icon(CONSTANTS.APPICON))

    def CreateProject(self, event):
        directory = CreateProject(self.NameInput.Value, self.GitOption.Value)
        wx.MessageBox('Created Project')
        os.startfile(directory)
        print(self.GetSize())
        self.Close()