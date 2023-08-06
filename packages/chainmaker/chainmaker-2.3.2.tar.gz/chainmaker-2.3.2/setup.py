#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   setup.py
# @Function     :   安装配置

from setuptools import setup, find_packages

__VERSION__ = '2.3.2'
__AUTHOR__ = 'The THL chainmaker developers'
__AUTHOR_EMAIL = 'operation@chainmaker.org'

INSTALL_REQUIRES = [
    "protobuf",
    "grpcio",
    "pyyaml",
    "cryptography",
    "pysha3",
    "pymysql",
    "eth-abi",
    "asn1",
    "pyasn1",
    "pyasn1-modules"
]

setup(
    name='chainmaker',
    description='ChainMaker Python SDK',
    version=__VERSION__,
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL,
    license='Apache-2.0',
    url='https://git.chainmaker.org.cn/chainmaker/chainmaker-sdk-python.git',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    packages=find_packages(include=['chainmaker']),
    # packages=['chainmaker',
    #           'chainmaker.utils',
    #           'chainmaker.utils.gm',
    #           'chainmaker.apis',
    #           'chainmaker.protos',
    #           'chainmaker.protos.accesscontrol',
    #           'chainmaker.protos.api',
    #           'chainmaker.protos.common',
    #           'chainmaker.protos.config',
    #           'chainmaker.protos.consensus',
    #           'chainmaker.protos.discovery',
    #           'chainmaker.protos.net',
    #           'chainmaker.protos.store',
    #           'chainmaker.protos.sync',
    #           'chainmaker.protos.syscontract',
    #           'chainmaker.protos.txpool',
    #           ],
)
