from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lurk',
    version='0.1.3',
    description='Extract html from one or multiple urls',
    long_description=long_description,
    url='https://github.com/mateogianolio/lurk',
    author='Mateo Gianolio',
    author_email='gianoliomateo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='lurk lurker scrape scraper scraping webscrape crawl crawler crawling',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'lurk=module:main',
        ],
    }
)
