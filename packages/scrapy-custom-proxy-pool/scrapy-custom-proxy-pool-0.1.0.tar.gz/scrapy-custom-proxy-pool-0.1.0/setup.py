from setuptools import setup, find_packages
import re
import os


def get_version():
    filename = os.path.join(os.path.dirname(__file__), "scrapy_custom_proxy_pool", "__init__.py")
    with open(filename) as f:
        return re.findall("__version__ = '([\d.\w]+)'", f.read())[0]


def get_long_description():
    return open('README.rst').read()


setup(
    name='scrapy-custom-proxy-pool',
    version=get_version(),
    author='Bohan Chen',
    author_email='chacyume@gmail.com',
    license='MIT',
    long_description=get_long_description(),
    description='Scrapy proxy pool that allows custom proxy provider',
    url='https://github.com/acyume/scrapy-custom-proxy-pool',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'scrapy',
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
