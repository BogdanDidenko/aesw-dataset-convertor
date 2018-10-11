from xml.dom import minidom
import sys
import os
_path_s = sys.argv[1]
_path = os.path.split(_path_s) #'aesw2016(v1.2)_dev' #'aesw2016(v1.2)_train'
name = _path[1]
path = _path[0]

xmldoc = minidom.parse(_path_s + '.xml')
itemlist = xmldoc.getElementsByTagName('sentence')

def process(itemlist, type):
    if type == 'input':
        ignore = 'ins'
    elif type == 'target':
        ignore = 'del'

    res = []
    for i, sentence in enumerate(itemlist):
        _sent = []
        for t in sentence.childNodes:
            if t.nodeType == t.TEXT_NODE:
                _sent.append(t.nodeValue)
            elif t.tagName != ignore:
                _sent.append( "".join( x.nodeValue for x in t.childNodes) )
        res.append( "".join(_sent).strip() )

    return res

type = 'input'
res = process(itemlist, type)
with open(os.path.join(path, type + '.' + name + '.txt'), "w", encoding='utf_8') as f:
    f.write("\n".join(res))

type = 'target'
res = process(itemlist, type)
with open(os.path.join(path, type + '.' + name + '.txt'), "w", encoding='utf_8') as f:
    f.write("\n".join(res))