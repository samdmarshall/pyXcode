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
        'pyXcode',
        'pyXcode/Helpers',
        'pyXcode/Helpers/pyLoggingHelper/Logger',
        'pyXcode/Helpers/pyxcrunHelper/xcrunHelper',
        'pyXcode/pbProj/pbProj',
        'pyXcode/pbProj/pbProj/pbPlist/pbPlist',
        'pyXcode/pyXCConfig/xcconfig',
    ],
    zip_safe=False
)