import xcodeproj
# import xcworkspace

xc = xcodeproj.xcodeproj('/Users/Samantha/Projects/pyXcode/test/workspace/ProjectWithBundleTarget/ProjectWithBundleTarget.xcodeproj')

print xc.projectFile.targets()