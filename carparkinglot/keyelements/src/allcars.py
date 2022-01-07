
__all__ = ['Car']


class Car(object):
    

    def __init__(self, registration_number, color):
        
        self._reg_number = registration_number
        self._color = color

    @property
    def get_registration_number(self):
       
        return self._reg_number

    @property
    def get_color(self):
       
        return self._color
