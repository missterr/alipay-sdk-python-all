#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardOrderBatchQueryResponse(object):

    def __init__(self):
        self._cancel_type = None
        self._card_id = None
        self._card_status = None
        self._card_template_id = None
        self._card_type = None
        self._create_date = None
        self._name = None
        self._open_id = None
        self._order_id = None
        self._origin_price_total = None
        self._out_order_no = None
        self._remain_count = None
        self._sale_price_total = None
        self._shop_id = None
        self._total_count = None
        self._user_id = None
        self._user_name = None

    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def origin_price_total(self):
        return self._origin_price_total

    @origin_price_total.setter
    def origin_price_total(self, value):
        self._origin_price_total = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def sale_price_total(self):
        return self._sale_price_total

    @sale_price_total.setter
    def sale_price_total(self, value):
        self._sale_price_total = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_type:
            if hasattr(self.cancel_type, 'to_alipay_dict'):
                params['cancel_type'] = self.cancel_type.to_alipay_dict()
            else:
                params['cancel_type'] = self.cancel_type
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.origin_price_total:
            if hasattr(self.origin_price_total, 'to_alipay_dict'):
                params['origin_price_total'] = self.origin_price_total.to_alipay_dict()
            else:
                params['origin_price_total'] = self.origin_price_total
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        if self.sale_price_total:
            if hasattr(self.sale_price_total, 'to_alipay_dict'):
                params['sale_price_total'] = self.sale_price_total.to_alipay_dict()
            else:
                params['sale_price_total'] = self.sale_price_total
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardOrderBatchQueryResponse()
        if 'cancel_type' in d:
            o.cancel_type = d['cancel_type']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'origin_price_total' in d:
            o.origin_price_total = d['origin_price_total']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        if 'sale_price_total' in d:
            o.sale_price_total = d['sale_price_total']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


