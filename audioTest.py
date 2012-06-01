from yaphe.helpers import *
e = elem
p = html5_page()
p += e('head', e('title', 'HTML5 Audio Test'))
p += e('body', e('audio{:src=>"finishbell.ogg", :controls=>"controls"}'))
print p.render()

class DivRule:
    sel = '.acLocngCell'
