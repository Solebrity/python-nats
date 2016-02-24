from setuptools import setup
from nats.io.client import __version__

setup(
  name='nats-client3',
  version=__version__,
  description='NATS client for Python 3',
  long_description='Python 3 client for NATS, a lightweight, high-performance cloud native messaging system',
  url='https://github.com/solebrity/python-nats',
  author='Waldemar Quevedo',
  author_email='wally@apcera.com',
  license='MIT License',
  packages=['nats', 'nats.io', 'nats.protocol'],
  install_requires=[
    'tornado',
  ],
  zip_safe=True,
)
