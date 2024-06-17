#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PendingEquityVO(object):

    def __init__(self):
        self._budget_type = None
        self._camp_id = None
        self._camp_order_id = None
        self._channel = None
        self._display_info = None
        self._interest_id = None
        self._prize_amount = None
        self._prize_biz_type = None
        self._prize_id = None
        self._prize_name = None
        self._prize_strategy_type = None
        self._send_order_id = None
        self._voucher_template_id = None

    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_order_id(self):
        return self._camp_order_id

    @camp_order_id.setter
    def camp_order_id(self, value):
        self._camp_order_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        self._display_info = value
    @property
    def interest_id(self):
        return self._interest_id

    @interest_id.setter
    def interest_id(self, value):
        self._interest_id = value
    @property
    def prize_amount(self):
        return self._prize_amount

    @prize_amount.setter
    def prize_amount(self, value):
        self._prize_amount = value
    @property
    def prize_biz_type(self):
        return self._prize_biz_type

    @prize_biz_type.setter
    def prize_biz_type(self, value):
        self._prize_biz_type = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_strategy_type(self):
        return self._prize_strategy_type

    @prize_strategy_type.setter
    def prize_strategy_type(self, value):
        self._prize_strategy_type = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_order_id:
            if hasattr(self.camp_order_id, 'to_alipay_dict'):
                params['camp_order_id'] = self.camp_order_id.to_alipay_dict()
            else:
                params['camp_order_id'] = self.camp_order_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.interest_id:
            if hasattr(self.interest_id, 'to_alipay_dict'):
                params['interest_id'] = self.interest_id.to_alipay_dict()
            else:
                params['interest_id'] = self.interest_id
        if self.prize_amount:
            if hasattr(self.prize_amount, 'to_alipay_dict'):
                params['prize_amount'] = self.prize_amount.to_alipay_dict()
            else:
                params['prize_amount'] = self.prize_amount
        if self.prize_biz_type:
            if hasattr(self.prize_biz_type, 'to_alipay_dict'):
                params['prize_biz_type'] = self.prize_biz_type.to_alipay_dict()
            else:
                params['prize_biz_type'] = self.prize_biz_type
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_strategy_type:
            if hasattr(self.prize_strategy_type, 'to_alipay_dict'):
                params['prize_strategy_type'] = self.prize_strategy_type.to_alipay_dict()
            else:
                params['prize_strategy_type'] = self.prize_strategy_type
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PendingEquityVO()
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_order_id' in d:
            o.camp_order_id = d['camp_order_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'interest_id' in d:
            o.interest_id = d['interest_id']
        if 'prize_amount' in d:
            o.prize_amount = d['prize_amount']
        if 'prize_biz_type' in d:
            o.prize_biz_type = d['prize_biz_type']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_strategy_type' in d:
            o.prize_strategy_type = d['prize_strategy_type']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        return o


