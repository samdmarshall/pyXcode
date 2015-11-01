import os
import sys

# importing the pbProj module
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pbProj'))
from pbProj import pbProj

# importing the xcscheme module
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pyxcscheme'))
from pyxcscheme import xcscheme


from Helpers import Logger

class xcodeproj(object):
    
    def __init__(self, xcodeproj_file_path):
        if os.path.exists(xcodeproj_file_path):
            if xcodeproj_file_path.endswith(('.xcodeproj', '.pbproj')):
                self.filePath = xcodeproj_file_path
                
                # loading the pbxproj
                pbxproj_file_path = os.path.join(self.filePath, 'project.pbxproj')
                if os.path.exists(pbxproj_file_path):
                    self.projectFile = pbProj.PBXProj(pbxproj_file_path)
                else:
                    Logger.write().error('Could not find the pbxproj file!')
                
                # load schemes
                self.schemes = xcscheme.LoadSchemes(xcodeproj_file_path)
                
            else:
                Logger.write().error('Not a Xcode project file!')
        else:
            Logger.write().error('Could not find the Xcode project file!')
    