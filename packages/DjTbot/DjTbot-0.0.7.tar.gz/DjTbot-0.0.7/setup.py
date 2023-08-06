import os
from setuptools import setup, find_packages

__version__ = '0.0.7'

"""
Upload to pypi:
python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""

"""
Developer mode install
python -m pip install -e .
"""

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def here(name):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        name)



# Development Status :: 1 - Planning
# Development Status :: 2 - Pre-Alpha
# Development Status :: 3 - Alpha
# Development Status :: 4 - Beta
# Development Status :: 5 - Production/Stable
# Development Status :: 6 - Mature
# Development Status :: 7 - Inactive


license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
}


def read(name, mode='r'):
    try:
        with open(here(name), mode) as fp:
            long_description = fp.read()
    except IOError:
        return 'Error generating long description: {} File not found'.format(here(name))
    return long_description


setup(
    name='DjTbot',
    version=__version__,
    packages=find_packages(),
    url='https://git.herrerosolis.com/bots/DjTbot',
    download_url='https://git.herrerosolis.com/bots/DjTbot/-/archive/master/DjTbot-master.tar.gz',
    license=license_classifiers['MIT license'],
    author='Rafael Herrero Solis',
    author_email='rafahsolis@hotmail.com',
    keywords=['Django', 'Telegram', 'Bot'],
    description='Django Telegram Bot',
    long_description_content_type='text/markdown',
    long_description=read('README.md'),
    test_suite='nose.collector',
    tests_require=['nose', 'six'],
    install_requires=[
        'CheKnife>=0.0.7',
        'python-telegram-bot>=12.2.0',
        'Django>=3.0',
        'future>=0.16.0',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
)
