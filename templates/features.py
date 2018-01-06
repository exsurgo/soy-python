# coding=utf-8
""" This file was automatically generated from features.soy.
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
    'templates': '.Users.exsurgo.Work.SoyPython.templates.features',
}

try:
  str = unicode
except NameError:
  pass



def demoComments(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoComments, /Users/exsurgo/Work/SoyPython/templates/features.soy, 24)-->' if False else '','blah blah<br>http://www.google.com<br>','<!--dta_cf(templates.demoComments)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoLineJoining(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoLineJoining, /Users/exsurgo/Work/SoyPython/templates/features.soy, 36)-->' if False else '','First second.<br><i>First</i>second.<br>Firstsecond.<br><i>First</i> second.<br>Firstsecond.<br>','<!--dta_cf(templates.demoLineJoining)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoRawTextCommands(data={}, ijData={}):
  output = []
  output.append('<pre>Space       : AA BB<br>Empty string: AABB<br>New line    : AA\nBB<br>Carriage ret: AA\rBB<br>Tab         : AA\tBB<br>Left brace  : AA{BB<br>Right brace : AA}BB<br>Literal     : AA\tBB { CC\n  DD } EE {sp}{\\n}{rb} FF</pre>')
  return sanitize.UnsanitizedText(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoPrint(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoPrint, /Users/exsurgo/Work/SoyPython/templates/features.soy, 94)-->' if False else '','Boo!<br>Boo!<br>3<br>',str(sanitize.escape_html(data.get('boo'))),'<br>',str(sanitize.escape_html(runtime.type_safe_add(1, data.get('two')))),'<br>','<!--dta_cf(templates.demoPrint)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoAutoescapeTrue(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoAutoescapeTrue, /Users/exsurgo/Work/SoyPython/templates/features.soy, 108)-->' if False else '',str(sanitize.escape_html(data.get('italicHtml'))),'<br>','<!--dta_cf(templates.demoAutoescapeTrue)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoMsg(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoMsg, /Users/exsurgo/Work/SoyPython/templates/features.soy, 121)-->' if False else '',translator_impl.render(translator_impl.prepare(6936162475751860807, 'Hello {NAME}!', ('NAME',)), {'NAME': str(sanitize.escape_html(data.get('name')))}),'<br>',translator_impl.render(translator_impl.prepare(5539341884085868292, 'Click {START_LINK}here{END_LINK} to access Labs.', ('START_LINK', 'END_LINK')), {'START_LINK': ''.join(['<a href="',str(sanitize.escape_html_attribute(sanitize.filter_normalize_uri(data.get('labsUrl')))),'">']), 'END_LINK': '</a>'}),'<br>',translator_impl.render_literal(translator_impl.prepare_literal(7224011416745566687, 'Archive')),'<br>',translator_impl.render_literal(translator_impl.prepare_literal(4826315192146469447, 'Archive')),'<br>','<!--dta_cf(templates.demoMsg)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoIf(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoIf, /Users/exsurgo/Work/SoyPython/templates/features.soy, 150)-->' if False else '',translator_impl.render(translator_impl.prepare(6820146346443344314, '{PI} is a good approximation of pi.', ('PI',)), {'PI': str(sanitize.escape_html(data.get('pi')))}) if runtime.type_safe_eq(runtime.simplify_num(round((math.frexp(data.get('pi'))[0] + sys.float_info.epsilon)*2**math.frexp(data.get('pi'))[1], 2), 2), 3.14) else translator_impl.render(translator_impl.prepare(6820284805811944992, '{PI} is a bad approximation of pi.', ('PI',)), {'PI': str(sanitize.escape_html(data.get('pi')))}) if runtime.type_safe_eq(runtime.simplify_num(round((math.frexp(data.get('pi'))[0] + sys.float_info.epsilon)*2**math.frexp(data.get('pi'))[1], 0), 0), 3) else translator_impl.render(translator_impl.prepare(889614911019327165, '{PI} is nowhere near the value of pi.', ('PI',)), {'PI': str(sanitize.escape_html(data.get('pi')))}),'<br>','<!--dta_cf(templates.demoIf)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoSwitch(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoSwitch, /Users/exsurgo/Work/SoyPython/templates/features.soy, 172)-->' if False else '','Dear ',str(sanitize.escape_html(data.get('name'))),', &nbsp;']
  switchValue = data.get('name')
  if runtime.type_safe_eq(switchValue, 'Go'):
    output.append('You\'ve been bad this year.')
  elif runtime.type_safe_eq(switchValue, 'Fay'):
    output.append('You\'ve been good this year.')
  elif runtime.type_safe_eq(switchValue, 'Ivy'):
    output.append('You\'ve been good this year.')
  else:
    output.append('You don\'t really believe in me, do you?')
  output.extend(['&nbsp; --Santa<br>','<!--dta_cf(templates.demoSwitch)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoForeach(data={}, ijData={}):
  output = []
  output.append('<!--dta_of(templates.demoForeach, /Users/exsurgo/Work/SoyPython/templates/features.soy, 192)-->' if False else '')
  personList98 = data.get('persons')
  if personList98:
    for personIndex98, personData98 in enumerate(personList98):
      output.extend(['First,' if personIndex98 == 0 else 'Finally,' if personIndex98 == len(personList98) - 1 else 'Then',' ',''.join([str(sanitize.escape_html(personData98.get('name'))),' ate 1 waffle.']) if runtime.type_safe_eq(personData98.get('numWaffles'), 1) else ''.join([str(sanitize.escape_html(personData98.get('name'))),' ate ',str(sanitize.escape_html(personData98.get('numWaffles'))),' waffles.']),'<br>'])
  else:
    output.append('Nobody here ate any waffles.<br>')
  output.append('<!--dta_cf(templates.demoForeach)-->' if False else '')
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoFor(data={}, ijData={}):
  output = []
  output.append('<!--dta_of(templates.demoFor, /Users/exsurgo/Work/SoyPython/templates/features.soy, 224)-->' if False else '')
  for i126 in xrange(0, data.get('numLines'), 1):
    output.extend(['Line ',str(sanitize.escape_html(runtime.type_safe_add(i126, 1))),' of ',str(sanitize.escape_html(data.get('numLines'))),'.<br>'])
  for i133 in xrange(2, 10, 2):
    output.extend([str(sanitize.escape_html(i133)),'... '])
  output.extend(['Who do we appreciate?<br>','<!--dta_cf(templates.demoFor)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoCallWithoutParam(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoCallWithoutParam, /Users/exsurgo/Work/SoyPython/templates/features.soy, 243)-->' if False else '',str(sanitize.escape_html(tripReport_({}, ijData))),'<br>',str(sanitize.escape_html(tripReport_(data, ijData))),'<br>',str(sanitize.escape_html(tripReport_(data.get('tripInfo'), ijData))),'<br>','<!--dta_cf(templates.demoCallWithoutParam)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoCallWithParam(data={}, ijData={}):
  output = []
  output.append('<!--dta_of(templates.demoCallWithParam, /Users/exsurgo/Work/SoyPython/templates/features.soy, 276)-->' if False else '')
  destinationList148 = data.get('destinations')
  for destinationIndex148, destinationData148 in enumerate(destinationList148):
    output.extend([str(sanitize.escape_html(tripReport_(runtime.merge_into_dict(dict(data), {'destination': destinationData148}), ijData))),'<br>',''.join([str(sanitize.escape_html(tripReport_({'name': data.get('companionName'), 'destination': destinationData148}, ijData))),'<br>']) if runtime.type_safe_eq(destinationIndex148 % 2, 0) else ''])
  output.append('<!--dta_cf(templates.demoCallWithParam)-->' if False else '')
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoCallWithParamBlock(data={}, ijData={}):
  output = []
  output.append('<!--dta_of(templates.demoCallWithParamBlock, /Users/exsurgo/Work/SoyPython/templates/features.soy, 305)-->' if False else '')
  param175 = []
  switchValue = random.randint(0, 3 - 1)
  if runtime.type_safe_eq(switchValue, 0):
    param175.append('Boston')
  elif runtime.type_safe_eq(switchValue, 1):
    param175.append('Singapore')
  elif runtime.type_safe_eq(switchValue, 2):
    param175.append('Zurich')
  output.append(str(sanitize.escape_html(tripReport_({'name': data.get('name'), 'destination': sanitize.UnsanitizedText(''.join(param175), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))}, ijData))))
  output.extend(['<br>','<!--dta_cf(templates.demoCallWithParamBlock)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def tripReport_(data={}, ijData={}):
  output = []
  output.append(translator_impl.render_literal(translator_impl.prepare_literal(3329840836245051515, 'A trip was taken.')) if not data.get('name') else translator_impl.render(translator_impl.prepare(3179387603303514412, '{NAME} took a trip.', ('NAME',)), {'NAME': str(data.get('name'))}) if not data.get('destination') else translator_impl.render(translator_impl.prepare(768490705511913603, '{NAME} took a trip to {DESTINATION}.', ('NAME', 'DESTINATION')), {'NAME': str(data.get('name')), 'DESTINATION': str(data.get('destination'))}))
  return sanitize.UnsanitizedText(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoParamWithKindAttribute(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoParamWithKindAttribute, /Users/exsurgo/Work/SoyPython/templates/features.soy, 355)-->' if False else '','<div>']
  param221 = []
  iList215 = data.get('list')
  for iIndex215, iData215 in enumerate(iList215):
    param221.extend(['<li>',str(sanitize.escape_html(iData215)),'</li>'])
  output.append(str(demoParamWithKindAttributeCallee_({'message': sanitize.SanitizedHtml(''.join(['<b>',str(sanitize.escape_html(data.get('message'))),'</b>']), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.')), 'listItems': sanitize.SanitizedHtml(''.join(param221), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))}, ijData)))
  output.extend(['</div>','<!--dta_cf(templates.demoParamWithKindAttribute)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoParamWithKindAttributeCallee_(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoParamWithKindAttributeCallee_, /Users/exsurgo/Work/SoyPython/templates/features.soy, 380)-->' if False else '','<div>',str(sanitize.escape_html(data.get('message'))),'</div><ol>',str(sanitize.escape_html(data.get('listItems'))),'</ol>','<!--dta_cf(templates.demoParamWithKindAttributeCallee_)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoExpressions(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoExpressions, /Users/exsurgo/Work/SoyPython/templates/features.soy, 397)-->' if False else '','First student\'s major: ',str(sanitize.escape_html(runtime.key_safe_data_access(data.get('students'), 0).get('major'))),'<br>Last student\'s year: ',str(sanitize.escape_html(runtime.key_safe_data_access(data.get('students'), len(data.get('students')) - 1).get('year'))),'<br>Random student\'s major: ',str(sanitize.escape_html(runtime.key_safe_data_access(data.get('students'), random.randint(0, len(data.get('students')) - 1)).get('major'))),'<br>']
  studentList240 = data.get('students')
  for studentIndex240, studentData240 in enumerate(studentList240):
    output.extend([str(sanitize.escape_html(studentData240.get('name'))),':',' First.' if studentIndex240 == 0 else ' Last.' if studentIndex240 == len(studentList240) - 1 else ' Middle.' if runtime.type_safe_eq(studentIndex240, int(math.ceil(len(data.get('students')) / 2)) - 1) else '',' Even.' if runtime.type_safe_eq(studentIndex240 % 2, 1) else '',' ',str(sanitize.escape_html(studentData240.get('major'))),'.',' Scientist.' if runtime.type_safe_eq(studentData240.get('major'), 'Physics') or runtime.type_safe_eq(studentData240.get('major'), 'Biology') else '',' Young.' if data.get('currentYear') - studentData240.get('year') < 10 else '',' ',str(sanitize.escape_html(runtime.type_safe_add(runtime.simplify_num(round((math.frexp(studentData240.get('year') - 1905)[0] + sys.float_info.epsilon)*2**math.frexp(studentData240.get('year') - 1905)[1], -1), -1), 's') if studentData240.get('year') < 2000 else '00s')),'. ',str(sanitize.escape_html(runtime.simplify_num(round((math.frexp(studentData240.get('year') - 1905)[0] + sys.float_info.epsilon)*2**math.frexp(studentData240.get('year') - 1905)[1], -1), -1))) if studentData240.get('year') < 2000 else '00','s.<br>'])
  output.append('<!--dta_cf(templates.demoExpressions)-->' if False else '')
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoDoubleBraces(data={}, ijData={}):
  output = []
  output.append(translator_impl.render(translator_impl.prepare(135956960462609535, 'The set of {SET_NAME} is {{{XXX}, ...}}.', ('SET_NAME', 'XXX')), {'SET_NAME': str(data.get('setName')), 'XXX': str(buildCommaSeparatedList_({'items': data.get('setMembers')}, ijData))}))
  return sanitize.UnsanitizedText(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def buildCommaSeparatedList_(data={}, ijData={}):
  output = []
  itemList290 = data.get('items')
  for itemIndex290, itemData290 in enumerate(itemList290):
    output.extend([', ' if not (itemIndex290 == 0) else '',str(itemData290)])
  return sanitize.UnsanitizedText(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def demoBidiSupport(data={}, ijData={}):
  output = ['<!--dta_of(templates.demoBidiSupport, /Users/exsurgo/Work/SoyPython/templates/features.soy, 476)-->' if False else '','<div id="title1" style="font-variant:small-caps" ',str(sanitize.filter_html_attributes(bidi.dir_attr(1, data.get('title')))),'>',str(sanitize.escape_html(data.get('title'))),'</div><div id="title2" style="font-variant:small-caps">',str(bidi.span_wrap(1, sanitize.escape_html(data.get('title')))),'</div>',translator_impl.render(translator_impl.prepare(7036633296476174078, 'by {AUTHOR} ({YEAR})', ('AUTHOR', 'YEAR')), {'AUTHOR': str(bidi.span_wrap(1, sanitize.escape_html(data.get('author')))), 'YEAR': str(sanitize.escape_html(data.get('year')))}),'<div id="choose_a_keyword">',translator_impl.render_literal(translator_impl.prepare_literal(2209690285855487595, 'Your favorite keyword')),': <select>']
  keywordList324 = data.get('keywords')
  for keywordIndex324, keywordData324 in enumerate(keywordList324):
    output.extend(['<option value="',str(sanitize.escape_html_attribute(keywordData324)),'">',str(sanitize.escape_html(bidi.unicode_wrap(1, keywordData324))),'</option>'])
  output.extend(['</select></div><a href="#" style="float:',str(sanitize.escape_html_attribute(sanitize.filter_css_value('left' if (1) < 0 else 'right'))),'">',translator_impl.render_literal(translator_impl.prepare_literal(7911416166208830577, 'Help')),'</a><br>','<!--dta_cf(templates.demoBidiSupport)-->' if False else ''])
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def bidiGlobalDir(data={}, ijData={}):
  output = []
  output.append(str(1))
  return sanitize.UnsanitizedText(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))


def exampleHeader(data={}, ijData={}):
  output = ['<!--dta_of(templates.exampleHeader, /Users/exsurgo/Work/SoyPython/templates/features.soy, 556)-->' if False else '','<hr><b>',str(sanitize.escape_html(data.get('exampleNum'))),'. ',str(sanitize.escape_html(data.get('exampleName'))),'</b><br>','<!--dta_cf(templates.exampleHeader)-->' if False else '']
  return sanitize.SanitizedHtml(''.join(output), approval=sanitize.IActuallyUnderstandSoyTypeSafetyAndHaveSecurityApproval('Internally created Sanitization.'))
