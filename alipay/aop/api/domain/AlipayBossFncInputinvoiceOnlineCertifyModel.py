#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceCertifyOpenApiDTO import InputInvoiceCertifyOpenApiDTO


class AlipayBossFncInputinvoiceOnlineCertifyModel(object):

    def __init__(self):
        self._input_invoice_certify_open_api_dto = None

    @property
    def input_invoice_certify_open_api_dto(self):
        return self._input_invoice_certify_open_api_dto

    @input_invoice_certify_open_api_dto.setter
    def input_invoice_certify_open_api_dto(self, value):
        if isinstance(value, InputInvoiceCertifyOpenApiDTO):
            self._input_invoice_certify_open_api_dto = value
        else:
            self._input_invoice_certify_open_api_dto = InputInvoiceCertifyOpenApiDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.input_invoice_certify_open_api_dto:
            if hasattr(self.input_invoice_certify_open_api_dto, 'to_alipay_dict'):
                params['input_invoice_certify_open_api_dto'] = self.input_invoice_certify_open_api_dto.to_alipay_dict()
            else:
                params['input_invoice_certify_open_api_dto'] = self.input_invoice_certify_open_api_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInputinvoiceOnlineCertifyModel()
        if 'input_invoice_certify_open_api_dto' in d:
            o.input_invoice_certify_open_api_dto = d['input_invoice_certify_open_api_dto']
        return o


