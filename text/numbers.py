""" from https://github.com/keithito/tacotron """

import inflect
import re
from vietnam_number import n2w, w2n

_inflect = inflect.engine()
_comma_number_re = re.compile(r'([0-9][0-9\,]+[0-9])')
_decimal_number_re = re.compile(r'([0-9]+\.[0-9]+)')
_pounds_re = re.compile(r'£([0-9\,]*[0-9]+)')
_dollars_re = re.compile(r'\$([0-9\.\,]*[0-9]+)')
_ordinal_re = re.compile(r'[0-9]+(st|nd|rd|th)')
_number_re = re.compile(r'[0-9]+')


def _remove_commas(m):
  return m.group(1).replace(',', '')


def _expand_decimal_point(m):
  return m.group(1).replace('.', ' chấm ')

def expand_ordinal(m):
    tmp = m.group(0)
    tmp = tmp.replace("st", "")
    tmp = tmp.replace("nd", "")
    tmp = tmp.replace("rd", "")
    tmp = tmp.replace("th", "")
    return n2w(tmp)


def expand_number(m):
    '''
    Convert number to words
    :param m:
    :return:
    '''
    num = m.group(0)
    return n2w(num)


def normalize_numbers(text):
    text = re.sub(_comma_number_re, _remove_commas, text)
    text = re.sub(_decimal_number_re, _expand_decimal_point, text)
    text = re.sub(_ordinal_re, expand_ordinal, text)
    text = re.sub(_number_re, expand_number, text)
    return text