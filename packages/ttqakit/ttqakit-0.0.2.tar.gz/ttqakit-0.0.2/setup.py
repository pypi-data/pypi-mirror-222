from setuptools import setup, find_packages

VERSION = '0.0.2'
AUTHOR = 'lfy'
AUTHOR_EMAIL = '2591091196@email.com'
DESCRIPTION = 'ttqakit'
LICENSE = 'Apache 2.0'
URL = 'https://github.com/lfy79001/TableQAKit'
KEYWORDS = "A Comprehensive and Practical Toolkit for Table-based Question Answering"
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    # Add more classifiers as needed
]
setup(
    name='ttqakit',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url=URL,
    LICENSE=LICENSE,
    keywords=KEYWORDS,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'torch',
        'transformers',
        'datasets',
        'peft',
        'openai',
        'matplotlib',
        'matplotlib',
        'wandb',
        'rouge_chinese'
    ],
    classifiers=CLASSIFIERS
)
