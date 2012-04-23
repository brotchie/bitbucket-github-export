#!/usr/bin/env python

from setuptools import setup

setup(name='bitbucket-github-export',
    version='1.0',
    description='Exports bitbucket repositories to github.',
    author='James Brotchie',
    author_email='brotchie@gmail.com',
    url='https://github.com/brotchie/bitbucket-github-export',
    install_requires=['hg-git', 'Pygithub3', 'python-bitbucket'],
    dependency_links=['https://bitbucket.org/jmoiron/python-bitbucket/get/default.tar.bz2#egg=python-bitbucket'],
    py_modules=['bitbucket_github_export'],
    entry_points={
        'console_scripts' : [
            'bitbucket-github-export = bitbucket_github_export:main'
        ]
    }
)
