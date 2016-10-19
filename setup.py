import os
from setuptools import setup, find_packages

VERSION = __import__("sorl_thumbnail_serializer").VERSION


def read_md(path):
    long_desc = ""
    if os.path.exists(path):
        try:
            from pypandoc import convert
            long_desc = convert(path, 'rst')
        except:
            try:
                long_desc = open(path, 'r').read()
            except:
                pass
    return long_desc

long_desc = read_md(os.path.join(os.path.dirname(__file__), 'README.md'))


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sorl-thumbnail-serializer-field',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    description='An image serializer field for use with sorl and Django REST Framework.',
    long_description=long_desc,
    url='https://github.com/dessibelle/sorl-thumbnail-serializer-field',
    download_url="https://github.com/dessibelle/sorl-thumbnail-serializer-field/"
        "archive/%s.tar.gz" % VERSION,
    author='Simon Fransson',
    author_email='simon@dessibelle.se',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.5.0',
        'djangorestframework==3.2.3',
        'sorl-thumbnail==12.3',
    ],
)
