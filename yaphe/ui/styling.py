CENTER = 'center'
LEFT = 'left'
RIGHT = 'right'

class Style:
    synonyms = {}
    
    def __init__(self, **kw):
        for key in kw:
            self.__dict__[key] = kw[key]
            
    def toString(self):
        style_string = ''
        for attr in self.__dict__:
            attr_string = attr
            if attr in self.synonyms:
                attr_string = synonyms[attr]

            style_string += "%s:%s;" % (attr_string.replace('_', '-'),
                                        str(self.__dict__[attr]))

        return style_string[:-1]
    
