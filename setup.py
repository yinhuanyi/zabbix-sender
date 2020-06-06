# coding: utf-8
"""
@Author: Robby
@Module name: setup.py
@Create date: 2020-06-06
@Function: 
"""

import os
from setuptools import setup


def package_data(pkg, roots):
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                print(os.path.relpath(os.path.join(dirname, fname), pkg))
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='robby_zabbix_api',
    author='Robby',
    author_email='yinhuanyicn@gmail.com',
    url='http://bbs.yhyblog.cn',
    license="MIT",
    version='1.0.0',
    description='robby zabbix api',
    packages=[
        'zabbix_api',
    ],
    install_requires=[
        'requests',
        'markdown',
    ],
    package_data=package_data("zabbix_api", ["static", "public", "translations"]),
)
