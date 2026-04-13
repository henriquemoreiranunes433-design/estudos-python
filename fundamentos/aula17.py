class MyError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MyError('a','b','c')
    raise exception_

try:
    levantar()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OutroError('Estou lançando outro erro.')
    raise exception_ from error