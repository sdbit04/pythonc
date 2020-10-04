from setuptools import setup 

setup( name="pythonc",
description="this give a command pythonc to compile any python module",
version="1.1.0",
author="swapan",
packages=["pythonc"],
entry_points={'console_scripts': [
    'pythonc=pythonc.pythonc:main_method',
]},
license='MIT',
classifiers=[
    'License :: OSI Approved :: MIT License'
]
)
