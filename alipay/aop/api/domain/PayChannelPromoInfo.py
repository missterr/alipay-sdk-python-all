#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChannelDetailParams import ChannelDetailParams
from alipay.aop.api.domain.InstallmentInfo import InstallmentInfo
from alipay.aop.api.domain.PrePayOperationInfo import PrePayOperationInfo


class PayChannelPromoInfo(object):

    def __init__(self):
        self._channel_balance = None
        self._channel_code = None
        self._channel_detail_params = None
        self._channel_enable = None
        self._channel_index = None
        self._channel_logo = None
        self._channel_name = None
        self._channel_operation_info = None
        self._installment_info_list = None
        self._operation_list = None

    @property
    def channel_balance(self):
        return self._channel_balance

    @channel_balance.setter
    def channel_balance(self, value):
        self._channel_balance = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_detail_params(self):
        return self._channel_detail_params

    @channel_detail_params.setter
    def channel_detail_params(self, value):
        if isinstance(value, ChannelDetailParams):
            self._channel_detail_params = value
        else:
            self._channel_detail_params = ChannelDetailParams.from_alipay_dict(value)
    @property
    def channel_enable(self):
        return self._channel_enable

    @channel_enable.setter
    def channel_enable(self, value):
        self._channel_enable = value
    @property
    def channel_index(self):
        return self._channel_index

    @channel_index.setter
    def channel_index(self, value):
        self._channel_index = value
    @property
    def channel_logo(self):
        return self._channel_logo

    @channel_logo.setter
    def channel_logo(self, value):
        self._channel_logo = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def channel_operation_info(self):
        return self._channel_operation_info

    @channel_operation_info.setter
    def channel_operation_info(self, value):
        self._channel_operation_info = value
    @property
    def installment_info_list(self):
        return self._installment_info_list

    @installment_info_list.setter
    def installment_info_list(self, value):
        if isinstance(value, list):
            self._installment_info_list = list()
            for i in value:
                if isinstance(i, InstallmentInfo):
                    self._installment_info_list.append(i)
                else:
                    self._installment_info_list.append(InstallmentInfo.from_alipay_dict(i))
    @property
    def operation_list(self):
        return self._operation_list

    @operation_list.setter
    def operation_list(self, value):
        if isinstance(value, list):
            self._operation_list = list()
            for i in value:
                if isinstance(i, PrePayOperationInfo):
                    self._operation_list.append(i)
                else:
                    self._operation_list.append(PrePayOperationInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.channel_balance:
            if hasattr(self.channel_balance, 'to_alipay_dict'):
                params['channel_balance'] = self.channel_balance.to_alipay_dict()
            else:
                params['channel_balance'] = self.channel_balance
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.channel_detail_params:
            if hasattr(self.channel_detail_params, 'to_alipay_dict'):
                params['channel_detail_params'] = self.channel_detail_params.to_alipay_dict()
            else:
                params['channel_detail_params'] = self.channel_detail_params
        if self.channel_enable:
            if hasattr(self.channel_enable, 'to_alipay_dict'):
                params['channel_enable'] = self.channel_enable.to_alipay_dict()
            else:
                params['channel_enable'] = self.channel_enable
        if self.channel_index:
            if hasattr(self.channel_index, 'to_alipay_dict'):
                params['channel_index'] = self.channel_index.to_alipay_dict()
            else:
                params['channel_index'] = self.channel_index
        if self.channel_logo:
            if hasattr(self.channel_logo, 'to_alipay_dict'):
                params['channel_logo'] = self.channel_logo.to_alipay_dict()
            else:
                params['channel_logo'] = self.channel_logo
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.channel_operation_info:
            if hasattr(self.channel_operation_info, 'to_alipay_dict'):
                params['channel_operation_info'] = self.channel_operation_info.to_alipay_dict()
            else:
                params['channel_operation_info'] = self.channel_operation_info
        if self.installment_info_list:
            if isinstance(self.installment_info_list, list):
                for i in range(0, len(self.installment_info_list)):
                    element = self.installment_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_info_list[i] = element.to_alipay_dict()
            if hasattr(self.installment_info_list, 'to_alipay_dict'):
                params['installment_info_list'] = self.installment_info_list.to_alipay_dict()
            else:
                params['installment_info_list'] = self.installment_info_list
        if self.operation_list:
            if isinstance(self.operation_list, list):
                for i in range(0, len(self.operation_list)):
                    element = self.operation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_list, 'to_alipay_dict'):
                params['operation_list'] = self.operation_list.to_alipay_dict()
            else:
                params['operation_list'] = self.operation_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayChannelPromoInfo()
        if 'channel_balance' in d:
            o.channel_balance = d['channel_balance']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_detail_params' in d:
            o.channel_detail_params = d['channel_detail_params']
        if 'channel_enable' in d:
            o.channel_enable = d['channel_enable']
        if 'channel_index' in d:
            o.channel_index = d['channel_index']
        if 'channel_logo' in d:
            o.channel_logo = d['channel_logo']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'channel_operation_info' in d:
            o.channel_operation_info = d['channel_operation_info']
        if 'installment_info_list' in d:
            o.installment_info_list = d['installment_info_list']
        if 'operation_list' in d:
            o.operation_list = d['operation_list']
        return o


