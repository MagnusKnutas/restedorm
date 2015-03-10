#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json
import requests
from restedorm.exeptions import NotFoundException
from restedorm.managers import BaseManager

__author__ = 'magnusknutas'
import logging

logger = logging.getLogger(__name__)


class RestObject(object):
    uri = str
    objects = BaseManager

    class Meta:
        endpoint = None

    def __init__(self, *args, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])