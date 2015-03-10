#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from .managers import BaseManager

__author__ = 'magnusknutas'


class Endpoint(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def __call__(self, *args):
        if args[0].Meta.endpoint:
            args[0].objects = BaseManager(args[0], args[0].Meta.endpoint)
        else:
            args[0].objects = BaseManager(args[0], self.endpoint)

        return args[0]