from setuptools import setup

setup(name='luigi_tree',
      description='Create Pascal\'s triangle like trees in Luigi.',
      version='0.1',
      package_dir={'':'src'},
      packages=['luigi_tree'],
      test_suite='test',
      tests_require=[
          'mock',
      ],
      install_requires=[
          'luigi',
      ],
      entry_points={
          'console_scripts': [
              'luigi_tree = luigi_tree.cli:main',
          ],
      },
      zip_safe=False)

