import config, haml
    
class Elem(object):
    def __init__(self, tag, content='', attrs=None, self_closing=''):
        """HTML Element class
        
        Arguments:
        - `tag`:
        - `contents`:
        - `attrs`:
        """
        if not attrs:
            attrs = {}
            
        # Tag could be a line of HAML
        haml_data = haml.HamlData(tag)
        if haml_data.is_valid_haml():
            tag = haml_data.tag
            attrs = self._merge_attrs_with_haml_attrs(attrs, haml_data.attrs)
            
        self.tag = tag
        self.attrs = attrs
        
        if isinstance(content, Elem):
            content = content.render()
        self.content = content

        if not self_closing and tag in ('meta', 'img', 'link', 'br', 'hr'):
            self_closing = ' />'
        self._self_closing = self_closing
        
        self._prefix_markup = ''
        self._sub_elems = []
        self._suffix_markup = ''

    def __str__(self):
        return self.render()
        
    def _add_sub_elem(self, other):
        if self.content:
            if isinstance(other, Elem):
                other = other.render()
            self._suffix_markup = other
        elif isinstance(other, Elem):    # Nested elem since there is no content
            self._sub_elems.append(other)
        else:
            # No content and 'other' is not an Elem instance so we just
            # append it.
            self._suffix_markup = other
            
        return self
    
    def __add__(self, other):
        return self._add_sub_elem(other)

    def __iadd__(self, other):
        return self._add_sub_elem(other)

    def __radd__(self, other):
        self._prefix_markup = other
        return self

    def _merge_attrs_with_haml_attrs(self, attrs, haml_attrs):
        for key in haml_attrs:
            v = haml_attrs[key]
            if attrs.get(key):
                v |= set(attrs[key].split())
                        
            attrs[key] = ' '.join(list(v))

        return attrs
    
    def _getAttrs(self):
        attrs = ' '
        for attr in self.attrs:
            attrs += '%s="%s" ' % (attr, self.attrs[attr])

        return attrs[:-1]

    def _getIndentation(self, depth):
        indentation = ''
        if config.do_indent:
            indentation = config.indent_string * depth

        return indentation
    
    def render(self, depth=0):

        attrs = self._getAttrs()
        indentation = self._getIndentation(depth)

        elem = self._prefix_markup
        elem += "%s<%s" % (indentation, self.tag + attrs)

        if not self._self_closing:
            elem += ">"
            
        if self.content:
            elem += self.content + "</%s>" % self.tag
        elif self._self_closing:
            elem += self._self_closing
        else:
            if config.do_indent:
                elem += "\n"
                
            new_depth = depth + 1
            for sub_elem in self._sub_elems:
                elem += sub_elem.render(new_depth)

                if config.do_indent:
                    elem += "\n"
                    
            elem += "%s</%s>" % (indentation, self.tag)

        elem  += self._suffix_markup
        
        return elem
        
