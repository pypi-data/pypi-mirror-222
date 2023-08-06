from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = "Lc's python helper."

setup(
    name="lc-base-helper",
    version=VERSION,
    author="Diselorya",
    # author_email="listorlc@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['PyPDF2', 'pytesseract', 'pdfplumber', 'unicodedata', 'pangu', 'opencv-python'],
    keywords=['python', 'lc-base-helper', 'diselorya'],
    # data_files=[('lc-base-helper', ['lc-base-helper/asdf.json'])],
    # entry_points={
    # 'console_scripts': [
    #     'lc-base-helper = lc-base-helper.main:main'
    # ]
    # },
    license="MIT",
    # url="",
    scripts=['lc-base-helper/chineseLanguageHelper.py',
             'lc-base-helper/ocrHelper.py',
             'lc-base-helper/pathHelper.py',
             'lc-base-helper/pdfHelper.py',
             'lc-base-helper/stringHelper.py',
             'lc-base-helper/terminalHelper.py',
             ],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)