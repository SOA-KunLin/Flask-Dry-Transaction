#Flask-Dry-Transaction

A python package implementing the strategy of business transaction in flask microservices developement

##Simple Example
initialize:
```
from flask_dry_transaction import Transaction, Right, Left

transaction = Transaction()
```
register with functions:
```
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
```
transaction.new()
transaction.step(is_positive)
transaction.step(is_ten)
```
execute the transaction:
```
transaction.call(-1)
transaction.call(1)
transaction.call(10)
```
##Working with class:
create a service object:
```
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
```
ServiceObject.call(-1)
ServiceObject.call(1)
ServiceObject.call(10)
```
