import sys
import requests
import json
import bs4

def traverse(element):
    attrs = {}
    for attr, value in element.attrs.iteritems():
        attrs[attr] = value
    children = element.findChildren(recursive=False)
    if not len(children):
        attrs['text'] = element.text
        return attrs if len(attrs) > 1 else element.text
    else:
        structure = attrs;
        for child in children:
            structure[child.name] = traverse(child)
        return structure

def lurk(urls, selector):
    urls = urls if type(urls) is list else [ urls ]
    output = []
    for url in urls:
        request = requests.get(url)
        dom = bs4.BeautifulSoup(request.content, 'html.parser')
        for element in dom.select(selector):
            output.append(traverse(element))
    return output

def main():
    if len(sys.argv) != 3:
        print 'Usage: lurk <url> <selector> [> <output file>]'
        sys.exit(0)
    url = sys.argv[1]
    selector = sys.argv[2]
    print json.dumps(lurk(url, selector))
