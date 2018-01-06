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
    'my.namespace': '.Users.exsurgo.Work.SoyPython.templates.custom',
}

try:
  str = unicode
except NameError:
  pass



def fooBar(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html("Foo Bar")))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def addNumbers(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html('Sum is ' + str(data['n1'] + data['n2']))))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def callMethod(data={}, ijData={}):
  output = []
  output.append(str(sanitize.escape_html(getattr((__import__(data['module'])), data['method'])())))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))
