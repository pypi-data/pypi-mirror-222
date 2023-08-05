from setuptools import setup, find_packages

version = '0.0.1'
description = 'An open-source offline text-to-speech package for Santali language. Convert text to speech in male or female voice.'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

name = 'SantaliTTS'
author = 'Shivnath'
email = ''

with open('requirements.txt') as f:
    required = f.read().splitlines()



keywords = ['python','text to speech','santali text to speech', 'santali tts', 'offline santali tts', 'offline santali text to speech']

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Utilities',
    'Operating System :: OS Independent',
]

projects_links = {
    "Documentation": "",
    "Source": "",
    "Bug Tracker": "",
}

setup(
    name="santalitts",
    python_requires='>=3.10',
)