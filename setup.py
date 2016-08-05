from setuptools import setup

setup(name='awstools',
      version='1.0',
      py_modules=['awstools'],
      entry_points={
        'console_scripts': [
            'awsls = awstools:awsls',
            'awscp = awstools:awscp',
            'awsvim = awstools:awsvim',
        ],
      },
)