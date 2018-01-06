# coding=utf-8
""" This file was automatically generated from simple.soy.
Please don't edit this file by hand.

SOY_NAMESPACE: 'templates'.

Templates in namespace templates.
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
    'templates': '.Users.exsurgo.Work.SoyPython.templates.simple',
}

try:
  str = unicode
except NameError:
  pass



def helloWorld(data={}, ijData={}):
  output = []
  output.append('Hello world!')
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def helloName(data={}, ijData={}):
  output = []
  output.append(''.join(['Hello ',str(sanitize.escape_html(data.get('name'))),'!']) if data.get('name') else str(helloWorld({}, ijData)))
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def helloNames(data={}, ijData={}):
  output = []
  output.append('<!--dta_of(templates.helloNames, /Users/exsurgo/Work/SoyPython/templates/simple.soy, 48)-->' if False else '')
  nameList19 = data.get('names')
  if nameList19:
    for nameIndex19, nameData19 in enumerate(nameList19):
      output.extend([str(helloName({'name': nameData19}, ijData)),'<br>' if not (nameIndex19 == len(nameList19) - 1) else ''])
  else:
    output.append(str(helloWorld({}, ijData)))
  output.extend([str(sanitize.escape_html(data.get('unsafe_body'))),'<script nonce="',str(sanitize.escape_html_attribute(data.get('CSP_NONCE'))),'"',''.join([' nonce="',str(sanitize.escape_html_attribute(ijData.get('csp_nonce'))),'"']) if ijData.get('csp_nonce') else '','>alert(\'hello\');</script>','<!--dta_cf(templates.helloNames)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))
