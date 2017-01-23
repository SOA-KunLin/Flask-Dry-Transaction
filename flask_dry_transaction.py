class Transaction(object):
    
    def __init__(self):
        self.params = None
        self.steps = None
        self.right = None
    
    
    def step(self, func):
        self.steps.append(func)
        

    def new(self):
        self.steps = []
        
        
    def register(self, func):
        def wrapped_f():
            fork = func(self.params)
            self.params = fork[1]
            if fork[0] is False:
                self.right = False
                
        return wrapped_f
    
    
    def call(self, params):
        self.params = params
        self.right = True
        iterator = iter(self.steps)
        
        try:
            while True:
                iterator.next()()
                if self.right is False:
                    break
        except StopIteration:
            pass
        finally:
            del iterator
        
        return { "success": self.right, "params": self.params}


def Right(params):
    return (True, params)


def Left(params):
    return (False, params)
