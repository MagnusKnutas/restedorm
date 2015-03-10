#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'magnusknutas'


class NotFoundException(Exception):
    def __init__(self, value):
        self.value = value
        super(NotFoundException, self).__init__()

    def __str__(self):
        return self.value


class ApiError(Exception):
    def __init__(self, value):
        self.value = value
        super(ApiError, self).__init__()

    def __str__(self):
        return self.value