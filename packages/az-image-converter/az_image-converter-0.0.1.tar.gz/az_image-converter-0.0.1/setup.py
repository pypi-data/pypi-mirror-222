from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Az Image Converter is a Python library that provides a simple and convenient way to convert images. A Library by Azeem Akhtar'
LONG_DESCRIPTION = 'Az Image Converter is a Python library that provides a simple and convenient way to convert images between different formats using the Pillow library.'

# Setting up
setup(
    name="az_image-converter",
    version=VERSION,
    author="Azeem Akhtar",
    author_email="hellomazeem@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    readme = "README.md",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pillow"],
    keywords=['Image', 'Image Converter', 'PNG TO JPG Converter', 'JPG TO PNG Converter', 'Azeem Akhtar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)