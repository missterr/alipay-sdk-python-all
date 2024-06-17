#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiInvoiceMixInfoVO import OpenApiInvoiceMixInfoVO


class AlipayBossFncOutputinvoiceApplyPreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncOutputinvoiceApplyPreviewResponse, self).__init__()
        self._result_set = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, OpenApiInvoiceMixInfoVO):
            self._result_set = value
        else:
            self._result_set = OpenApiInvoiceMixInfoVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncOutputinvoiceApplyPreviewResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
