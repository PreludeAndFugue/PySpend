#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup
#from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    # py2exe
    #windows=['pyspend.py'],

    #cx_Freeze
    #executables=[Executable('pyspend/pyspend.py', base=base)],
    #build_options = {}

    name='PySpend',
    version='0.1',
    author='Gary Kerr',
    author_email='gdrummondk@gmail.com',
    packages=['pyspend', 'pyspend.test'],
    package_data={'pyspend': ['config.json', 'pyspend.pyw']},
    license='LICENSE.txt',
    description='Record your expenditure',
    long_description=open('README.txt').read(),
    classifiers=[
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)

