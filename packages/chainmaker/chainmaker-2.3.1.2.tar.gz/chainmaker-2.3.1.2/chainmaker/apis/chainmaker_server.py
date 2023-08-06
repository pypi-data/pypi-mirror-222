#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   chainmaker_server.py
# @Function     :   ChainMaker系统合约(链查询相关)接口
import time

import grpc

from chainmaker.apis.base_client import BaseClient
from chainmaker.exceptions import ERR_MSG_MAP, RpcConnectError, ContractFail
from chainmaker.protos import TxRequest
from chainmaker.protos.common.result_pb2 import Result
from chainmaker.sdk_config import DefaultConfig


class ChainMakerServerMixIn(BaseClient):
    """ChainMaker服务操作"""

    def get_chainmaker_server_version(self) -> str:
        """获取chainmaker服务版本号"""
        self._debug('begin to get chainmaker server version')
        tx_request = TxRequest()

        retry_limit = DefaultConfig.rpc_retry_limit
        retry_interval = DefaultConfig.rpc_retry_interval

        err_msg = ''
        for i in range(retry_limit):
            try:
                return self._get_client().GetChainMakerVersion(tx_request).version
            except grpc._channel._InactiveRpcError as ex:
                # todo 处理 DeadlineExceeded
                err_msg = ERR_MSG_MAP.get(ex.details(), ex.details())
                # self._logger.exception(ex)
                time.sleep(retry_interval // 1000)  # 毫秒
                self._logger.debug('[Sdk] %s, retry to send rpc request to %s' % (ex.details(), self.node.node_addr))
        else:
            raise RpcConnectError(
                '[Sdk] rpc service<%s enable_tls=%s> not available: %s' % (
                    self.node.node_addr, self.node.enable_tls, err_msg))

