#!/usr/bin/env python

"""
MAX30105 can be used to measure heart rate, pulse oximetry (SPO2 / blood oxygen saturation) and smoke other particles also.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name='max30105',
    version='0.0.5',
    author='EmbdEzaz9',
    author_email='embdezaz9@gmail.com',
    description="""Python library for the MAX30105 HeartRate-Pulse Detector/Smoke""",
    long_description=open('README.md').read() + '\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["max30105", "max30102", "esp32","Risc V","Raspberry Pi"],
    url='https://github.com/EmbdEzaz9/Max30105-0.0.5',
    download_url='https://files.pythonhosted.org/packages/92/71/26fc7cbf18d6c1deb96940664e4640ec372fd47b3b919f132ac14cedb27e/max30105-0.0.5.tar.gz)',
    classifiers=classifiers,
    packages=['max30105'],
    dependency_links  = [],
    install_requires=['i2cdevice>=0.0.7']
)
