#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskImagePlusQueryOrderInfo import RiskImagePlusQueryOrderInfo
from alipay.aop.api.domain.RiskImagePlusQueryOrderInfo import RiskImagePlusQueryOrderInfo


class AlipayCloudTraasRiskgoScalperQueryModel(object):

    def __init__(self):
        self._activity_info = None
        self._apdid = None
        self._bank_card_no = None
        self._business_code = None
        self._cert_no = None
        self._cert_type = None
        self._certificate_date = None
        self._channel = None
        self._customer_id = None
        self._email_address = None
        self._env_id = None
        self._imei = None
        self._imsi = None
        self._industry = None
        self._ip = None
        self._is_employee = None
        self._isv_pid = None
        self._lbs = None
        self._login_cert = None
        self._login_phone = None
        self._mac_address = None
        self._mailing_address = None
        self._mailing_phone = None
        self._mer_pid = None
        self._mobile_no = None
        self._open_id = None
        self._order_items_info = None
        self._order_items_info_list = None
        self._order_no = None
        self._out_order_no = None
        self._registration_cert = None
        self._registration_date = None
        self._registration_phone = None
        self._risk_type = None
        self._role = None
        self._sales_amount = None
        self._scene = None
        self._service = None
        self._store_mcc_desc = None
        self._user_id = None
        self._user_name = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        self._activity_info = value
    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def certificate_date(self):
        return self._certificate_date

    @certificate_date.setter
    def certificate_date(self, value):
        self._certificate_date = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def imsi(self):
        return self._imsi

    @imsi.setter
    def imsi(self, value):
        self._imsi = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def is_employee(self):
        return self._is_employee

    @is_employee.setter
    def is_employee(self, value):
        self._is_employee = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def lbs(self):
        return self._lbs

    @lbs.setter
    def lbs(self, value):
        self._lbs = value
    @property
    def login_cert(self):
        return self._login_cert

    @login_cert.setter
    def login_cert(self, value):
        self._login_cert = value
    @property
    def login_phone(self):
        return self._login_phone

    @login_phone.setter
    def login_phone(self, value):
        self._login_phone = value
    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value
    @property
    def mailing_address(self):
        return self._mailing_address

    @mailing_address.setter
    def mailing_address(self, value):
        self._mailing_address = value
    @property
    def mailing_phone(self):
        return self._mailing_phone

    @mailing_phone.setter
    def mailing_phone(self, value):
        self._mailing_phone = value
    @property
    def mer_pid(self):
        return self._mer_pid

    @mer_pid.setter
    def mer_pid(self, value):
        self._mer_pid = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_items_info(self):
        return self._order_items_info

    @order_items_info.setter
    def order_items_info(self, value):
        if isinstance(value, RiskImagePlusQueryOrderInfo):
            self._order_items_info = value
        else:
            self._order_items_info = RiskImagePlusQueryOrderInfo.from_alipay_dict(value)
    @property
    def order_items_info_list(self):
        return self._order_items_info_list

    @order_items_info_list.setter
    def order_items_info_list(self, value):
        if isinstance(value, list):
            self._order_items_info_list = list()
            for i in value:
                if isinstance(i, RiskImagePlusQueryOrderInfo):
                    self._order_items_info_list.append(i)
                else:
                    self._order_items_info_list.append(RiskImagePlusQueryOrderInfo.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def registration_cert(self):
        return self._registration_cert

    @registration_cert.setter
    def registration_cert(self, value):
        self._registration_cert = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
    @property
    def registration_phone(self):
        return self._registration_phone

    @registration_phone.setter
    def registration_phone(self, value):
        self._registration_phone = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def sales_amount(self):
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        self._sales_amount = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value
    @property
    def store_mcc_desc(self):
        return self._store_mcc_desc

    @store_mcc_desc.setter
    def store_mcc_desc(self, value):
        self._store_mcc_desc = value
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
        if self.activity_info:
            if hasattr(self.activity_info, 'to_alipay_dict'):
                params['activity_info'] = self.activity_info.to_alipay_dict()
            else:
                params['activity_info'] = self.activity_info
        if self.apdid:
            if hasattr(self.apdid, 'to_alipay_dict'):
                params['apdid'] = self.apdid.to_alipay_dict()
            else:
                params['apdid'] = self.apdid
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.certificate_date:
            if hasattr(self.certificate_date, 'to_alipay_dict'):
                params['certificate_date'] = self.certificate_date.to_alipay_dict()
            else:
                params['certificate_date'] = self.certificate_date
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.imsi:
            if hasattr(self.imsi, 'to_alipay_dict'):
                params['imsi'] = self.imsi.to_alipay_dict()
            else:
                params['imsi'] = self.imsi
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.is_employee:
            if hasattr(self.is_employee, 'to_alipay_dict'):
                params['is_employee'] = self.is_employee.to_alipay_dict()
            else:
                params['is_employee'] = self.is_employee
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.lbs:
            if hasattr(self.lbs, 'to_alipay_dict'):
                params['lbs'] = self.lbs.to_alipay_dict()
            else:
                params['lbs'] = self.lbs
        if self.login_cert:
            if hasattr(self.login_cert, 'to_alipay_dict'):
                params['login_cert'] = self.login_cert.to_alipay_dict()
            else:
                params['login_cert'] = self.login_cert
        if self.login_phone:
            if hasattr(self.login_phone, 'to_alipay_dict'):
                params['login_phone'] = self.login_phone.to_alipay_dict()
            else:
                params['login_phone'] = self.login_phone
        if self.mac_address:
            if hasattr(self.mac_address, 'to_alipay_dict'):
                params['mac_address'] = self.mac_address.to_alipay_dict()
            else:
                params['mac_address'] = self.mac_address
        if self.mailing_address:
            if hasattr(self.mailing_address, 'to_alipay_dict'):
                params['mailing_address'] = self.mailing_address.to_alipay_dict()
            else:
                params['mailing_address'] = self.mailing_address
        if self.mailing_phone:
            if hasattr(self.mailing_phone, 'to_alipay_dict'):
                params['mailing_phone'] = self.mailing_phone.to_alipay_dict()
            else:
                params['mailing_phone'] = self.mailing_phone
        if self.mer_pid:
            if hasattr(self.mer_pid, 'to_alipay_dict'):
                params['mer_pid'] = self.mer_pid.to_alipay_dict()
            else:
                params['mer_pid'] = self.mer_pid
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_items_info:
            if hasattr(self.order_items_info, 'to_alipay_dict'):
                params['order_items_info'] = self.order_items_info.to_alipay_dict()
            else:
                params['order_items_info'] = self.order_items_info
        if self.order_items_info_list:
            if isinstance(self.order_items_info_list, list):
                for i in range(0, len(self.order_items_info_list)):
                    element = self.order_items_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_items_info_list[i] = element.to_alipay_dict()
            if hasattr(self.order_items_info_list, 'to_alipay_dict'):
                params['order_items_info_list'] = self.order_items_info_list.to_alipay_dict()
            else:
                params['order_items_info_list'] = self.order_items_info_list
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.registration_cert:
            if hasattr(self.registration_cert, 'to_alipay_dict'):
                params['registration_cert'] = self.registration_cert.to_alipay_dict()
            else:
                params['registration_cert'] = self.registration_cert
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        if self.registration_phone:
            if hasattr(self.registration_phone, 'to_alipay_dict'):
                params['registration_phone'] = self.registration_phone.to_alipay_dict()
            else:
                params['registration_phone'] = self.registration_phone
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.sales_amount:
            if hasattr(self.sales_amount, 'to_alipay_dict'):
                params['sales_amount'] = self.sales_amount.to_alipay_dict()
            else:
                params['sales_amount'] = self.sales_amount
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.store_mcc_desc:
            if hasattr(self.store_mcc_desc, 'to_alipay_dict'):
                params['store_mcc_desc'] = self.store_mcc_desc.to_alipay_dict()
            else:
                params['store_mcc_desc'] = self.store_mcc_desc
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
        o = AlipayCloudTraasRiskgoScalperQueryModel()
        if 'activity_info' in d:
            o.activity_info = d['activity_info']
        if 'apdid' in d:
            o.apdid = d['apdid']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'certificate_date' in d:
            o.certificate_date = d['certificate_date']
        if 'channel' in d:
            o.channel = d['channel']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'imei' in d:
            o.imei = d['imei']
        if 'imsi' in d:
            o.imsi = d['imsi']
        if 'industry' in d:
            o.industry = d['industry']
        if 'ip' in d:
            o.ip = d['ip']
        if 'is_employee' in d:
            o.is_employee = d['is_employee']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'lbs' in d:
            o.lbs = d['lbs']
        if 'login_cert' in d:
            o.login_cert = d['login_cert']
        if 'login_phone' in d:
            o.login_phone = d['login_phone']
        if 'mac_address' in d:
            o.mac_address = d['mac_address']
        if 'mailing_address' in d:
            o.mailing_address = d['mailing_address']
        if 'mailing_phone' in d:
            o.mailing_phone = d['mailing_phone']
        if 'mer_pid' in d:
            o.mer_pid = d['mer_pid']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_items_info' in d:
            o.order_items_info = d['order_items_info']
        if 'order_items_info_list' in d:
            o.order_items_info_list = d['order_items_info_list']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'registration_cert' in d:
            o.registration_cert = d['registration_cert']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        if 'registration_phone' in d:
            o.registration_phone = d['registration_phone']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'role' in d:
            o.role = d['role']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service' in d:
            o.service = d['service']
        if 'store_mcc_desc' in d:
            o.store_mcc_desc = d['store_mcc_desc']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


