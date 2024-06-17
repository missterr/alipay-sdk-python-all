#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpdateContactRequest(object):

    def __init__(self):
        self._email = None
        self._id = None
        self._job_title = None
        self._name = None
        self._operator = None
        self._phone_number = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.job_title:
            if hasattr(self.job_title, 'to_alipay_dict'):
                params['job_title'] = self.job_title.to_alipay_dict()
            else:
                params['job_title'] = self.job_title
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpdateContactRequest()
        if 'email' in d:
            o.email = d['email']
        if 'id' in d:
            o.id = d['id']
        if 'job_title' in d:
            o.job_title = d['job_title']
        if 'name' in d:
            o.name = d['name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


