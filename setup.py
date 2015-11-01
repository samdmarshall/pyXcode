from setuptools import setup

setup(
    name='pyXcode',
    version='0.1',
    description='Xcode Build System Library',
    url='https://github.com/samdmarshall/pyXcode',
    author='Samantha Marshall',
    author_email='me@samdmarshall.com',
    license='BSD 3-Clause',
    package_data = {
        'pyXcode/pyXCConfig/xcconfig': [
            '*.xcconfig',
        ],
    },
    packages=[
        'pyXcode',                                      # root module
        
        'pyXcode/Helpers',                              # helper module (contains small modules used often)
        'pyXcode/Helpers/pyLoggingHelper/Logger',       # logging utility
        'pyXcode/Helpers/pyxcrunHelper/xcrunHelper',    # collection of methods for accessing xcrun
        
        'pyXcode/pbProj/pbProj',                        # pbxproj parser
        'pyXcode/pbProj/pbProj/pbPlist/pbPlist',        # ascii plist parser
        
        'pyXcode/pyXCConfig/xcconfig',                  # xcconfig parser
        
        'pyXcode/pyxcscheme/pyxcscheme',                # xcscheme parser
        
        'pyXcode/pyxcwsdata/pyxcwsdata',                # xcworkspacedata parser
    ],
    zip_safe=False
)