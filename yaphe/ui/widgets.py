from yaphe.core import Elem
import styling

MAX_GRID_WIDTH = 24

def widthToGridSpan(width):
    if width < 0:
        width = MAX_GRID_WIDTH

    return 'grid_%d' % width

class Label(Elem):
    def __init__(self, text, text_align=styling.CENTER, style=None, width=-1):
        attrs = {'class': widthToGridSpan(width)}
        self.text = text
        self.width = width
        
        if not style:
            style = styling.Style()

        style.text_align=text_align
        attrs['style'] = style.toString()
        
        Elem.__init__(self, 'div', text, attrs=attrs)
        
class HBox(Elem):
    def __init__(self, width=-1, height=-1):
        attrs = {'class': widthToGridSpan(width)}
        self.width = width
        self.height = height

        if height > 0:
            attrs['line-height'] = self.height
        
        Elem.__init__(self, 'div', attrs=attrs)
        

    def _add_sub_elem(self, other):
        if isinstance(other, Elem):
            if not self._sub_elems:
                other.attrs['class'] += ' alpha'
            else:
                self._sub_elems[-1].attrs['class'].replace(' omega', '')
                other.attrs['class'] += ' omega'

        return Elem._add_sub_elem(self, other)
