# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def _notequal(context, row):
    return {row.index: {'query': row.values, }}
