import os
import json
import subprocess
import src.constants as CONSTANTS
from src.settings import LoadSettings

def CreateProject(name, git):
    """ Creates a new project """
    settings = LoadSettings()
    directory = os.path.join(settings['project-dir'], name)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        with open(os.path.join(directory, 'README.md'), 'w') as ReadmeFile:
            ReadmeFile.write('# {}'.format(name))  

    if git:
        CreateGitRepo(directory)

    projects = LoadProjects()
    with open('track.json', 'w') as TrackFile:
        projects['projects'].append({'name': name, 'dir': directory})
        projects['num'] += 1
        with open('track.json', 'w') as TrackFile:
            json.dump(projects, TrackFile)  

    return directory
    

def LoadProjects():
    """ Loads current projects from tracking file"""
    try:
        with open('track.json', 'r') as TrackFile:
            return json.load(TrackFile)
    except FileNotFoundError as identifier:
        return CONSTANTS.DEFAULT_TRACK

def CreateGitRepo(directory):
    git = subprocess.Popen(['git', 'init'], cwd=directory)
    git.wait()
