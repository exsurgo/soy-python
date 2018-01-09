# coding=utf-8
""" This file was automatically generated from custom.soy.
Please don't edit this file by hand.

SOY_NAMESPACE: 'my.namespace'.

Templates in namespace my.namespace.
"""

from __future__ import unicode_literals
from __future__ import division
import collections
import math
import random
import sys
from runtime import bidi
from runtime import directives
from runtime import runtime
from runtime import sanitize

NAMESPACE_MANIFEST = {
    'my.namespace': '.Users.exsurgo.Work.soy-python.templates.custom',
}

try:
  str = unicode
except NameError:
  pass



def fooBarTemplate(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html("Foo Bar")))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def addNumbersTemplate(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html('Sum is ' + str(data['n1'] + data['n2']))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def externalCallTemplate(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html((ijData['utils'].get('foo_bar_baz') if 'utils' in ijData else __import__('utils.utils', globals(), locals(), -1).foo_bar_baz()))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def callMethodTemplate1Param(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html(getattr(__import__('utils'), 'foo_bar_baz')('My Value 1'))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def callMethodTemplate2Params(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html(getattr(__import__('utils'), 'foo_bar_baz')('My Value 1', 'My Value 2'))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def callMethodTemplateNamedParam(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html(getattr(__import__('utils'), 'foo_bar_baz')(data.get('value')))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))
