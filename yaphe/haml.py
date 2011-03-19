import re

class HamlData(object):
    def __init__(self, haml_line):
        self.tag = self._extract_tag(haml_line)
        self.attrs = {}
        self._add_attrs_from_attr_hash(haml_line)
        self._add_attrs_from_shortcuts(haml_line)
        
    def _extract_tag(self, haml_line):
        """Takes a line of HAML and extracts the tag"""
        try:
            if haml_line.startswith(".") or haml_line.startswith("#"):
                return 'div'
        
            return re.match("\w+", haml_line).group(0)
        except AttributeError:
            raise RuntimeError("No tag was specified in %s" % haml_line)

    def _add_attrs_from_attr_hash(self, haml_line):
        """Takes a line of HAML and extracts the attribute hash"""
        try:
            attr_hash = re.search("\{.+\}", haml_line).group(0)
            attr_pairs = re.findall(',?\s*:(\w+)\s*=>\s*"(.+?)"\s*,?',
                                    attr_hash)
            for k, v in attr_pairs:
                self.attrs[k] = set(v.split())
        except AttributeError:
            pass

    def _add_attrs_from_shortcuts(self, haml_line):
        ids = set(re.findall("#(\w+)", haml_line))
        classes = set(re.findall("\.(\w+)", haml_line))
        for key, v in (('id', ids), ('class', classes)):
            if v:
                if self.attrs.get(key, None):
                    self.attrs[key] |= v
                else:
                    self.attrs[key] = v
        
    def is_valid_haml(self):
        return len(self.attrs.keys()) > 0
