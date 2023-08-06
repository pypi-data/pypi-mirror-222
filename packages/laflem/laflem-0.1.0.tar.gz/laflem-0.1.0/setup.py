#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def get_version():
  """Get version from __init__.py file."""
  filename = os.path.join(os.path.dirname(__file__), 'lib', 'flem', '__init__.py')
  with open(filename) as f:
    for line in f:
      if line.startswith('__version__'):
        return eval(line.split('=')[-1])
      
  raise ValueError(f"No __version__ defined in {filename}")

setup(
  name='laflem',
  version=get_version(),
  description='Tools collection',
  long_description=open('README.md').read(),
  author='Guillaume MARTINEZ',
  author_email='lunik@tiwabbit.fr',
  maintainer='Guillaume MARTINEZ',
  maintainer_email='lunik@tiwabbit.fr',
  url='https://tobedefined.tiwabbit.fr',
  download_url='https://tobedefined.tiwabbit.fr',
  license_files = ('LICENSE',),
  package_dir={'': 'lib'},
  packages=find_packages(where='lib'),
  include_package_data=True,
  data_files=[
    ('configs/flem', [os.path.join(root, file) for root, _, files in os.walk('configs') for file in files]),
  ],
  scripts=['scripts/flem'],
  python_requires=">=3.8.0",
  install_requires = [
    "rich==13.*",
  ],
  extras_require={
    'dev': [
      'pylint',
      'twine',
    ]
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)