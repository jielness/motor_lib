# -*- coding: utf-8 -*-
# Time : 2021/7/2 2:45 PM
# Author : Shaojie Liu
# File : setup.py

from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='motor_lib',  # 包名
      version='0.0.1',  # 版本号
      description='A package of motor control',
      long_description=long_description,
      author='Shaojie Liu',
      author_email='jielness@zju.edu.cn',
      url='https://mp.weixin.qq.com/s/9FQ-Tun5FbpBepBAsdY62w',
      install_requires=['pyserial', ],
      license='GNU GENERAL PUBLIC LICENSE',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'],
      )
