import wx
import json
import src.constants as CONSTANTS

class SettingsWindow(wx.Frame):
    Name = "Settings"
    Settings = None

    def __init__(self, parent):
        wx.Frame.__init__(self, None, title=self.Name)
        self.SetMinSize((290, 242))

        self.Settings = LoadSettings()

        self.Panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Projects Folder
        vbox.Add(wx.StaticText(self.Panel, 1, 'Projects Folder: '), 0, wx.EXPAND | wx.ALL, 10)
        self.ProjectsFolderLabel = wx.StaticText(self.Panel, 1, self.Settings['project-dir']) 
        vbox.Add(self.ProjectsFolderLabel, 0, wx.EXPAND | wx.ALL, 10)
        SelectProjectButton = wx.Button(self.Panel, 1, 'Open')
        SelectProjectButton.Bind(wx.EVT_BUTTON, self.SelectFolderDialog)
        vbox.Add(SelectProjectButton, 0, wx.EXPAND | wx.ALL, 10)

        # Save Button
        SaveButton = wx.Button(self.Panel, 1, 'Save')
        SaveButton.Bind(wx.EVT_BUTTON, self.SaveSettings)
        vbox.Add(SaveButton, 0, wx.EXPAND | wx.ALL, 10)

        self.Panel.SetSizer(vbox)
        self.SetIcon(wx.Icon(CONSTANTS.APPICON))

    def SaveSettings(self, event):
        SaveSettings(self.Settings)
        wx.MessageBox('Saved Settings')
        print(self.GetSize())
        self.Close()
        
    def SelectFolderDialog(self, event):
        """Opens dialog to choose projects folder"""
        with wx.DirDialog(self, "Choose projects folder:", self.Settings['project-dir']) as DirectoryDialog:
            if DirectoryDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                self.Settings['project-dir'] = DirectoryDialog.GetPath()
                self.ProjectsFolderLabel.SetLabel(self.Settings['project-dir'])

def SaveSettings(settings):
    """Save settings"""
    newsettings = CONSTANTS.DEFAULT_SETTINGS.copy()
    newsettings.update(settings)
    with open('settings.json', 'w') as SettingsFile:
        json.dump(newsettings, SettingsFile)

def LoadSettings():
    """Loads settings"""
    try:
        with open('settings.json', 'r') as SettingsFile:
            return json.load(SettingsFile)
    except FileNotFoundError as identifier:
        return CONSTANTS.DEFAULT_SETTINGS
    