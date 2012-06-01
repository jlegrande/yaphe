from core import Elem, Page
import doctypes

def html5_page():
    return Page(doctypes.xhtml_5)

def html_transitional_page():
    return Page()

def elem(tag, content='', attrs={}, self_closing=False):
    return Elem(tag, content, attrs, self_closing)

def js_file(path):
    return Elem('script', attrs={'type': 'text/javascript',
                                 'src': path}) 
def screen_css(href):
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
