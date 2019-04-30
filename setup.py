#!/usr/bin/env python3
from distutils.core import setup

setup(name='beamin_target',
      version='0.1.0',
      description='Beamin info-beamer target',
      author='Louis Simons',
      author_email='lousimons@gmail.com',
      packages=['beamin_target'],
      install_requires=[
          'flask',
      ],
      entry_points = {
        'console_scripts': ['beamin_target=beamin_target.server:main']
      }
      )
