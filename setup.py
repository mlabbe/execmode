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
    license = 'MIT',
)

# from distutils.core import setup

# setup(
#     name = 'execmode',
#     packages = ['execmode'],
#     version = '1.0',
#     description = 'verbose debug, succint release mode behaviors',
#     author = 'Michael Labbe',
#     author_email = 'mike@frogtoss.com',
#     url = 'https://github.com/mlabbe/execmode',
#     download_url = 'https://github.com/mlabbe/execmode/tarball/1.0',
#     keywords = ['logging', 'debug', 'release'],
#     classifiers = [],
# )


