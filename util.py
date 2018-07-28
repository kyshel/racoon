#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def as_dict(sa_result):
    return [dict(r) for r in sa_result]