# -*- coding: utf-8 -*-
"""
This file contains helper functions
"""
import imaplib


def imapmeta2date(meta):
    """
    extracting date from metadata
    """
    return imaplib.Internaldate2tuple(meta)


def imapmeta2flags(meta):
    """
    extracting flags from metadata
    """
    flags = imaplib.ParseFlags(meta)
    return tuple(ensure_string(flag) for flag in flags)


def imapflags2internal(flags):
    conv = {
        '\\Seen': 'R',
        '\\Answered': 'A',
        '\\Flagged': 'F',
        '\\Deleted': 'D'
    }

    return ''.join(conv[_] for _ in flags if _ in conv)


def maya2struct_time(mayadt):
    return mayadt.datetime().timetuple()


def ensure_string(val):
    if isinstance(val, bytes):
        return val.decode('ascii')

    return str(val)
