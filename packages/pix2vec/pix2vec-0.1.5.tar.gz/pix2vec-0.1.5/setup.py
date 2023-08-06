#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Alessandro Frigeri",
    author_email='alessandro.frigeri@inaf.it',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
	'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="pix2vec produces a vector representation of planetary mapping spectrometers hyperspectral and camera ISIS data cube",
    entry_points={
        'console_scripts': [
            'pix2vec=pix2vec.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords='pix2vec',
    name='pix2vec',
    packages=find_packages(include=['pix2vec', 'pix2vec.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/afrigeri/pix2vec',
    version='0.1.5',
    zip_safe=False,
)
