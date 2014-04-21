# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = """{0}

{1}
""".format(read('README.rst'), read('HISTORY.rst'))


setup(
    name='bobtemplates.gr1n',
    version='0.1',
    description='Collection of `mr.bob` templates for my personal use.',
    long_description=long_description,
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    author='Nikita Grishko',
    author_email='grin.minsk@gmail.com',
    url='https://github.com/Gr1N/bobtemplates.gr1n',
    license='MIT',
    packages=find_packages(),
    install_requires=(
        'setuptools',
        'mr.bob',
    ),
    extras_require={
        'development': (
            'zest.releaser',
            'check-manifest',
        ),
    },
    namespace_packages=(
        'bobtemplates',
    ),
    include_package_data=True,
    zip_safe=False
)
