__str__ = 'error which are more certain to the system is written here'
__all__ = ['SlotError', 'SizeError', 'CarError', 'FileError']


class Error(Exception):
    pass


class FileError(Error):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class SizeError(Error):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class SlotError(Error):
    """check if it is already empty or invalid,slot error"""

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class CarError(Error):
    """ car with this color not found"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)
