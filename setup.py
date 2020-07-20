"""pytzsub setup script."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
from os import path

__version__ = None
NAME = "pytzsub"
ME = "Barabash Maxim"
ME_MAIL = "maxim.s.barabash@gmail.com"
PACKAGES = ["pytzsub"]
PWD = path.abspath(path.dirname(__file__))

with open(path.join(PWD, "README.md"), encoding="utf-8") as fileptr:
    long_description = fileptr.read()

with open(path.join(PWD, NAME, "_version.py")) as fileptr:
    exec(fileptr.read())


setup(
    name="pytzsub",
    version=__version__,
    zip_safe=True,
    description=(
        "World timezone definitions by country Subdivision "
        "(e.g., provinces or states)"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=ME,
    author_email=ME_MAIL,
    maintainer=ME,
    maintainer_email=ME_MAIL,
    url="https://github.com/maxim-s-barabash/pytzsub",
    project_urls={
        "Source": "https://github.com/maxim-s-barabash/pytzsub",
        "Tracker": "https://github.com/maxim-s-barabash/pytzsub/issues",
    },
    license="MIT License",
    keywords=["timezone", "tzinfo", "datetime", "pytz", "time"],
    packages=PACKAGES,
    package_data={"pytzsub": ["zone-sub.tab"]},
    platforms=["Independent"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
