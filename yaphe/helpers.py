from core import Elem

def elem(tag, content='', attrs={}, self_closing=False):
    return Elem(tag, content, attrs, self_closing)

def screen_stylsheet(href):
    return Elem("link", attrs={'rel': 'stylesheet',
                               'href': href,
                               'type': 'text/css',
                               'media': 'screen'})

def img(src, alt='', attrs={}):
    attrs['src'] = src
    if alt:
        attrs['alt'] = alt
    return Elem("img", attrs=attrs) 

def a(href, content, attrs={}):
    attrs['href'] = href
    return Elem('a', content, attrs)
