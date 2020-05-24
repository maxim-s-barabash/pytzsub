'''
pytzsub setup script
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pytzsub, sys, os, os.path

me = 'Barabash Maxim'
memail = 'maxim.s.barabash@gmail.com'
ldesc = '''\
World timezone definitions by country subdivision (e.g., provinces or states)
'''

packages = ['pytzsub']

setup (
    name='pytzsub',
    version=pytzsub.VERSION,
    zip_safe=True,
    description='World timezone definitions by country Subdivision (e.g., provinces or states)',
    long_description=ldesc,
    author=me,
    author_email=memail,
    maintainer=me,
    maintainer_email=memail,
    url='https://github.com/maxim-s-barabash/pytzsub',
    license=open('LICENSE','r').read(),
    keywords=['timezone','tzinfo', 'datetime', 'olson', 'time'],
    packages=packages,
    package_data={'pytz': ['zone-sub.tab']},
#    download_url='http://',
    platforms=['Independant'],
    include_package_data=True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
