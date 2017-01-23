#Flask-Dry-Transaction

A python package implementing the strategy of business transaction in flask microservices developement

##Simple Example
initialize:
```python
from flask_dry_transaction import Transaction, Right, Left

transaction = Transaction()
```
register with functions:
```python
@transaction.register
def is_positive(a):
    if a > 0:
        return Right(a)
    else:
        return Left("Error, is not positive.")
		
@transaction.register
def is_ten(a):
    if a is 10:
        return Right(a)
    else:
        return Left("Error, is not ten.")
```
add steps:
```python
transaction.new()
transaction.step(is_positive)
transaction.step(is_ten)
```
execute the transaction:
```python
transaction.call(-1)
transaction.call(1)
transaction.call(10)
```
##Working with class:
create a service object:
```python
class ServiceObject(object):
    transaction = Transaction()
    
    @staticmethod
    @transaction.register
    def is_positive(a):
        if a > 0:
            return Right(a)
        else:
            return Left("Error, is not positive.")
        
    @staticmethod
    @transaction.register
    def is_ten(a):
        if a is 10:
            return Right(a)
        else:
            return Left("Error, is not ten.")
        
    
    @classmethod
    def call(self, params):
        self.transaction.new()
        self.transaction.step(self.is_positive)
        self.transaction.step(self.is_ten)
        return self.transaction.call(params)
```
execute the transaction:
```python
ServiceObject.call(-1)
ServiceObject.call(1)
ServiceObject.call(10)
```
