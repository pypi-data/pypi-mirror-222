from setuptools import setup, find_packages

classifiers = [
"Development Status :: 2 - Pre-Alpha",
"Intended Audience :: Education",
"Operating System :: MacOS :: MacOS X",
"Operating System :: Microsoft :: Windows",
"Programming Language :: Python :: 3",
]
setup(
name="catalystai",
version="1.0.2",
description="Catalyst AI package",
long_description="Catalyst AI package to upload data to MinIO bucket",
url="",
author="Catalyst AI",
author_email="catalystlabs.ai@gmail.com",
license="Catalyst AI",
classifiers=classifiers,
keywords=['python', 'first package'],
packages=find_packages(),
install_requires=[], # add any additional packages that needs to be installed along with your package. 
)