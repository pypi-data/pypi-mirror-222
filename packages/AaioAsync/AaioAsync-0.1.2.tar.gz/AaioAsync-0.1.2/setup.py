from setuptools import setup

version = '0.1.2'

setup(name='AaioAsync',
      version=version,

      author='Belyashik2K',
      author_email='lovelybelyashik@gmail.com',

      license='Apache License, Version 2.0',

      description='Fully async python wrapper for Aaio.io API',
      packages=['AaioAsync', 'AaioAsync/exceptions', 'AaioAsync/models'],
      install_requires=['certifi', 'aiohttp', 'pydantic'],
      zip_safe=False)
