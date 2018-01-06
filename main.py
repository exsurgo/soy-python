from templates import simple
from templates import custom


print simple.helloWorld()

print simple.helloName({'name': 'Bob'})

print custom.fooBar()

print custom.addNumbers({'n1': 1, 'n2': 2})

print custom.callMethod({'module': 'utils', 'method': 'foo_bar_baz'})
