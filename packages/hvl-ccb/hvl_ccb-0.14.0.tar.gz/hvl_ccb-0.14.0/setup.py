#!/usr/bin/env python
#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""The setup script."""
import sys

from setuptools import find_packages, setup

# Note: compare only major and minor version numbers
python_min_version = (3, 9,)
python_max_version = (3, 10,)
python_version = sys.version_info[:2]
python_min_version_str = '.'.join(map(str, python_min_version))
python_max_version_str = '.'.join(map(str, python_max_version))
if python_version < python_min_version:
    import platform
    print(
        'ERROR: You are using Python {}; Python >={} is required.'.format(
            platform.python_version(),
            python_min_version_str,
        ),
    )
    sys.exit(-1)
if python_version > python_max_version:
    import platform
    print(
        'WARNING: You are using Python {}; Python <={} is officially supported.'.format(
            platform.python_version(),
            python_max_version_str,
        ),
    )

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('INSTALLATION.rst') as installation_file:
    installation = installation_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyserial>=3.5',
    'pymodbus>=3.1.1',
    'bitstring>=3.1.9',
    'pyvisa>=1.12.0',
    'pyvisa-py>=0.5.3',
    'typeguard>=3.0.0',
    'aenum>=3.1.11',
    'asyncua>=1.0.1',
    'numpy>=1.23.4'
]

tiepie = ['python-libtiepie==1.1.6']  # To be unfixed with stable version of libtiepie
labjack = ['labjack-ljm>=1.21.0']
picotech = ['PicoSDK==1.0']
all_libs = tiepie + labjack + picotech

extra_requirements = {
    'all': all_libs,
    'tiepie': tiepie,
    'labjack': labjack,
    'picotech': picotech,
}


dependency_links = []

setup(
    author=(
        'Mikołaj Rybiński, David Graber, Henrik Menne, Alise Chachereau, '
        'Henning Janssen, David Taylor, Joseph Engelbrecht, Chi-Ching Hsu'
    ),
    maintainer='Chi-Ching Hsu, Henning Janssen',
    maintainer_email='contact-project+ethz-hvl-hvl-ccb-15975897-issue-@incoming'
                     '.gitlab.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ] + [
        'Programming Language :: Python :: 3.{}'.format(i)
        for i in range(python_min_version[1], python_max_version[1] + 1)
    ],
    description=(
        'Python common code base to control devices high voltage research devices, in '
        'particular, as used in Christian Franck\'s High Voltage Lab (HVL), D-ITET, ETH'
    ),
    entry_points={},
    python_requires='>={}'.format(python_min_version_str),
    install_requires=requirements,
    extras_require=extra_requirements,
    dependency_links=dependency_links,
    license='GNU General Public License v3',
    long_description=readme + '\n\n' + installation + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='hvl_ccb',
    name='hvl_ccb',
    package_data={
        'hvl_ccb': ['py.typed'],
    },
    packages=find_packages(),
    test_suite='tests',
    url='https://gitlab.com/ethz_hvl/hvl_ccb/',
    version='0.14.0',
    zip_safe=False,
)
