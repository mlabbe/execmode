from setuptools import setup, find_packages

setup(
    name = 'execmode',
    version = '1.0',
    packages = find_packages(),

    package_data = {
        '': ['LICENSE', 'README.md'],
    },

    # PyPI metadata
    description = 'verbose debug, succint release mode behaviors',
    author = 'Michael Labbe',
    author_email = 'mike@frogtoss.com',
    url = 'https://github.com/mlabbe/execmode',
    keywords = ['logging', 'debug', 'release'],
)

