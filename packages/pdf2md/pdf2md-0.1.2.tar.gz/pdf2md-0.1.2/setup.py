import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='pdf2md',
    version='0.1.2',
    description='Convert PDF files into markdown files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='bolin',
    author_email='runningBolin@gmail.com',
    url='https://github.com/runningBolin/pdf-to-markdown',
    license='New BSD License',
    install_requires=[
        'pdfminer.six',
    ],
    packages=[
        'pdf2md',
    ],
    scripts=[
        'bin/pdf2md',
    ],
)
