#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceBillEventTriggerModel(object):

    def __init__(self):
        self._bill_id_list = None
        self._open_id = None
        self._user_id = None

    @property
    def bill_id_list(self):
        return self._bill_id_list

    @bill_id_list.setter
    def bill_id_list(self, value):
        if isinstance(value, list):
            self._bill_id_list = list()
            for i in value:
                self._bill_id_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_id_list:
            if isinstance(self.bill_id_list, list):
                for i in range(0, len(self.bill_id_list)):
                    element = self.bill_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_id_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_id_list, 'to_alipay_dict'):
                params['bill_id_list'] = self.bill_id_list.to_alipay_dict()
            else:
                params['bill_id_list'] = self.bill_id_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceBillEventTriggerModel()
        if 'bill_id_list' in d:
            o.bill_id_list = d['bill_id_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


