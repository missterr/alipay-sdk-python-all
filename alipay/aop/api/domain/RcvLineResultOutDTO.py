#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RcvLineResultOutDTO(object):

    def __init__(self):
        self._expense_month = None
        self._item_name = None
        self._line_type = None
        self._po_line_num = None
        self._quantity = None
        self._rcv_date = None
        self._rcv_line_id = None
        self._rcv_line_num = None
        self._received_amount = None
        self._received_quantity = None

    @property
    def expense_month(self):
        return self._expense_month

    @expense_month.setter
    def expense_month(self, value):
        self._expense_month = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def line_type(self):
        return self._line_type

    @line_type.setter
    def line_type(self, value):
        self._line_type = value
    @property
    def po_line_num(self):
        return self._po_line_num

    @po_line_num.setter
    def po_line_num(self, value):
        self._po_line_num = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def rcv_date(self):
        return self._rcv_date

    @rcv_date.setter
    def rcv_date(self, value):
        self._rcv_date = value
    @property
    def rcv_line_id(self):
        return self._rcv_line_id

    @rcv_line_id.setter
    def rcv_line_id(self, value):
        self._rcv_line_id = value
    @property
    def rcv_line_num(self):
        return self._rcv_line_num

    @rcv_line_num.setter
    def rcv_line_num(self, value):
        self._rcv_line_num = value
    @property
    def received_amount(self):
        return self._received_amount

    @received_amount.setter
    def received_amount(self, value):
        self._received_amount = value
    @property
    def received_quantity(self):
        return self._received_quantity

    @received_quantity.setter
    def received_quantity(self, value):
        self._received_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_month:
            if hasattr(self.expense_month, 'to_alipay_dict'):
                params['expense_month'] = self.expense_month.to_alipay_dict()
            else:
                params['expense_month'] = self.expense_month
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.line_type:
            if hasattr(self.line_type, 'to_alipay_dict'):
                params['line_type'] = self.line_type.to_alipay_dict()
            else:
                params['line_type'] = self.line_type
        if self.po_line_num:
            if hasattr(self.po_line_num, 'to_alipay_dict'):
                params['po_line_num'] = self.po_line_num.to_alipay_dict()
            else:
                params['po_line_num'] = self.po_line_num
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.rcv_date:
            if hasattr(self.rcv_date, 'to_alipay_dict'):
                params['rcv_date'] = self.rcv_date.to_alipay_dict()
            else:
                params['rcv_date'] = self.rcv_date
        if self.rcv_line_id:
            if hasattr(self.rcv_line_id, 'to_alipay_dict'):
                params['rcv_line_id'] = self.rcv_line_id.to_alipay_dict()
            else:
                params['rcv_line_id'] = self.rcv_line_id
        if self.rcv_line_num:
            if hasattr(self.rcv_line_num, 'to_alipay_dict'):
                params['rcv_line_num'] = self.rcv_line_num.to_alipay_dict()
            else:
                params['rcv_line_num'] = self.rcv_line_num
        if self.received_amount:
            if hasattr(self.received_amount, 'to_alipay_dict'):
                params['received_amount'] = self.received_amount.to_alipay_dict()
            else:
                params['received_amount'] = self.received_amount
        if self.received_quantity:
            if hasattr(self.received_quantity, 'to_alipay_dict'):
                params['received_quantity'] = self.received_quantity.to_alipay_dict()
            else:
                params['received_quantity'] = self.received_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcvLineResultOutDTO()
        if 'expense_month' in d:
            o.expense_month = d['expense_month']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'line_type' in d:
            o.line_type = d['line_type']
        if 'po_line_num' in d:
            o.po_line_num = d['po_line_num']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'rcv_date' in d:
            o.rcv_date = d['rcv_date']
        if 'rcv_line_id' in d:
            o.rcv_line_id = d['rcv_line_id']
        if 'rcv_line_num' in d:
            o.rcv_line_num = d['rcv_line_num']
        if 'received_amount' in d:
            o.received_amount = d['received_amount']
        if 'received_quantity' in d:
            o.received_quantity = d['received_quantity']
        return o


