import wx
import os
from src.files import CreateProject
import src.constants as CONSTANTS

class NewProjectWindow(wx.Frame):
    Name = "New Project"

    def __init__(self, parent):
        wx.Frame.__init__(self, None, title=self.Name)
        self.SetMinSize((400,253))

        self.Panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Name
        vbox.Add(wx.StaticText(self.Panel, 1, "Project Name:"), 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        self.NameInput = wx.TextCtrl(self.Panel, 1)
        vbox.Add(self.NameInput, 0, wx.EXPAND | wx.ALL, 10)

        # Language
        vbox.Add(wx.StaticText(self.Panel, 1, "Project Language:"), 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        self.LanguageInput = wx.TextCtrl(self.Panel, 1)
        vbox.Add(self.LanguageInput, 0, wx.EXPAND | wx.ALL, 10)

        # Create Button
        CreateButton = wx.Button(self.Panel, 1, 'Create Project')
        CreateButton.Bind(wx.EVT_BUTTON, self.CreateProject)
        vbox.Add(CreateButton, 0, wx.EXPAND | wx.ALL, 10)

        self.Panel.SetSizer(vbox)
        self.SetIcon(wx.Icon(CONSTANTS.APPICON))

    def CreateProject(self, event):
        directory = CreateProject(self.NameInput.Value)
        wx.MessageBox('Created Project')
        os.startfile(directory)
        self.Close()