#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardTemplatestatusModifyModel(object):

    def __init__(self):
        self._card_template_id = None
        self._operate_status = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def operate_status(self):
        return self._operate_status

    @operate_status.setter
    def operate_status(self, value):
        self._operate_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.operate_status:
            if hasattr(self.operate_status, 'to_alipay_dict'):
                params['operate_status'] = self.operate_status.to_alipay_dict()
            else:
                params['operate_status'] = self.operate_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplatestatusModifyModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'operate_status' in d:
            o.operate_status = d['operate_status']
        return o


