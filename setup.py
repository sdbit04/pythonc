from setuptools import setup 
import os

current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'README.md'),'r') as readme_ob:
    README=readme_ob.read()


setup( name="sdbit04-pythonc",
description="On installation, This package gives a command pythonc to compile any python module",
long_description=README,
long_description_content_type="text/markdown",
version="1.2.2",
author="swapankumarDas",
url="https://github.com/",
packages=["pythonc"],
entry_points={'console_scripts': [
    'pythonc=pythonc.pythonc:main_method',
]},
license='MIT',
classifiers=[
    'License :: OSI Approved :: MIT License'
]
)
