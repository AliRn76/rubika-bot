import os
import re
from setuptools import setup, find_packages


def rubika_version() -> str:
    with open(os.path.join('rubika_bot/__init__.py')) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


_version = rubika_version()
_long_description = open('README.md').read()

setup(
    name='rubika-bot',
    version=_version,
    python_requires='>=3.10',
    author='Rubika Team',
    author_email='A.RajabNezhad@rubika.ir',
    keywords=['rubika', 'bot', 'rubika-bot'],
    url='https://github.com/alirn76/rubika-bot',
    description='Rubika Bot Library',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(where='.', exclude=(), include=('*',)),
    install_requires=['requests', 'pydantic'],
)





