class ErrorDate(Exception):
    def __init__(self,mesage):
        self.message = mesage
    def __str__(self):
        return 'Error date compiler'

class ErrorAllowedValue(Exception):
    def __init__(self,mesage):
        self.message = mesage
    def __str__(self):
        return 'Error allowed value'


