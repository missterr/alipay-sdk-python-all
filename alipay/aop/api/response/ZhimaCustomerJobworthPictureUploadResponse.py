#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthPictureUploadResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthPictureUploadResponse, self).__init__()
        self._pic_id = None
        self._sub_code = None
        self._sub_msg = None

    @property
    def pic_id(self):
        return self._pic_id

    @pic_id.setter
    def pic_id(self, value):
        self._pic_id = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthPictureUploadResponse, self).parse_response_content(response_content)
        if 'pic_id' in response:
            self.pic_id = response['pic_id']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
