from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Fingerprint reader R503'
LONG_DESCRIPTION = 'A package that allows a computer to direct interface with GROW R503 finger print sensor without using external microcontroller'

# Setting up
setup(
    name="r503",
    version=VERSION,
    author="RoshanCS",
    author_email="<roshan.cs790@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyserial'],
    keywords=['python', 'fingerprint', 'security', 'grow', 'r503', 'password'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)