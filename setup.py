#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("norm.norm",
                         ["norm/norm.pyx"],
                         extra_compile_args=[],
                         extra_link_args=[])]

from norm import __version__

sdict = {
    'name': 'norm',
    'cmdclass': {'build_ext': build_ext},
    'ext_modules': ext_modules,
    'version': __version__,
    'description': 'Easy peasy sql generation',
    'long_description': "Really easy SQL generation",
    'url': 'http://github.com/justinvanwinkle',
    'download_url': 'https://github.com/justinvanwinkle/Norm',
    'author': 'Justin Van Winkle',
    'author_email': 'justin.vanwinkle@gmail.com',
    'maintainer': 'Justin Van Winkle',
    'maintainer_email': 'justin.vanwinkle@gmail.com',
    'keywords': ['Norm', 'sql'],
    'license': 'BSD',
    'packages': ['norm'],
    #'test_suite' : 'tests.all_tests',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python']}

setup(**sdict)
