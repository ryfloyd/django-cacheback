#!/usr/bin/env python

from setuptools import setup, find_packages
import os
from cacheback import __version__

PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
os.chdir(PACKAGE_DIR)


setup(
    name='django-cacheback',
    version=__version__,
    url='https://github.com/codeinthehole/django-cacheback',
    author="David Winterbottom",
    author_email="david.winterbottom@gmail.com",
    description=("Caching library for Django that uses Celery "
                 "to refresh cache items asynchronously"),
    long_description=open(os.path.join(PACKAGE_DIR, 'README.rst')).read(),
    license='MIT',
    packages=find_packages(exclude=["sandbox*", "tests*"]),
    include_package_data=True,
    install_requires=[
        'django>=1.3',
        'celery',
        'six',
        'cache-tagging==0.7.7.11'
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
