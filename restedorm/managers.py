#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
import requests
from . import BASE_URL, caller_name
from requests.exceptions import ConnectionError
from .exeptions import NotFoundException, ApiError

__author__ = 'magnusknutas'
from .statics import HTTP_200, HTTP_404


class BaseManager(object):
    next = None
    previous = None
    count = 0

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.endpoint = args[1]
            self.cls = args[0]
        self.module = caller_name(skip=4)

    def filter(self, **kwargs):
        uri = self._get_uri() + ('?' if len(kwargs) > 0 else '')
        for key in kwargs.keys():
            uri += str(key)+"="+str(kwargs[key])

        try:
            r = requests.get(uri, auth=('name', 'pass'))  # TODO: Fix auth
        except ConnectionError:
            raise NotFoundException("endpoint %s is not found" % self.endpoint)

        if r.status_code == 404:
            raise NotFoundException("endpoint %s is not found" % self.endpoint)
        objs = json.loads(r.text)
        ret = []

        if r.status_code != 200:
            raise ApiError("%s, %s" % (r.status_code, r.text))

        for obj in objs.get('results', {}):
            obj.pop('id')
            ret.append(self.cls(**obj))
        self.next = objs.get('next', None)
        self.previous = objs.get('previous', None)
        self.count = objs.get('count', None)
        return ret

    def all(self):
        page = 1
        ret = self.filter(page=page)
        while self.next:
            page += 1
            ret += self.filter(page=page)
        return ret

    def get(self, ident):
        uri = self._get_uri() + "%i/" % ident

        r = requests.get(uri, auth=('name', 'pass'))  # TODO: Fix auth

        if r.status_code == HTTP_404:
            raise NotFoundException("id %i not found in endpoint /%s/" % (ident, self.endpoint))

        obj = json.loads(r.text)

        if r.status_code == HTTP_200:
            return self.cls(**obj)
        else:
            raise ApiError("%s, %s" % (r.status_code, r.text))

    def create(self):
        pass

    def _get_uri(self):
        if self.endpoint:
            return BASE_URL + self.endpoint + '/'
        else:
            print "oh herro"