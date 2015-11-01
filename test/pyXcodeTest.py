import os
import xml.etree.ElementTree as xml

workspace_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'workspace/pyXcodeTestWorkspace.xcworkspace/contents.xcworkspacedata')

contents = xml.parse(workspace_path)

print os.environ.get('DEVELOPER_DIR')
for child in contents.getroot():
    print child.tag
