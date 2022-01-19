#!/usr/bin/env python

from setuptools import setup

gnitch_version="0.1"

gnitch_classifiers=[
    'Environment :: Console :: Curses',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python',
    'Topic :: Multimedia :: Video :: Display'
]

with open("README.md", "r") as fp:
    gnitch_long_description = fp.read()

setup(
    name="gnitch",
    author="3ship",
    author_email="",
    classifiers=gnitch_classifiers,
    description="TUI/CLI wrapper around streamlink for twitch.tv - forked from reflex-curses for the GNOME desktop",
    entry_points={
        'console_scripts': [
            'gnitch = gnitch.gnitch:main',
        ],},
    install_requires=["requests"],
    keywords="tui cli twitch streamlink",
    license="GPLv3",
    long_description=gnitch_long_description,
    long_description_content_type='text/markdown',
    packages=["gnitch"],
    python_requires=">=3.6",
    url="https://github.com/3ship/gnitch",
    version=gnitch_version,
    zip_safe=True
)
