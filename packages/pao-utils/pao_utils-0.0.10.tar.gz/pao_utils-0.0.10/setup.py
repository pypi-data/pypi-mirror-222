from setuptools import setup, find_packages
import codecs
import os

 
DESCRIPTION = 'Plotting Package'
LONG_DESCRIPTION_PATH  = "C:/Users/gsppp/OneDrive/Desktop/data_science_utils_folder/README.rst"
with open(LONG_DESCRIPTION_PATH, "r") as f :
    LONG_DESCRIPTION = f.read()

#print(LONG_DESCRIPTION)

# Setting up
setup(
    name                            = "pao_utils",
    version                         = '0.0.10',
    author                          = "pao_800a (Giuseppe Paonessa)",
    author_email                    = "<ggpaonessa@gmail.com>",
    description                     = DESCRIPTION,
    long_description                = LONG_DESCRIPTION,
    long_description_content_type   = "text/x-rst",
    package_dir                     = {"" : "app"},
    packages                        = find_packages(where = "pao_utils"),
    license                         = "MIT",
    url                             = "https://github.com/pao800a/data_science_utils_folder",
    keywords                        = ['python'],
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires                 = ">=3.11",
)
