#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SlowLog import SlowLog


class AlipayCloudCloudbaseDatabaseSlowsqldetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseDatabaseSlowsqldetailQueryResponse, self).__init__()
        self._page_index = None
        self._page_size = None
        self._slow_logs = None
        self._total = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def slow_logs(self):
        return self._slow_logs

    @slow_logs.setter
    def slow_logs(self, value):
        if isinstance(value, list):
            self._slow_logs = list()
            for i in value:
                if isinstance(i, SlowLog):
                    self._slow_logs.append(i)
                else:
                    self._slow_logs.append(SlowLog.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseDatabaseSlowsqldetailQueryResponse, self).parse_response_content(response_content)
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'slow_logs' in response:
            self.slow_logs = response['slow_logs']
        if 'total' in response:
            self.total = response['total']
