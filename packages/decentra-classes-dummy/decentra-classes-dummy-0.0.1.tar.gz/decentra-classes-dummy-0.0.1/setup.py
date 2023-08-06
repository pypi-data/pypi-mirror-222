from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'All Source code of the Python Course from DecentrCalasses.'
LONG_DESCRIPTION = 'This module will help you to access all the codes done in the tutorials of the Python Course from DecentrCalasses.'

# Setting up
setup(
    name="decentra-classes-dummy",
    version=VERSION,
    author="Atharva Akshat (Decentraclasses)",
    author_email="<helloatharvaakshat@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'tutorial', 'learn', 'code', 'experiment'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)