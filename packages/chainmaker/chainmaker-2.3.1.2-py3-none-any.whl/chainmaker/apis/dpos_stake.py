#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   dpos.py
# @Function     :   ChainMaker DPOS ERC20 / DPOS Stake 等操作接口

from chainmaker.apis.base_client import BaseClient
from chainmaker.keys import (SystemContractName, DposStakeMethod, ParamKey)
from chainmaker.protos.common.request_pb2 import Payload
from chainmaker.protos.common.result_pb2 import TxResponse


class DPosStakeMixIn(BaseClient):
    """DPos权益操作"""

    # 08-08 Stake合约中设置验证人的NodeID
    def set_node_id(self, node_id: str, timeout: int = None, with_sync_result: bool = None) -> TxResponse:  # ✅
        """
        Stake合约中设置验证人的NodeId
        <08-08-DPOS_STAKE-SET_NODE_ID>
        :param node_id: 节点Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._debug('begin to set node id')
        params = {
            ParamKey.node_id.name: node_id
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.SET_NODE_ID.name,
            params)
        response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 08-09 Stake合约中查询验证人的NodeId
    def get_node_id(self, address: str) -> str:  # ✅
        """
        Stake合约中查询验证人的NodeID
        <08-09-DPOS_STAKE-GET_NODE_ID>
        :param address:
        :return:
        """
        self._debug('begin to get node id')
        params = {
            ParamKey.address.name: address
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.GET_NODE_ID.name,
            params)

        response = self.send_request(payload)
        data = response.contract_result.result
        return data.decode()

    # 08-10 更新验证人节点的最少自我抵押数量
    def create_update_min_self_delegation_payload(self, min_self_delegation: int) -> Payload:  # todo
        """
        更新验证人节点的最少自我抵押数量
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
        :return:
        """
        self._debug('begin to create [DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION] to be signed payload')
        params = {
            ParamKey.min_self_delegation.name: min_self_delegation
        }
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.UPDATE_MIN_SELF_DELEGATION.name,
                                                             params)
        return payload

    # 08-11 查询验证人节点的最少自我抵押数量
    def get_min_self_delegation(self) -> int:  # ✅
        """
        查询验证人节点的最少自我抵押数量
        <08-11-DPOS_STAKE-READ_MIN_SELF_DELEGATION>
        :return:
        """
        self._debug('begin to get min self delegation')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_VALIDATOR_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data) if data else 0

    # 08-12 更新世代中的验证人数
    def create_update_epoch_validator_number_payload(self, epoch_validator_number: int) -> Payload:
        """
        更新世代中的验证人数
        <08-12-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        self._debug('begin to create [DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION] to be signed payload')
        params = {
            ParamKey.epoch_validator_number.name: epoch_validator_number
        }
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.UPDATE_EPOCH_BLOCK_NUMBER.name,
                                                             params)
        return payload

    # 08-13 查询世代中的验证人数
    def get_epoch_validator_number(self) -> int:  # ✅
        """
        查询世代中的验证人数
        <08-13-DPOS_STAKE-READ_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        self._debug('begin to get epoch validator number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_VALIDATOR_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data) if data else 0

    # 08-14 更新世代中的区块数量
    def create_update_epoch_block_number_payload(self, epoch_block_number: int) -> Payload:
        """
        更新世代中的区块数量
        <08-14-DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER>
        :return:
        """
        self._debug('begin to create [DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER] to be signed payload')
        params = {
            ParamKey.epoch_block_number.name: epoch_block_number
        }
        payload = self._payload_builder.create_invoke_payload(SystemContractName.DPOS_STAKE.name,
                                                              DposStakeMethod.UPDATE_EPOCH_BLOCK_NUMBER.name, params)
        return payload

    # 08-15 查询世代中的区块数量
    def get_epoch_block_number(self) -> int:  # ✅
        """
        查询世代中的区块数量
        <08-15-DPOS_STAKE-READ_EPOCH_BLOCK_NUMBER>
        :return:
        """
        self._debug('begin to get epoch block number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_BLOCK_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data) if data else 0

    # 08-16 查询收到解质押退款间隔的世代数
    def get_unbounding_interval_epoch_number(self) -> int:  # ✅
        """
        查询收到解质押退款间隔的世代数
        <08-16-DPOS_STAKE-READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER>
        :return:
        """
        self._debug('begin to get unbounding interval epoch number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data) if data else 0

    # 08-17 查询Stake合约的系统地址
    def get_stake_contract_address(self) -> str:  # ✅
        """
        查询Stake合约的系统地址
        <08-18-DPOS_STAKE-READ_SYSTEM_CONTRACT_ADDR>
        :return:
        """
        self._debug('begin to get state contract address')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_SYSTEM_CONTRACT_ADDR.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return data.decode()

    # 08-19
    def create_unbounding_payload(self) -> Payload:  # todo
        """
        <08-19-DPOS_STAKE-UNBOUNDING>
        :return:
        """
        raise NotImplementedError("待实现")
        self._debug('begin to create [DPOS_STAKE-UNBOUNDING] to be signed payload')
        params = {
            # todo
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.UNBOUNDING.name,
            params)
        return payload

    # 08-20
    def create_create_epoch_payload(self) -> Payload:
        """
        <08-20-DPOS_STAKE-CREATE_EPOCH>
        :return:
        """
        self._debug('begin to create [DPOS_STAKE-CREATE_EPOCH] to be signed payload')
        params = {
            # todo
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.CREATE_EPOCH.name,
            params)
        return payload

    # 08-21
    def create_update_epoch_validator_number_and_epoch_block_number_payload(self, epoch_block_number: int,
                                                                            epoch_validator_number: int) -> Payload:
        """
        <08-21-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER>
        :return:
        """
        self._debug('begin to create [DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER] '
                    'to be signed payload')
        params = {
            ParamKey.epoch_block_number: epoch_block_number,
            ParamKey.epoch_validator_number.name: epoch_validator_number
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER.name,
            params)
        return payload


class DPosStakeWithEndorsers(BaseClient):
    # 08-10 更新验证人节点的最少自我抵押数量
    def set_min_self_delegation(self, min_self_delegation: int, timeout: int = None,
                                with_sync_result: bool = None) -> TxResponse:  # todo
        """
        更新验证人节点的最少自我抵押数量
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
        :param min_self_delegation: 最少自我抵押数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        payload = self.create_update_min_self_delegation_payload(min_self_delegation)
        tx_response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return tx_response

    # 08-12 更新世代中的验证人数量
    def set_epoch_validator_number(self, epoch_validator_number: int, timeout: int = None,
                                   with_sync_result: bool = None) -> TxResponse:
        """
        更新世代中的验证人数量
        <08-12-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER>
        :param epoch_validator_number:  世代验证者数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        payload = self.create_update_epoch_validator_number_payload(epoch_validator_number)
        tx_response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return tx_response

    # 08-14 更新世代中的区块数量
    def set_epoch_block_number(self, epoch_block_number: int, timeout: int = None,
                               with_sync_result: bool = None) -> TxResponse:
        """
        更新世代中的区块数量
        <08-14-DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER>
        :param epoch_block_number: 世代区块数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        payload = self.create_update_epoch_block_number_payload(epoch_block_number)
        tx_response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return tx_response

    # 08-19
    def unbounding(self, timeout: int = None, with_sync_result: bool = None) -> TxResponse:  # todo
        """
        <08-19-DPOS_STAKE-UNBOUNDING>
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        raise NotImplementedError("待实现")
        payload = self.create_unbounding_payload()
        tx_response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return tx_response

    # 08-20
    def create_epoch(self) -> Payload:
        """
        <08-20-DPOS_STAKE-CREATE_EPOCH>
        :return:
        """
        raise NotImplementedError("待实现")

    # 08-21
    def set_epoch_validator_number_and_epoch_block_number(self, epoch_block_number: int,
                                                          epoch_validator_number: int, timeout: int = None,
                                                          with_sync_result: bool = None) -> Payload:
        """
        <08-21-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER>
        :return:
        """
        payload = self.create_update_epoch_validator_number_and_epoch_block_number_payload(epoch_block_number,
                                                                                           epoch_validator_number)
        tx_response = self.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return tx_response
