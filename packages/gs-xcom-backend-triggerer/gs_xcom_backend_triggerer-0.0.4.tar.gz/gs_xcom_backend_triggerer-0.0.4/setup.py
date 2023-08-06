from setuptools import setup, find_packages
import os

VERSION = '0.0.4'
DESCRIPTION = 'triggerer gs_xcom_backend module file'
LONG_DESCRIPTION = 'triggerer gs_xcom_backend module file'

# Setting up
setup(
    name="gs_xcom_backend_triggerer",
    version=VERSION,
    author="imvj202",
    author_email="imvj202@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)