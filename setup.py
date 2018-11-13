#!/usr/bin/env python
# vim: se fileencoding=utf-8 :
# (c) 2018 Michał Górny
# Released under the terms of the 2-clause BSD license

from distutils.core import setup


setup(
    name='kernel-readver',
    version='0',
    author='Michał Górny',
    author_email='mgorny@gentoo.org',
    url='http://github.com/mgorny/kernel-readver',

    scripts=['kernel-readver'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Operating System Kernels :: Linux',
    ],
)
