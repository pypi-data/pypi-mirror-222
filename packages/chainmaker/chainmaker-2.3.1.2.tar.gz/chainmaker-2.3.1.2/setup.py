#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   setup.py
# @Function     :   安装配置

from setuptools import setup

# VERSION = '2.3.1'
VERSION = '2.3.1.2'

setup(
    name='chainmaker',
    version=VERSION,
    packages=['chainmaker',
              'chainmaker.utils',
              'chainmaker.utils.gm',
              'chainmaker.apis',
              'chainmaker.protos',
              'chainmaker.protos.accesscontrol',
              'chainmaker.protos.api',
              'chainmaker.protos.common',
              'chainmaker.protos.config',
              'chainmaker.protos.consensus',
              'chainmaker.protos.discovery',
              'chainmaker.protos.net',
              'chainmaker.protos.store',
              'chainmaker.protos.sync',
              'chainmaker.protos.syscontract',
              'chainmaker.protos.txpool',
              ],
    url='https://git.chainmaker.org.cn/chainmaker/chainmaker-sdk-python.git',
    license='Apache-2.0',
    author='The THL chainmaker developers',
    author_email='operation@chainmaker.org',
    description='ChainMaker Python SDK',
    install_requires=["protobuf", "grpcio", "pyyaml", "cryptography", "pysha3", "pymysql", "eth-abi",
                      "asn1", "pyasn1", "pyasn1-modules"]
)
