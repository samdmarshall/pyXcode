import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pyLoggingHelper'))
from Logger.Logger import Logger

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pyxcrunHelper'))
from xcrunHelper.xcrun import xcrun