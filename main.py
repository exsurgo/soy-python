from templates import simple
from templates import custom


print simple.helloWorld()

print simple.helloName({'name': 'Bob'})

print custom.fooBarTemplate()

print custom.addNumbersTemplate({'n1': 1, 'n2': 2})

print custom.callMethodTemplate1Param()

print custom.callMethodTemplate2Params()

print custom.callMethodTemplateNamedParam({'value': 'My Named Value'})
